from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import scipy.stats
from matplotlib.scale import ScaleBase, register_scale

from .locators import ProbabilityLocator
from .transforms import ProbabilityTransform, ProbitTransform, ProbabilityFormatter


class ProbabilityScale(ScaleBase):
    """
    Probability scale for data between zero and one, both excluded.

    Send p -> dist.ppf(p)
    It maps the interval ]0, 1[ onto ]-infty, +infty[.
    """
    name = 'probability'

    # noinspection PyUnusedLocal
    def __init__(self, axis, dist, nonpos='mask', percentage=True, **kwargs):
        """
        *nonpos*: ['mask' | 'clip' ]
          values beyond ]0, 1[ can be masked as invalid, or clipped to a number
          very close to 0 or 1
        """
        if nonpos not in ['mask', 'clip']:
            raise ValueError("nonposx, nonposy kwarg must be 'mask' or 'clip'")

        self._transform = ProbabilityTransform(dist, nonpos, **kwargs)
        self.percentage = percentage
        # self.minor = minor

    def get_transform(self):
        """
        Return a :class:`ProbitTransform` instance.
        """
        return self._transform

    def set_default_locators_and_formatters(self, axis):
        # ..., 0.01, 0.1, 0.5, 0.9, 0.99, ...
        axis.set_minor_formatter(ProbabilityFormatter(percentage=self.percentage))
        axis.set_major_formatter(ProbabilityFormatter(percentage=self.percentage))
        axis.set_major_locator(ProbabilityLocator())
        axis.set_minor_locator(ProbabilityLocator(minor=True))

    def limit_range_for_scale(self, vmin, vmax, minpos):
        """
        Limit the domain to values between 0 and 1 (excluded).
        """
        return (vmin <= 0 and minpos or vmin,
                vmax >= 1 and (1 - minpos) or vmax)


class ProbitScale(ProbabilityScale):
    """
    Probability scale for data between zero and one, both excluded.

    Send p -> phi^-1(p), where phi(x) = CDF for a normal N(0, 1) distribution
    I.e. probit(p) == x  <==>  p == (1/sqrt(2pi)) * Integral exp(-t^2/2)dt over ]-infty, x]

    It maps the interval ]0, 1[ onto ]-infty, +infty[.
    """
    name = 'probit'

    def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
        """
        *axis*:
          unused, compatibility with ProbabilityScale
        *dist_args*:
           passed to constructor of scipy.stats.{dist}(*dist_args, **dist_kwargs)
        *dist_kwargs*:
           passed to constructor of scipy.stats.{dist}(*dist_args, **dist_kwargs)
        *nonpos*: ['mask' | 'clip' ]
          values beyond ]0, 1[ can be masked as invalid, or clipped to a number
          very close to 0 or 1
        *percentage*: [True | False]
          Display probability values as percentages
        """
        args = dist_args or []
        kwargs = dist_kwargs or {}
        dist = scipy.stats.norm(*args, **kwargs)
        ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)
        self._transform = ProbitTransform(dist, nonpos)


register_scale(ProbitScale)

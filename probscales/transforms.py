# See https://github.com/matplotlib/matplotlib/pull/3753 for the pull request for logit scale
# See http://nbviewer.jupyter.org/gist/pierre-haessig/7e3e6a818edeb6819708 for an example using the logit scale

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
import scipy.stats
from matplotlib.ticker import (Formatter, is_decade)
from matplotlib.transforms import Transform

from .locators import MIN_PROB, MAX_PROB


class ProbabilityFormatter(Formatter):
    """Probability formatter (using Math text)"""
    def __init__(self, percentage=False):
        self.percentage = percentage

    def __call__(self, x, pos=None):
        if self.percentage:
            x = (100.0 * x)
            if x > 99.9:
                s = '{:.2f}%'.format(x)
            elif x > 99:
                s = '{:.1f}%'.format(x)
            elif x >= 1:
                s = '{:.0f}%'.format(x)
            elif x >= 0.1:
                s = '{:.1f}%'.format(x)
            else:
                s = '{:.2f}%'.format(x)
            return s

        if 0.01 <= x <= 0.99:
            s = '{:.2f}'.format(x)
        elif x < 0.01:
            lx = np.floor(np.log10(x))
            if lx >= -3:
                s = '{:.3f}'.format(x)
            elif is_decade(x):
                s = '$10^{{{:.0f}}}$'.format(np.log10(x))
            else:
                s = '${:.3f}$'.format(x)
        else:  # x > 0.99
            lx = np.floor(np.log10(1-x))
            if lx >= -3:
                s = '{:.3f}'.format(x)
            else:
                s = '{:.4f}$'.format(x)
        return s

    def format_data_short(self, value):
        """return a short formatted string representation of a number"""
        return '%-12g' % value


def _mask_non_probit(a):
    """
    Return a Numpy array where all values outside ]0, 1[ are
    replaced with NaNs. If all values are inside ]0, 1[, the original
    array is returned.
    """
    # print(a)
    conds = [(a < 0.0), (a > 1.0), a == 0.0, a == 1.0]
    if any([_.any() for _ in conds]):
        return np.select(conds, [-np.inf, np.inf, MIN_PROB, MAX_PROB])
    return a


def _clip_non_probit(a):
    with np.errstate(invalid="ignore"):
        a = np.array(a, float)
        return np.select([a <= 0.0, a > 1.0], [MIN_PROB, MAX_PROB])


# noinspection PyAbstractClass
class ProbabilityTransform(Transform):
    input_dims = 1
    output_dims = 1
    is_separable = True
    has_inverse = True

    def __init__(self, dist, nonpos, **kwargs):
        Transform.__init__(self)
        self.dist = dist
        if nonpos == 'mask':
            self._handle_nonpos = _mask_non_probit
        else:
            self._handle_nonpos = _clip_non_probit
        self._nonpos = nonpos

    def transform_non_affine(self, a):
        """Probability transform (base 10), masked or clipped"""
        a2 = self._handle_nonpos(a)
        return np.nan_to_num(self.dist.ppf(1.0 * a2))

    def inverted(self):
        return ProbabilityCDFTransform(self.dist, self._nonpos)


# noinspection PyAbstractClass
class ProbabilityCDFTransform(Transform):
    input_dims = 1
    output_dims = 1
    is_separable = True
    has_inverse = True

    def __init__(self, dist, nonpos='mask'):
        Transform.__init__(self)
        self.dist = dist
        self._nonpos = nonpos

    def transform_non_affine(self, a):
        """Apply the distribution's CDF"""
        return self.dist.cdf(a)

    def inverted(self):
        return ProbabilityTransform(self.dist, self._nonpos)


# noinspection PyAbstractClass
class ProbitTransform(ProbabilityTransform):
    def __init__(self, dist=None, nonpos='mask', **kwargs):
        if dist is None:
            dist = scipy.stats.norm(**kwargs)
        ProbabilityTransform.__init__(self, dist, nonpos=nonpos)

    def inverted(self):
        return NormalCDFTransform(self.dist, self._nonpos)


# noinspection PyAbstractClass
class NormalCDFTransform(ProbabilityCDFTransform):
    def __init__(self, dist, nonpos='mask', **kwargs):
        if dist is None:
            dist = scipy.stats.norm(**kwargs)
        ProbabilityCDFTransform.__init__(self, dist, nonpos=nonpos)

    def transform_non_affine(self, a):
        """normal distribution CDF"""
        return scipy.stats.norm.cdf(a)

    def inverted(self):
        return ProbitTransform(self.dist, self._nonpos)



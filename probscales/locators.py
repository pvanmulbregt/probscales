from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
from matplotlib.ticker import (Locator)

MIN_PROB = 1e-10
MAX_PROB = 1 - 1e-10


class ProbabilityLocator(Locator):
    """
    Determine the tick locations for ProbabilityScale axes
    """

    def __init__(self, minor=False):
        """
        place ticks on the Probability locations
        """
        self.minor = minor

    def set_params(self, minor=None):
        """Set parameters within this locator."""
        if minor is not None:
            self.minor = minor

    def __call__(self):
        """Return the locations of the ticks"""
        vmin, vmax = self.axis.get_view_interval()
        return self.tick_values(vmin, vmax)

    def tick_values(self, vmin, vmax):
        # dummy axis has no axes attribute
        if hasattr(self.axis, 'axes') and self.axis.axes.name == 'polar':
            raise NotImplementedError('Polar axis cannot be Probability scaled yet')

        vmin, vmax = self.nonsingular(vmin, vmax)

        # usual_major_values = [0.001, 0.005, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 0.98, 0.995, 0.999]
        # Drop 0.01=1.0% (or 99.0%),
        # Drop 0.002=0.2% (or 99.8%)
        if 0:
            usual_major_values = [0.001, 0.005, 0.02, 0.05, 0.1, 0.2]
            usual_minor_values = usual_major_values + [0.3, 0.4]
            usual_major_values = usual_major_values + [0.5] + list(reversed([1 - _ for _ in usual_major_values]))
            usual_minor_values = usual_minor_values + [0.5] + list(reversed([1 - _ for _ in usual_minor_values]))
        else:
            usual_major_values = [0.001, 0.005, 0.02, 0.05, 0.1, 0.2]
            usual_minor_values = [0.3, 0.4]
            usual_major_values = usual_major_values + [0.5] + list(reversed([1 - _ for _ in usual_major_values]))
            usual_minor_values = usual_minor_values + list(reversed([1 - _ for _ in usual_minor_values]))
        # decade_min = 0
        # if vmin < 0.5:
        #     decade_min = np.floor(np.log10(vmin))
        # decade_max = 0
        # if vmax > 0.5:
        #     decade_max = np.ceil(np.log10(1-vmax))

        # major ticks
        if not self.minor:
            ticklocs = [x for x in usual_major_values if vmin <= x <= vmax]
        # minor ticks
        else:
            ticklocs = [x for x in usual_minor_values if vmin <= x <= vmax]

        return self.raise_if_exceeds(np.array(ticklocs))

    def nonsingular(self, vmin, vmax):
        initial_range = (MIN_PROB, MAX_PROB)
        if not np.isfinite(vmin) or not np.isfinite(vmax):
            return initial_range  # no data plotted yet

        if vmin > vmax:
            vmin, vmax = vmax, vmin

        # what to do if a window beyond ]0, 1[ is chosen
        if self.axis is not None:
            minpos = self.axis.get_minpos()
            if not np.isfinite(minpos):
                return initial_range  # again, no data plotted
        else:
            minpos = MIN_PROB  # should not occur in normal use

        # NOTE: for vmax, we should query a property similar to get_minpos, but
        # related to the maximal, less-than-one data point. Unfortunately,
        # Bbox._minpos is defined very deep in the BBox and updated with data,
        # so for now we use 1 - minpos as a substitute.

        if vmin <= 0:
            vmin = minpos
        if vmax >= 1:
            vmax = 1 - minpos
        if vmin == vmax:
            return 0.1 * vmin, 1 - 0.1 * vmin

        return vmin, vmax

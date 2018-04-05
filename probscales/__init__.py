r"""
Create matplotlib Scales from scipy's continuous probability distributions.

E.g.
  >>> import matplotlib.pyplot as plt
  >>> import probscales
  >>> plt.plot(x_data, y_data, scale="normal")
  >>> plt.plot(x_data, y_data, scale="normal", dist_kwargs={"loc" : 1, "scale" : 2})

The Scale "xxx"  scales the axis according to scipy.stats.xxx.ppf().
The Scale named "probit" is the same as the scale named "normal".
"""

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Import-ing scipyscales is needed to register all scipy Scales
# with matplotlib.scale
from .scipyscales import get_scale_prefix, get_scale_names  # nopep8

__all__ = ['get_scale_names', 'get_scale_prefix']

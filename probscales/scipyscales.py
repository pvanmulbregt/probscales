
from __future__ import (absolute_import, division, print_function, unicode_literals)

import scipy.stats
from matplotlib.scale import register_scale

from .scales import ProbabilityScale

_PREFIX = ''


def get_scale_prefix():
    """return the prefix applied to the scipy.prob distribution names when generating the scale names"""
    return _PREFIX

# Holds all the names of generated Scales
_prob_scales = []


def get_scale_names():
    """Return the list of probability scale names"""
    return _prob_scales


def _record_scale(scale):
    """Record the name of the scale locally before passing on to matplotlib"""
    global _prob_scales
    _prob_scales.append(scale.name)
    register_scale(scale)


#################################################
try:
    scipy.stats.alpha
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class AlphaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.alpha distribution.

        Send p -> CDF^-1(p) = scipy.stats.alpha.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.alpha.pdf(t)dt over ]-infty, x]
        """
        name = 'alpha'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.alpha(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.alpha(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.alpha(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(AlphaScale)


#################################################
try:
    scipy.stats.anglit
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class AnglitScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.anglit distribution.

        Send p -> CDF^-1(p) = scipy.stats.anglit.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.anglit.pdf(t)dt over ]-infty, x]
        """
        name = 'anglit'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.anglit(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.anglit(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.anglit(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(AnglitScale)


#################################################
try:
    scipy.stats.arcsine
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ArcsineScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.arcsine distribution.

        Send p -> CDF^-1(p) = scipy.stats.arcsine.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.arcsine.pdf(t)dt over ]-infty, x]
        """
        name = 'arcsine'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.arcsine(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.arcsine(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.arcsine(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ArcsineScale)


#################################################
try:
    scipy.stats.argus
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ArgusScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.argus distribution.

        Send p -> CDF^-1(p) = scipy.stats.argus.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.argus.pdf(t)dt over ]-infty, x]
        """
        name = 'argus'
        ctor_args = ['chi']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.argus(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.argus(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.argus(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ArgusScale)


#################################################
try:
    scipy.stats.beta
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class BetaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.beta distribution.

        Send p -> CDF^-1(p) = scipy.stats.beta.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.beta.pdf(t)dt over ]-infty, x]
        """
        name = 'beta'
        ctor_args = ['a', 'b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.beta(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.beta(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.beta(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(BetaScale)


#################################################
try:
    scipy.stats.betaprime
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class BetaprimeScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.betaprime distribution.

        Send p -> CDF^-1(p) = scipy.stats.betaprime.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.betaprime.pdf(t)dt over ]-infty, x]
        """
        name = 'betaprime'
        ctor_args = ['a', 'b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.betaprime(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.betaprime(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.betaprime(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(BetaprimeScale)


#################################################
try:
    scipy.stats.bradford
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class BradfordScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.bradford distribution.

        Send p -> CDF^-1(p) = scipy.stats.bradford.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.bradford.pdf(t)dt over ]-infty, x]
        """
        name = 'bradford'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.bradford(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.bradford(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.bradford(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(BradfordScale)


#################################################
try:
    scipy.stats.burr
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class BurrScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.burr distribution.

        Send p -> CDF^-1(p) = scipy.stats.burr.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.burr.pdf(t)dt over ]-infty, x]
        """
        name = 'burr'
        ctor_args = ['c', 'd']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.burr(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.burr(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.burr(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(BurrScale)


#################################################
try:
    scipy.stats.burr12
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Burr12Scale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.burr12 distribution.

        Send p -> CDF^-1(p) = scipy.stats.burr12.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.burr12.pdf(t)dt over ]-infty, x]
        """
        name = 'burr12'
        ctor_args = ['c', 'd']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.burr12(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.burr12(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.burr12(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Burr12Scale)


#################################################
try:
    scipy.stats.cauchy
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class CauchyScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.cauchy distribution.

        Send p -> CDF^-1(p) = scipy.stats.cauchy.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.cauchy.pdf(t)dt over ]-infty, x]
        """
        name = 'cauchy'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.cauchy(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.cauchy(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.cauchy(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(CauchyScale)


#################################################
try:
    scipy.stats.chi
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ChiScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.chi distribution.

        Send p -> CDF^-1(p) = scipy.stats.chi.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.chi.pdf(t)dt over ]-infty, x]
        """
        name = 'chi'
        ctor_args = ['df']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.chi(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.chi(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.chi(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ChiScale)


#################################################
try:
    scipy.stats.chi2
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Chi2Scale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.chi2 distribution.

        Send p -> CDF^-1(p) = scipy.stats.chi2.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.chi2.pdf(t)dt over ]-infty, x]
        """
        name = 'chi2'
        ctor_args = ['df']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.chi2(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.chi2(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.chi2(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Chi2Scale)


#################################################
try:
    scipy.stats.cosine
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class CosineScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.cosine distribution.

        Send p -> CDF^-1(p) = scipy.stats.cosine.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.cosine.pdf(t)dt over ]-infty, x]
        """
        name = 'cosine'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.cosine(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.cosine(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.cosine(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(CosineScale)


#################################################
try:
    scipy.stats.crystalball
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class CrystalballScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.crystalball distribution.

        Send p -> CDF^-1(p) = scipy.stats.crystalball.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.crystalball.pdf(t)dt over ]-infty, x]
        """
        name = 'crystalball'
        ctor_args = ['beta', 'm']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.crystalball(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.crystalball(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.crystalball(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(CrystalballScale)


#################################################
try:
    scipy.stats.dgamma
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class DgammaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.dgamma distribution.

        Send p -> CDF^-1(p) = scipy.stats.dgamma.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.dgamma.pdf(t)dt over ]-infty, x]
        """
        name = 'dgamma'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.dgamma(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.dgamma(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.dgamma(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(DgammaScale)


#################################################
try:
    scipy.stats.dweibull
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class DweibullScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.dweibull distribution.

        Send p -> CDF^-1(p) = scipy.stats.dweibull.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.dweibull.pdf(t)dt over ]-infty, x]
        """
        name = 'dweibull'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.dweibull(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.dweibull(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.dweibull(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(DweibullScale)


#################################################
try:
    scipy.stats.erlang
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ErlangScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.erlang distribution.

        Send p -> CDF^-1(p) = scipy.stats.erlang.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.erlang.pdf(t)dt over ]-infty, x]
        """
        name = 'erlang'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.erlang(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.erlang(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.erlang(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ErlangScale)


#################################################
try:
    scipy.stats.expon
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ExponScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.expon distribution.

        Send p -> CDF^-1(p) = scipy.stats.expon.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.expon.pdf(t)dt over ]-infty, x]
        """
        name = 'expon'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.expon(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.expon(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.expon(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ExponScale)


#################################################
try:
    scipy.stats.exponnorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ExponnormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.exponnorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.exponnorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.exponnorm.pdf(t)dt over ]-infty, x]
        """
        name = 'exponnorm'
        ctor_args = ['K']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.exponnorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.exponnorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.exponnorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ExponnormScale)


#################################################
try:
    scipy.stats.exponpow
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ExponpowScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.exponpow distribution.

        Send p -> CDF^-1(p) = scipy.stats.exponpow.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.exponpow.pdf(t)dt over ]-infty, x]
        """
        name = 'exponpow'
        ctor_args = ['b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.exponpow(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.exponpow(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.exponpow(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ExponpowScale)


#################################################
try:
    scipy.stats.exponweib
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ExponweibScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.exponweib distribution.

        Send p -> CDF^-1(p) = scipy.stats.exponweib.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.exponweib.pdf(t)dt over ]-infty, x]
        """
        name = 'exponweib'
        ctor_args = ['a', 'c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.exponweib(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.exponweib(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.exponweib(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ExponweibScale)


#################################################
try:
    scipy.stats.f
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class FScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.f distribution.

        Send p -> CDF^-1(p) = scipy.stats.f.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.f.pdf(t)dt over ]-infty, x]
        """
        name = 'f'
        ctor_args = ['dfn', 'dfd']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.f(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.f(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.f(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(FScale)


#################################################
try:
    scipy.stats.fatiguelife
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class FatiguelifeScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.fatiguelife distribution.

        Send p -> CDF^-1(p) = scipy.stats.fatiguelife.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.fatiguelife.pdf(t)dt over ]-infty, x]
        """
        name = 'fatiguelife'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.fatiguelife(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.fatiguelife(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.fatiguelife(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(FatiguelifeScale)


#################################################
try:
    scipy.stats.fisk
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class FiskScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.fisk distribution.

        Send p -> CDF^-1(p) = scipy.stats.fisk.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.fisk.pdf(t)dt over ]-infty, x]
        """
        name = 'fisk'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.fisk(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.fisk(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.fisk(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(FiskScale)


#################################################
try:
    scipy.stats.foldcauchy
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class FoldcauchyScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.foldcauchy distribution.

        Send p -> CDF^-1(p) = scipy.stats.foldcauchy.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.foldcauchy.pdf(t)dt over ]-infty, x]
        """
        name = 'foldcauchy'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.foldcauchy(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.foldcauchy(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.foldcauchy(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(FoldcauchyScale)


#################################################
try:
    scipy.stats.foldnorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class FoldnormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.foldnorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.foldnorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.foldnorm.pdf(t)dt over ]-infty, x]
        """
        name = 'foldnorm'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.foldnorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.foldnorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.foldnorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(FoldnormScale)


#################################################
try:
    scipy.stats.frechet_l
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Frechet_lScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.frechet_l distribution.

        Send p -> CDF^-1(p) = scipy.stats.frechet_l.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.frechet_l.pdf(t)dt over ]-infty, x]
        """
        name = 'frechet_l'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.frechet_l(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.frechet_l(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.frechet_l(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Frechet_lScale)


#################################################
try:
    scipy.stats.frechet_r
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Frechet_rScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.frechet_r distribution.

        Send p -> CDF^-1(p) = scipy.stats.frechet_r.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.frechet_r.pdf(t)dt over ]-infty, x]
        """
        name = 'frechet_r'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.frechet_r(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.frechet_r(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.frechet_r(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Frechet_rScale)


#################################################
try:
    scipy.stats.gamma
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GammaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gamma distribution.

        Send p -> CDF^-1(p) = scipy.stats.gamma.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gamma.pdf(t)dt over ]-infty, x]
        """
        name = 'gamma'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gamma(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gamma(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gamma(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GammaScale)


#################################################
try:
    scipy.stats.gausshyper
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GausshyperScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gausshyper distribution.

        Send p -> CDF^-1(p) = scipy.stats.gausshyper.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gausshyper.pdf(t)dt over ]-infty, x]
        """
        name = 'gausshyper'
        ctor_args = ['a', 'b', 'c', 'z']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gausshyper(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gausshyper(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gausshyper(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GausshyperScale)


#################################################
try:
    scipy.stats.genexpon
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GenexponScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.genexpon distribution.

        Send p -> CDF^-1(p) = scipy.stats.genexpon.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.genexpon.pdf(t)dt over ]-infty, x]
        """
        name = 'genexpon'
        ctor_args = ['a', 'b', 'c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.genexpon(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.genexpon(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.genexpon(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GenexponScale)


#################################################
try:
    scipy.stats.genextreme
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GenextremeScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.genextreme distribution.

        Send p -> CDF^-1(p) = scipy.stats.genextreme.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.genextreme.pdf(t)dt over ]-infty, x]
        """
        name = 'genextreme'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.genextreme(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.genextreme(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.genextreme(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GenextremeScale)


#################################################
try:
    scipy.stats.gengamma
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GengammaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gengamma distribution.

        Send p -> CDF^-1(p) = scipy.stats.gengamma.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gengamma.pdf(t)dt over ]-infty, x]
        """
        name = 'gengamma'
        ctor_args = ['a', 'c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gengamma(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gengamma(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gengamma(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GengammaScale)


#################################################
try:
    scipy.stats.genhalflogistic
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GenhalflogisticScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.genhalflogistic distribution.

        Send p -> CDF^-1(p) = scipy.stats.genhalflogistic.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.genhalflogistic.pdf(t)dt over ]-infty, x]
        """
        name = 'genhalflogistic'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.genhalflogistic(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.genhalflogistic(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.genhalflogistic(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GenhalflogisticScale)


#################################################
try:
    scipy.stats.genlogistic
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GenlogisticScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.genlogistic distribution.

        Send p -> CDF^-1(p) = scipy.stats.genlogistic.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.genlogistic.pdf(t)dt over ]-infty, x]
        """
        name = 'genlogistic'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.genlogistic(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.genlogistic(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.genlogistic(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GenlogisticScale)


#################################################
try:
    scipy.stats.gennorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GennormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gennorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.gennorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gennorm.pdf(t)dt over ]-infty, x]
        """
        name = 'gennorm'
        ctor_args = ['beta']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gennorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gennorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gennorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GennormScale)


#################################################
try:
    scipy.stats.genpareto
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GenparetoScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.genpareto distribution.

        Send p -> CDF^-1(p) = scipy.stats.genpareto.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.genpareto.pdf(t)dt over ]-infty, x]
        """
        name = 'genpareto'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.genpareto(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.genpareto(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.genpareto(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GenparetoScale)


#################################################
try:
    scipy.stats.gilbrat
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GilbratScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gilbrat distribution.

        Send p -> CDF^-1(p) = scipy.stats.gilbrat.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gilbrat.pdf(t)dt over ]-infty, x]
        """
        name = 'gilbrat'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gilbrat(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gilbrat(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gilbrat(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GilbratScale)


#################################################
try:
    scipy.stats.gompertz
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class GompertzScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gompertz distribution.

        Send p -> CDF^-1(p) = scipy.stats.gompertz.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gompertz.pdf(t)dt over ]-infty, x]
        """
        name = 'gompertz'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gompertz(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gompertz(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gompertz(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(GompertzScale)


#################################################
try:
    scipy.stats.gumbel_l
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Gumbel_lScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gumbel_l distribution.

        Send p -> CDF^-1(p) = scipy.stats.gumbel_l.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gumbel_l.pdf(t)dt over ]-infty, x]
        """
        name = 'gumbel_l'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gumbel_l(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gumbel_l(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gumbel_l(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Gumbel_lScale)


#################################################
try:
    scipy.stats.gumbel_r
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Gumbel_rScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.gumbel_r distribution.

        Send p -> CDF^-1(p) = scipy.stats.gumbel_r.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.gumbel_r.pdf(t)dt over ]-infty, x]
        """
        name = 'gumbel_r'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.gumbel_r(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.gumbel_r(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.gumbel_r(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Gumbel_rScale)


#################################################
try:
    scipy.stats.halfcauchy
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class HalfcauchyScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.halfcauchy distribution.

        Send p -> CDF^-1(p) = scipy.stats.halfcauchy.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.halfcauchy.pdf(t)dt over ]-infty, x]
        """
        name = 'halfcauchy'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.halfcauchy(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.halfcauchy(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.halfcauchy(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(HalfcauchyScale)


#################################################
try:
    scipy.stats.halfgennorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class HalfgennormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.halfgennorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.halfgennorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.halfgennorm.pdf(t)dt over ]-infty, x]
        """
        name = 'halfgennorm'
        ctor_args = ['beta']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.halfgennorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.halfgennorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.halfgennorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(HalfgennormScale)


#################################################
try:
    scipy.stats.halflogistic
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class HalflogisticScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.halflogistic distribution.

        Send p -> CDF^-1(p) = scipy.stats.halflogistic.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.halflogistic.pdf(t)dt over ]-infty, x]
        """
        name = 'halflogistic'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.halflogistic(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.halflogistic(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.halflogistic(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(HalflogisticScale)


#################################################
try:
    scipy.stats.halfnorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class HalfnormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.halfnorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.halfnorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.halfnorm.pdf(t)dt over ]-infty, x]
        """
        name = 'halfnorm'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.halfnorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.halfnorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.halfnorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(HalfnormScale)


#################################################
try:
    scipy.stats.hypsecant
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class HypsecantScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.hypsecant distribution.

        Send p -> CDF^-1(p) = scipy.stats.hypsecant.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.hypsecant.pdf(t)dt over ]-infty, x]
        """
        name = 'hypsecant'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.hypsecant(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.hypsecant(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.hypsecant(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(HypsecantScale)


#################################################
try:
    scipy.stats.invgamma
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class InvgammaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.invgamma distribution.

        Send p -> CDF^-1(p) = scipy.stats.invgamma.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.invgamma.pdf(t)dt over ]-infty, x]
        """
        name = 'invgamma'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.invgamma(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.invgamma(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.invgamma(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(InvgammaScale)


#################################################
try:
    scipy.stats.invgauss
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class InvgaussScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.invgauss distribution.

        Send p -> CDF^-1(p) = scipy.stats.invgauss.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.invgauss.pdf(t)dt over ]-infty, x]
        """
        name = 'invgauss'
        ctor_args = ['mu']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.invgauss(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.invgauss(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.invgauss(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(InvgaussScale)


#################################################
try:
    scipy.stats.invweibull
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class InvweibullScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.invweibull distribution.

        Send p -> CDF^-1(p) = scipy.stats.invweibull.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.invweibull.pdf(t)dt over ]-infty, x]
        """
        name = 'invweibull'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.invweibull(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.invweibull(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.invweibull(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(InvweibullScale)


#################################################
try:
    scipy.stats.johnsonsb
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class JohnsonsbScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.johnsonsb distribution.

        Send p -> CDF^-1(p) = scipy.stats.johnsonsb.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.johnsonsb.pdf(t)dt over ]-infty, x]
        """
        name = 'johnsonsb'
        ctor_args = ['a', 'b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.johnsonsb(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.johnsonsb(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.johnsonsb(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(JohnsonsbScale)


#################################################
try:
    scipy.stats.johnsonsu
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class JohnsonsuScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.johnsonsu distribution.

        Send p -> CDF^-1(p) = scipy.stats.johnsonsu.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.johnsonsu.pdf(t)dt over ]-infty, x]
        """
        name = 'johnsonsu'
        ctor_args = ['a', 'b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.johnsonsu(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.johnsonsu(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.johnsonsu(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(JohnsonsuScale)


#################################################
try:
    scipy.stats.kappa3
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Kappa3Scale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.kappa3 distribution.

        Send p -> CDF^-1(p) = scipy.stats.kappa3.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.kappa3.pdf(t)dt over ]-infty, x]
        """
        name = 'kappa3'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.kappa3(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.kappa3(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.kappa3(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Kappa3Scale)


#################################################
try:
    scipy.stats.kappa4
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Kappa4Scale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.kappa4 distribution.

        Send p -> CDF^-1(p) = scipy.stats.kappa4.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.kappa4.pdf(t)dt over ]-infty, x]
        """
        name = 'kappa4'
        ctor_args = ['h', 'k']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.kappa4(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.kappa4(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.kappa4(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Kappa4Scale)


#################################################
try:
    scipy.stats.ksone
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class KsoneScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.ksone distribution.

        Send p -> CDF^-1(p) = scipy.stats.ksone.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.ksone.pdf(t)dt over ]-infty, x]
        """
        name = 'ksone'
        ctor_args = ['n']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.ksone(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.ksone(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.ksone(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(KsoneScale)


#################################################
try:
    scipy.stats.kstwobign
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class KstwobignScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.kstwobign distribution.

        Send p -> CDF^-1(p) = scipy.stats.kstwobign.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.kstwobign.pdf(t)dt over ]-infty, x]
        """
        name = 'kstwobign'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.kstwobign(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.kstwobign(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.kstwobign(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(KstwobignScale)


#################################################
try:
    scipy.stats.laplace
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class LaplaceScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.laplace distribution.

        Send p -> CDF^-1(p) = scipy.stats.laplace.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.laplace.pdf(t)dt over ]-infty, x]
        """
        name = 'laplace'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.laplace(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.laplace(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.laplace(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(LaplaceScale)


#################################################
try:
    scipy.stats.levy
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class LevyScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.levy distribution.

        Send p -> CDF^-1(p) = scipy.stats.levy.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.levy.pdf(t)dt over ]-infty, x]
        """
        name = 'levy'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.levy(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.levy(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.levy(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(LevyScale)


#################################################
try:
    scipy.stats.levy_l
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Levy_lScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.levy_l distribution.

        Send p -> CDF^-1(p) = scipy.stats.levy_l.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.levy_l.pdf(t)dt over ]-infty, x]
        """
        name = 'levy_l'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.levy_l(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.levy_l(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.levy_l(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Levy_lScale)


#################################################
try:
    scipy.stats.loggamma
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class LoggammaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.loggamma distribution.

        Send p -> CDF^-1(p) = scipy.stats.loggamma.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.loggamma.pdf(t)dt over ]-infty, x]
        """
        name = 'loggamma'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.loggamma(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.loggamma(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.loggamma(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(LoggammaScale)


#################################################
try:
    scipy.stats.logistic
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class LogisticScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.logistic distribution.

        Send p -> CDF^-1(p) = scipy.stats.logistic.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.logistic.pdf(t)dt over ]-infty, x]
        """
        name = 'logistic'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.logistic(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.logistic(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.logistic(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(LogisticScale)


#################################################
try:
    scipy.stats.loglaplace
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class LoglaplaceScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.loglaplace distribution.

        Send p -> CDF^-1(p) = scipy.stats.loglaplace.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.loglaplace.pdf(t)dt over ]-infty, x]
        """
        name = 'loglaplace'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.loglaplace(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.loglaplace(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.loglaplace(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(LoglaplaceScale)


#################################################
try:
    scipy.stats.lognorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class LognormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.lognorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.lognorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.lognorm.pdf(t)dt over ]-infty, x]
        """
        name = 'lognorm'
        ctor_args = ['s']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.lognorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.lognorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.lognorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(LognormScale)


#################################################
try:
    scipy.stats.lomax
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class LomaxScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.lomax distribution.

        Send p -> CDF^-1(p) = scipy.stats.lomax.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.lomax.pdf(t)dt over ]-infty, x]
        """
        name = 'lomax'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.lomax(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.lomax(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.lomax(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(LomaxScale)


#################################################
try:
    scipy.stats.maxwell
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class MaxwellScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.maxwell distribution.

        Send p -> CDF^-1(p) = scipy.stats.maxwell.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.maxwell.pdf(t)dt over ]-infty, x]
        """
        name = 'maxwell'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.maxwell(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.maxwell(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.maxwell(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(MaxwellScale)


#################################################
try:
    scipy.stats.mielke
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class MielkeScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.mielke distribution.

        Send p -> CDF^-1(p) = scipy.stats.mielke.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.mielke.pdf(t)dt over ]-infty, x]
        """
        name = 'mielke'
        ctor_args = ['k', 's']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.mielke(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.mielke(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.mielke(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(MielkeScale)


#################################################
try:
    scipy.stats.moyal
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class MoyalScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.moyal distribution.

        Send p -> CDF^-1(p) = scipy.stats.moyal.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.moyal.pdf(t)dt over ]-infty, x]
        """
        name = 'moyal'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.moyal(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.moyal(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.moyal(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(MoyalScale)


#################################################
try:
    scipy.stats.nakagami
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class NakagamiScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.nakagami distribution.

        Send p -> CDF^-1(p) = scipy.stats.nakagami.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.nakagami.pdf(t)dt over ]-infty, x]
        """
        name = 'nakagami'
        ctor_args = ['nu']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.nakagami(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.nakagami(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.nakagami(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(NakagamiScale)


#################################################
try:
    scipy.stats.ncf
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class NcfScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.ncf distribution.

        Send p -> CDF^-1(p) = scipy.stats.ncf.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.ncf.pdf(t)dt over ]-infty, x]
        """
        name = 'ncf'
        ctor_args = ['dfn', 'dfd', 'nc']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.ncf(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.ncf(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.ncf(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(NcfScale)


#################################################
try:
    scipy.stats.nct
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class NctScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.nct distribution.

        Send p -> CDF^-1(p) = scipy.stats.nct.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.nct.pdf(t)dt over ]-infty, x]
        """
        name = 'nct'
        ctor_args = ['df', 'nc']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.nct(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.nct(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.nct(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(NctScale)


#################################################
try:
    scipy.stats.ncx2
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Ncx2Scale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.ncx2 distribution.

        Send p -> CDF^-1(p) = scipy.stats.ncx2.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.ncx2.pdf(t)dt over ]-infty, x]
        """
        name = 'ncx2'
        ctor_args = ['df', 'nc']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.ncx2(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.ncx2(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.ncx2(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Ncx2Scale)


#################################################
try:
    scipy.stats.norm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class NormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.norm distribution.

        Send p -> CDF^-1(p) = scipy.stats.norm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.norm.pdf(t)dt over ]-infty, x]
        """
        name = 'norm'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.norm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.norm(*dist_args, **dist_kwargs)
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

    _record_scale(NormScale)


#################################################
try:
    scipy.stats.norminvgauss
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class NorminvgaussScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.norminvgauss distribution.

        Send p -> CDF^-1(p) = scipy.stats.norminvgauss.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.norminvgauss.pdf(t)dt over ]-infty, x]
        """
        name = 'norminvgauss'
        ctor_args = ['a', 'b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.norminvgauss(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.norminvgauss(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.norminvgauss(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(NorminvgaussScale)


#################################################
try:
    scipy.stats.pareto
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ParetoScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.pareto distribution.

        Send p -> CDF^-1(p) = scipy.stats.pareto.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.pareto.pdf(t)dt over ]-infty, x]
        """
        name = 'pareto'
        ctor_args = ['b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.pareto(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.pareto(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.pareto(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ParetoScale)


#################################################
try:
    scipy.stats.pearson3
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Pearson3Scale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.pearson3 distribution.

        Send p -> CDF^-1(p) = scipy.stats.pearson3.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.pearson3.pdf(t)dt over ]-infty, x]
        """
        name = 'pearson3'
        ctor_args = ['skew']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.pearson3(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.pearson3(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.pearson3(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Pearson3Scale)


#################################################
try:
    scipy.stats.powerlaw
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class PowerlawScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.powerlaw distribution.

        Send p -> CDF^-1(p) = scipy.stats.powerlaw.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.powerlaw.pdf(t)dt over ]-infty, x]
        """
        name = 'powerlaw'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.powerlaw(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.powerlaw(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.powerlaw(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(PowerlawScale)


#################################################
try:
    scipy.stats.powerlognorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class PowerlognormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.powerlognorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.powerlognorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.powerlognorm.pdf(t)dt over ]-infty, x]
        """
        name = 'powerlognorm'
        ctor_args = ['c', 's']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.powerlognorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.powerlognorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.powerlognorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(PowerlognormScale)


#################################################
try:
    scipy.stats.powernorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class PowernormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.powernorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.powernorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.powernorm.pdf(t)dt over ]-infty, x]
        """
        name = 'powernorm'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.powernorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.powernorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.powernorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(PowernormScale)


#################################################
try:
    scipy.stats.rayleigh
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class RayleighScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.rayleigh distribution.

        Send p -> CDF^-1(p) = scipy.stats.rayleigh.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.rayleigh.pdf(t)dt over ]-infty, x]
        """
        name = 'rayleigh'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.rayleigh(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.rayleigh(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.rayleigh(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(RayleighScale)


#################################################
try:
    scipy.stats.rdist
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class RdistScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.rdist distribution.

        Send p -> CDF^-1(p) = scipy.stats.rdist.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.rdist.pdf(t)dt over ]-infty, x]
        """
        name = 'rdist'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.rdist(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.rdist(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.rdist(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(RdistScale)


#################################################
try:
    scipy.stats.recipinvgauss
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class RecipinvgaussScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.recipinvgauss distribution.

        Send p -> CDF^-1(p) = scipy.stats.recipinvgauss.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.recipinvgauss.pdf(t)dt over ]-infty, x]
        """
        name = 'recipinvgauss'
        ctor_args = ['mu']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.recipinvgauss(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.recipinvgauss(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.recipinvgauss(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(RecipinvgaussScale)


#################################################
try:
    scipy.stats.reciprocal
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class ReciprocalScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.reciprocal distribution.

        Send p -> CDF^-1(p) = scipy.stats.reciprocal.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.reciprocal.pdf(t)dt over ]-infty, x]
        """
        name = 'reciprocal'
        ctor_args = ['a', 'b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.reciprocal(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.reciprocal(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.reciprocal(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(ReciprocalScale)


#################################################
try:
    scipy.stats.rice
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class RiceScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.rice distribution.

        Send p -> CDF^-1(p) = scipy.stats.rice.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.rice.pdf(t)dt over ]-infty, x]
        """
        name = 'rice'
        ctor_args = ['b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.rice(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.rice(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.rice(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(RiceScale)


#################################################
try:
    scipy.stats.semicircular
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class SemicircularScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.semicircular distribution.

        Send p -> CDF^-1(p) = scipy.stats.semicircular.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.semicircular.pdf(t)dt over ]-infty, x]
        """
        name = 'semicircular'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.semicircular(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.semicircular(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.semicircular(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(SemicircularScale)


#################################################
try:
    scipy.stats.skewnorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class SkewnormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.skewnorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.skewnorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.skewnorm.pdf(t)dt over ]-infty, x]
        """
        name = 'skewnorm'
        ctor_args = ['a']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.skewnorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.skewnorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.skewnorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(SkewnormScale)


#################################################
try:
    scipy.stats.t
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class TScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.t distribution.

        Send p -> CDF^-1(p) = scipy.stats.t.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.t.pdf(t)dt over ]-infty, x]
        """
        name = 't'
        ctor_args = ['df']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.t(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.t(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.t(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(TScale)


#################################################
try:
    scipy.stats.trapz
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class TrapzScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.trapz distribution.

        Send p -> CDF^-1(p) = scipy.stats.trapz.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.trapz.pdf(t)dt over ]-infty, x]
        """
        name = 'trapz'
        ctor_args = ['c', 'd']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.trapz(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.trapz(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.trapz(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(TrapzScale)


#################################################
try:
    scipy.stats.triang
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class TriangScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.triang distribution.

        Send p -> CDF^-1(p) = scipy.stats.triang.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.triang.pdf(t)dt over ]-infty, x]
        """
        name = 'triang'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.triang(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.triang(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.triang(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(TriangScale)


#################################################
try:
    scipy.stats.truncexpon
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class TruncexponScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.truncexpon distribution.

        Send p -> CDF^-1(p) = scipy.stats.truncexpon.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.truncexpon.pdf(t)dt over ]-infty, x]
        """
        name = 'truncexpon'
        ctor_args = ['b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.truncexpon(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.truncexpon(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.truncexpon(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(TruncexponScale)


#################################################
try:
    scipy.stats.truncnorm
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class TruncnormScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.truncnorm distribution.

        Send p -> CDF^-1(p) = scipy.stats.truncnorm.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.truncnorm.pdf(t)dt over ]-infty, x]
        """
        name = 'truncnorm'
        ctor_args = ['a', 'b']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.truncnorm(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.truncnorm(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.truncnorm(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(TruncnormScale)


#################################################
try:
    scipy.stats.tukeylambda
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class TukeylambdaScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.tukeylambda distribution.

        Send p -> CDF^-1(p) = scipy.stats.tukeylambda.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.tukeylambda.pdf(t)dt over ]-infty, x]
        """
        name = 'tukeylambda'
        ctor_args = ['lam']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.tukeylambda(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.tukeylambda(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.tukeylambda(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(TukeylambdaScale)


#################################################
try:
    scipy.stats.uniform
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class UniformScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.uniform distribution.

        Send p -> CDF^-1(p) = scipy.stats.uniform.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.uniform.pdf(t)dt over ]-infty, x]
        """
        name = 'uniform'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.uniform(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.uniform(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.uniform(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(UniformScale)


#################################################
try:
    scipy.stats.vonmises
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class VonmisesScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.vonmises distribution.

        Send p -> CDF^-1(p) = scipy.stats.vonmises.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.vonmises.pdf(t)dt over ]-infty, x]
        """
        name = 'vonmises'
        ctor_args = ['kappa']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.vonmises(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.vonmises(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.vonmises(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(VonmisesScale)


#################################################
try:
    scipy.stats.vonmises_line
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Vonmises_lineScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.vonmises_line distribution.

        Send p -> CDF^-1(p) = scipy.stats.vonmises_line.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.vonmises_line.pdf(t)dt over ]-infty, x]
        """
        name = 'vonmises_line'
        ctor_args = ['kappa']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.vonmises_line(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.vonmises_line(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.vonmises_line(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Vonmises_lineScale)


#################################################
try:
    scipy.stats.wald
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class WaldScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.wald distribution.

        Send p -> CDF^-1(p) = scipy.stats.wald.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.wald.pdf(t)dt over ]-infty, x]
        """
        name = 'wald'
        ctor_args = []

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.wald(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.wald(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.wald(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(WaldScale)


#################################################
try:
    scipy.stats.weibull_max
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Weibull_maxScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.weibull_max distribution.

        Send p -> CDF^-1(p) = scipy.stats.weibull_max.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.weibull_max.pdf(t)dt over ]-infty, x]
        """
        name = 'weibull_max'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.weibull_max(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.weibull_max(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.weibull_max(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Weibull_maxScale)


#################################################
try:
    scipy.stats.weibull_min
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class Weibull_minScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.weibull_min distribution.

        Send p -> CDF^-1(p) = scipy.stats.weibull_min.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.weibull_min.pdf(t)dt over ]-infty, x]
        """
        name = 'weibull_min'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.weibull_min(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.weibull_min(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.weibull_min(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(Weibull_minScale)


#################################################
try:
    scipy.stats.wrapcauchy
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class WrapcauchyScale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.wrapcauchy distribution.

        Send p -> CDF^-1(p) = scipy.stats.wrapcauchy.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.wrapcauchy.pdf(t)dt over ]-infty, x]
        """
        name = 'wrapcauchy'
        ctor_args = ['c']

        def __init__(self, axis, dist_args=None, dist_kwargs=None, nonpos='mask', percentage=False):
            """
            *axis*:
              unused, compatibility with ProbabilityScale
            *dist_args*:
              passed to constructor of scipy.stats.wrapcauchy(*dist_args, **dist_kwargs)
            *dist_kwargs*:
              passed to constructor of scipy.stats.wrapcauchy(*dist_args, **dist_kwargs)
            *nonpos*: ['mask' | 'clip' ]
              values beyond ]0, 1[ can be masked as invalid, or clipped to a number
              very close to 0 or 1
            *percentage*: [True | False]
              Display probability values as percentages
            """
            args = dist_args or []
            kwargs = dist_kwargs or {}
            dist = scipy.stats.wrapcauchy(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)

    _record_scale(WrapcauchyScale)


from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import inspect

import scipy.stats


def _getargspec(meth):
    """Similar functionality as scipy._lib._util.getargspec_no_self, but implementing here
    avoids PEP8 warnings on the access of protected members of classes."""
    try:
        # Python3's inspect has getfullargspec(), and has deprecated getargspec()
        # but getfullargspec() returns a named tuple with one different name 'keywords' -> 'varkw'
        fullargspec = inspect.getfullargspec(meth)
    except AttributeError:
        # noinspection PyDeprecation
        argspec = inspect.getargspec(meth)
    else:
        argspec = inspect.ArgSpec(*fullargspec[:4])
    # Drop the 'self' argument
    if argspec.args[0] == 'self':
        argspec.args.pop(0)
    return argspec


# Original list extracted from https://docs.scipy.org/doc/scipy-0.19.0/reference/tutorial/stats/continuous.html
# E.g. "Alpha Distribution" links to
# https://docs.scipy.org/doc/scipy-0.19.0/reference/tutorial/stats/continuous_alpha.html

_dists = list(filter(None, '''
alpha anglit arcsine argus
beta betaprime bradford burr burr12
cauchy chi chi2 cosine
dgamma dweibull
erlang expon exponnorm exponpow exponweib
f fatiguelife fisk foldcauchy foldnorm frechet_l frechet_r
gamma gausshyper genexpon genextreme gengamma genhalflogistic 
genlogistic gennorm genpareto gilbrat gompertz gumbel_l gumbel_r
halfcauchy halfgennorm halflogistic halfnorm hypsecant
invgamma invgauss invweibull
johnsonsb johnsonsu
kappa3 kappa4 ksone kstwobign
laplace levy levy_l loggamma logistic loglaplace lognorm lomax
maxwell mielke
nakagami ncf nct ncx2 norm
pareto pearson3 powerlaw powerlognorm powernorm
rayleigh rdist recipinvgauss reciprocal rice
semicircular skewnorm
t trapz triang truncexpon truncnorm tukeylambda
uniform
vonmises vonmises_line
wald weibull_max weibull_min wrapcauchy
'''.split()))

# noinspection PyProtectedMember
_dists_from_scipystats = list(sorted(
    [k for k in scipy.stats._continuous_distns.__all__ if not (
        (k.startswith('rv_') or k.endswith('_gen') or (k == 'levy_stable')))]))
# levy_stable only generate random deviates, it doesn't have a PDF or CDF

_TOP_TEMPLATE = '''
from __future__ import (absolute_import, division, print_function, unicode_literals)

import scipy.stats
from matplotlib.scale import register_scale

from .transforms import ProbabilityTransform
from .scales import ProbabilityScale

_PREFIX = {prefix!r}


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

'''

_SCALE_TEMPLATE = '''
#################################################
try:
    scipy.stats.{dist}
except AttributeError:
    pass
else:
    # Some distributions have '_' in their names, breaking CamelCase convention
    # noinspection PyPep8Naming
    class {dist_class_name}Scale(ProbabilityScale):
        """
        Probability scale for data between zero and one using scipy.stats.{dist} distribution.

        Send p -> CDF^-1(p) = scipy.stats.{dist}.ppf(p)
        I.e. f(p) == x  <==>  p ==  Integral scipy.stats.{dist}.pdf(t)dt over ]-infty, x]
        """
        name = '{prefix}{dist}'
        ctor_args = {ctor_args!r}

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
            kwargs = dist_kwargs or {{}}
            dist = scipy.stats.{dist}(*args, **kwargs)
            ProbabilityScale.__init__(self, axis, dist, nonpos=nonpos, percentage=percentage)
            # self._transform = ProbabilityTransform(dist, nonpos)

    _record_scale({dist_class_name}Scale)

'''


def _get_shapes(dst):
    """Perform some trickery to discern the arguments necessary to create the frozen probability distribution"""
    # The distribution has a shapes member but it appears to be often None
    # Similarly for the 'shapes' key in the _ctor_param dictionary
    # Look instead at the _pdf and _cdf methods
    # noinspection PyProtectedMember
    ctr_dct = dst._ctor_param
    shapes = ctr_dct.get('shapes')
    if shapes is None:
        # Based on scipy's rv_continuous._construct_argparser()
        # noinspection PyProtectedMember,PyProtectedMember
        meths_to_inspect = dst._pdf, dst._cdf
        shapes_list = []

        for meth in meths_to_inspect:
            shapes_args = _getargspec(meth)  # NB: does not contain self
            args = shapes_args.args[1:]  # peel off 'x', too
            # print(dst.name, shapes_args)

            if args:
                shapes_list.append(args)
                # *args or **kwargs are not allowed w/automatic shapes
                if shapes_args.varargs is not None:
                    raise TypeError(
                        '*args are not allowed w/out explicit shapes')
                if shapes_args.keywords is not None:
                    raise TypeError(
                        '**kwds are not allowed w/out explicit shapes')
                if shapes_args.defaults is not None:
                    raise TypeError('defaults are not allowed for shapes')

        if shapes_list:
            shapes = shapes_list[0]
            # make sure the signatures are consistent
            for item in shapes_list:
                if item != shapes:
                    raise TypeError('Shape arguments are inconsistent.')
        else:
            shapes = []

    return shapes


def generate_source(prefix=None):
    if prefix is None:
        prefix = ''
    s = _TOP_TEMPLATE.format(prefix=prefix)
    undoc = sorted(set(_dists_from_scipystats) - set(_dists))
    if undoc:
        print('WARNING: There are {:d} continuous distributions in scipy.stats '
              'which are undocumented {!r}'.format(len(undoc), undoc))
        print()
    # http://scipy.github.io/devdocs/tutorial/stats/continuous.html#continuous-random-variables
    # undoc = sorted(set(_dists_from_scipystats) - set(_dists_dev))

    for dist in _dists_from_scipystats:  # was _dists
        dist_cap = dist[0].upper() + dist[1:]
        dst = getattr(scipy.stats, dist)
        shapes = _get_shapes(dst)
        # noinspection PyProtectedMember
        ctr_dct = dst._ctor_param
        if 0:
            # Record some default arguments which can be used later on in testing
            # Grab arguments from the distribution's _ctor_param dictionary.
            # FAILURE:
            # 1. Some use a,b parameters for the arguments, the min and max x-values.
            # But some distributions use c,d for other shapes.  Still others require 'lam'.
            # 2. The dst._ctor_param dict is not reliable.  It doesn't agree with dst.numargs (E.g. burr, truncnorm,...)
            # 3. The dst._ctor_param dict is not reliable.  It doesn't have all needed keywords (E.g. tukeylambda)
            ctor_args = tuple(filter(lambda _: _ is not None, map(ctr_dct.get, ['a', 'b'])))
            # print(ctrDct)
            # print(dst.numargs, ctorArgs)
        else:
            # print(dist, dst.numargs, "shapes=", ctr_dct.get('shapes'), shapes)
            print('{} numargs={} shapes={}'.format(dist, dst.numargs, shapes))
            # ctorArgs = ', '.join(shapes) if shapes else ''  # NB: not None
            ctor_args = shapes
        s += _SCALE_TEMPLATE.format(dist=dist, dist_class_name=dist_cap, prefix=prefix, ctor_args=ctor_args)
    return s


def create_probscales(fn, prefix=None):
    s = generate_source(prefix=prefix)
    with open(fn, 'wt') as f:
        f.write(s)


def parse_args():
    parser = argparse.ArgumentParser(
        prog='gen_probscales',
        description="Generate the py file of Matplotlib scales from scipy's continuous distributions")

    parser.add_argument('--out', help='name of generated output python file', default='scipyscales.py')
    parser.add_argument('--prefix', help='prefix for the scale name.  "scipy.stats.normal" ->"<prefix>normal"',
                        default=None)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main_args = parse_args()
    create_probscales(main_args.out, prefix=main_args.prefix)

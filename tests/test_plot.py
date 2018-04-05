# -*- coding: utf-8 -*-

import sys
import os.path
import unittest
import inspect
import logging

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

try:
    from .context import probscales
except Exception as e:
    import probscales

TEST_OUTPUT_DIR = 'test_out'
_probscalesfile = probscales.__file__
if _probscalesfile and os.path.dirname(_probscalesfile):
    _topdir = os.path.dirname(os.path.dirname(_probscalesfile))
    if _topdir:
        TEST_OUTPUT_DIR = os.path.join(_topdir, TEST_OUTPUT_DIR)
    del _topdir
del _probscalesfile


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
    # Drop the 'self' argument from 'args'
    if argspec.args[0] == 'self':
        argspec.args.pop(0)
    return argspec


def _get_shapes(dst):
    # noinspection PyProtectedMember
    ctr_dct = dst._ctor_param
    shapes = ctr_dct.get('shapes')
    if shapes is None:
        # Based on scipy's rv_continuous._construct_argparser()
        # noinspection PyProtectedMember
        meths_to_inspect = [dst._pdf, dst._cdf]
        shapes_list = []

        for meth in meths_to_inspect:
            shapes_args = _getargspec(meth)  # NB: does not contain self
            args = shapes_args.args[1:]  # peel off 'x', too

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
            for item in shapes_list[1:]:
                if item != shapes:
                    raise TypeError('Shape arguments are inconsistent.')
        else:
            shapes = []

    return shapes


_defaultCtrArgs = {
    'alpha': [1],
    'beta': [0.2, 0.8],
    'betaprime': [0.2, 0.8],
    'bradford': [1],
    'burr': [1, 2],
    'burr12': [1, 2],
    # 'chi': [4],
    # 'f': [29, 18],
    'f': [12, 8],
    # 'fisk': [1],
    'ksone': [1e3],
    'trapz': [0.2, 0.8],
    'triang': [0.2],
    'wrapcauchy': [0.2],
}


def _get_dist_args(dst, scalename):
    shapes = _get_shapes(dst)
    dist_args = _defaultCtrArgs.get(scalename, None)
    if dist_args is None:
        if shapes == ['df']:
            dist_args = [4]  # degrees of freedom for chi, chi2, ...
        elif shapes == ['dfn', 'dfd']:
            dist_args = [12, 8]  # f distribution
        elif shapes == ['h', 'k']:
            dist_args = [1.0, 2.0]  # kappa4 needs float, not integers
            pass

    if dist_args is None:
        dist_args = list(range(1, len(shapes) + 1, 1))

    return dist_args


def plot_one_scale(scalename, scale_prefix='', outfn=None, separate_pdf_axis=True):
    logger = logging.getLogger(__name__)
    if scalename == 'runTest':
        # May happen if yielding classes for testing
        return

    u0, u1 = 0, 1
    threshvals = np.arange(-80, 81, 1) / 20.0  # +/- 4 std deviations
    threshvals = np.arange(-60, 61, 1) / 20.0  # +/- 3 std deviations
    xvals = scipy.stats.norm.sf(threshvals)
    yvals = scipy.stats.norm.cdf(threshvals - u1)

    dist_args = ()
    if scalename == 'linear':
        dst = scipy.stats.uniform(0, 1)
    elif scalename == 'probit':
        dst = scipy.stats.norm()
    else:
        sc2 = scalename
        if scale_prefix and sc2.startswith(scale_prefix):
            sc2 = sc2[len(scale_prefix):]
        try:
            dstattr = getattr(scipy.stats, sc2)
        except AttributeError as e:
            if 0:
                print(e)
            raise
        except Exception as e:
            if 0:
                print(e)
            raise
        else:
            dist_args = _get_dist_args(dstattr, sc2)
            try:
                # noinspection PyArgumentList
                dst = dstattr(*dist_args)
            except Exception as e:
                if 0:
                    import traceback
                    traceback.print_exc()
                raise
    minp = (0 if np.isfinite(dst.a) else 0.001)
    maxp = (1 if np.isfinite(dst.b) else 1-0.001)

    # RED_FLAG Scales appear to need to extend beyond [0, 1]...
    minp, maxp = 0.01, 1.0 - 0.01

    # Use linearly spacing on the x-axis for plotting? Or linear spacing on the CDF prob?
    # Linear spacing on the x-axis makes for better plots...
    linspaced_probs = np.linspace(minp, maxp, num=101, endpoint=True)
    xx_plinspaced = dst.ppf(linspaced_probs)
    minx, maxx = xx_plinspaced[0], xx_plinspaced[-1]
    xx_linspaced = np.linspace(minx, maxx, num=101, endpoint=True)

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=[16, 8], squeeze=True)
    ax0 = axs[0]
    plt.sca(ax0)
    if 0:
        xxs = xx_plinspaced
        yys = linspaced_probs
    else:
        xxs = xx_linspaced
        yys = dst.cdf(xx_linspaced)
    ax0.plot(xxs, yys, '-', lw=1, label='CDF')
    ax0.set_ylabel('CDF', color='C0')
    ax0.set_xlabel('x')
    ax0.set_ylim([0, 1])
    ax0.tick_params('y', colors='C0')

    xlim = [xxs[0], xxs[-1]]
    ax0.set_xlim(xlim)
    ax0.grid(which='major', axis='both')

    if separate_pdf_axis:
        ax2 = ax0.twinx()
        pdfs = dst.pdf(xxs)
        # While the CDFs may be well-behaved at the endpoints, the PDFs may not be...
        # f, gumbel_r, rdist, recipinvgauss
        if not np.isfinite(pdfs[0]):
            logger.warning('Dropping infinite left {} for scale {}'.format(xxs[0], scalename))
            xxs = xxs[1:]
            pdfs = pdfs[1:]
        if not np.isfinite(pdfs[-1]):
            logger.warning('Dropping infinite right {} for scale {}'.format(xxs[-1], scalename))
            xxs = xxs[:-1]
            pdfs = pdfs[:-1]
        if 0 and pdfs[-1] > 10 * pdfs[-2]:
            logger.warning('Dropping large right {}>{} for scale {}'.format(pdfs[-1], pdfs[-2], scalename))
            xxs = xxs[:-1]
            pdfs = pdfs[:-1]
        if 0 and pdfs[0] > 10 * pdfs[1]:
            logger.warning('Dropping large left {}>{} for scale {}'.format(pdfs[0], pdfs[1], scalename))
            xxs = xxs[1:]
            pdfs = pdfs[1:]
        ax2.plot(xxs, pdfs, 'C1o-', markersize=1, label='PDF', lw=1)
        ax2.set_ylabel('PDF', color='C1')
        ax2.tick_params('y', colors='C1')
        ax2.set_ylim([0, ax2.get_ylim()[1]])
        ax2.set_xlim(xlim)
        # Plot one point on ax0 to get a legend entry
        # ax0.plot(xxs[0], yys[0], 'C1o-', markersize=1, label='PDF', lw=1)
        ax0.plot(-100, -100, 'C1o-', markersize=1, label='PDF', lw=1)
    else:
        ax0.plot(xxs, dst.pdf(xxs), '-', markersize=1, label='PDF', lw=1)
    ax0.legend()

    plt.title('Scale={}'.format(scalename))

    ax1 = axs[1]
    plt.sca(ax1)
    ax1.plot(xvals, yvals, 'bo', linestyle='-', markersize=2, lw=1, label='u1-u0=1')
    yys = 1 - linspaced_probs
    ax1.plot(linspaced_probs, yys, 'r+', linestyle='-', lw=1, markersize=2, label='random')
    ax1.set_title('FA-FR curve, scale={}'.format(scalename))
    ax1.set_xlabel('False Alarm Probability (in %)')
    ax1.set_ylabel('False Reject Probability')
    ax1.set_xlim([0.001, 1-0.001])
    ax1.set_ylim([0.001, 1-0.001])
    ax1.set_xscale(scalename, dist_args=dist_args, percentage=True)
    ax1.set_yscale(scalename, dist_args=dist_args, percentage=False)
    ax1.grid(b=True, axis='y', which='minor', color='grey', linestyle='-.')
    ax1.grid(b=True, axis='x', which='major', color='grey', linestyle='-.')
    ax1.legend()

    # Check that the transform is doing what is expected
    if scalename not in ['linear']:
        # 'linear' scale has no transform
        ax = plt.gca()
        ax = ax1
        # noinspection PyProtectedMember
        mplscale = ax.xaxis._scale
        # noinspection PyProtectedMember
        mpltransform = mplscale._transform
        txvals = np.array(mpltransform.transform(xvals))
        xvals_ppf = dst.ppf(xvals)
        assert np.allclose(txvals, xvals_ppf)

        # noinspection PyProtectedMember
        mplscale = ax.yaxis._scale
        # noinspection PyProtectedMember
        mpltransform = mplscale._transform
        yvals_ppf = dst.ppf(yvals)
        tyvals = np.array(mpltransform.transform(yvals))
        assert np.allclose(tyvals, yvals_ppf)

    if outfn:
        plt.savefig(outfn)
    plt.close(fig)
    # if scalename == 'beta':
    #     raise Exception('Bail early')


class PlotTestSuite(unittest.TestCase):
    """plot test cases."""

    @staticmethod
    def test_scales(outdir=TEST_OUTPUT_DIR):
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        scale_prefix = probscales.get_scale_prefix()
        scale_names = probscales.get_scale_names()
        print(scale_names)
        nTested = 0
        for sc in ['linear', 'probit']:
            fn = os.path.join(outdir, sc + '.png')
            plot_one_scale(sc, outfn=fn)
            nTested += 1
        for name in scale_names:
            fn = os.path.join(outdir, name + '.png')
            print('Scale: %s' % name)
            plot_one_scale(name, scale_prefix=scale_prefix, outfn=fn)
            nTested += 1
        print('nTested={}'.format(nTested))


if __name__ == '__main__':
    unittest.main()

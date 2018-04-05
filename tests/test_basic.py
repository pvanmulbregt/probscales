# -*- coding: utf-8 -*-

from .context import probscales

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @staticmethod
    def test_names():
        scale_prefix = probscales.get_scale_prefix()
        scale_names = probscales.get_scale_names()
        if scale_prefix:
            name_starts_ok = [sc.startswith(scale_prefix) for sc in scale_names]
            assert all(name_starts_ok)


if __name__ == '__main__':
    unittest.main()

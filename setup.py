from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='probscales',
      version='1.0a1',
      description='Probability scales for matplotlib',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization',
      ],
      keywords='matplotlib scale probability',
      url='http://github.com/p.vanmulbregt/probscales',
      author='Paul van Mulbregt',
      author_email='paulpy@vanmulbregt.net',
      license='MIT',
      packages=['probscales'],
      install_requires=[
          'numpy',
          'matplotlib',
          'scipy'
      ],
      # test_suite='nose.collector',
      # tests_require=['nose', 'nose-cover3'],
      # tests_require=['pytest'],
      # cmdclass = {'test': PyTest},
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      entry_points={},
      include_package_data=True,
      zip_safe=True)

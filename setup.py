from setuptools import setup

setup(name='biomarker_survival',
      version='0.1',
      description='Utilities for performing biomarker survival analyses',
      url='http://github.com/joansmith/biomarker-survival',
      author='Joan Smith',
      author_email='joans@alum.mit.edu',
      license='MIT',
      packages=['biomarker_survival'],
      zip_safe=False,
      install_requires=[
        'matplotlib',
        'numpy',
        'scipy',
        'rpy2',
        'pandas'])

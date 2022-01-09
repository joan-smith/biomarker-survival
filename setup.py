from setuptools import setup, find_packages


# note: tzlocal is an rpy2 dependency that's left out of the rpy2 spec.
setup(name='biomarker_survival',
      version='0.2.4',
      description='Utilities for performing biomarker survival analyses',
      url='http://github.com/joansmith/biomarker-survival',
      author='Joan Smith',
      author_email='joans@alum.mit.edu',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      setup_requires=['pytest-runner'],
      install_requires=[
        'pandas>=0.25.1',
        'rpy2==3.4.5',
        'matplotlib',
        'scipy>=1.3.1',
        'tzlocal',
        'openpyxl'],
      tests_require=['pytest', 'pytest-datafiles'])


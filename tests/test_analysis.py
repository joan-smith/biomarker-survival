import os
import numpy as np
import rpy2

from biomarker_survival import analysis

def test_do_cox_success():
  time = [48, 79, 9, 60, 81, 0, 64, 5, 26, 39, 83, 55, 33, 20, 29, 38, 47, 49, 96, 50, 84, 45, 84, 43,
           4, 87, 27, 15, 24, 34, 46, 43, 53, 41, 86, 69, 79, 25, 6, 65, 71, 52, 43, 18, 32, 7, 47, 57,
           7, 45]
  censor = [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
              1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1]
  split  = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0,
             1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]

  cox_dict = analysis.do_cox(time, censor, split)
  print(cox_dict)
  assert cox_dict['n'] == 50
  assert cox_dict['p'] < 1
  assert list(cox_dict.keys()).sort() == ['n', 'z', 'p', 'hazard_ratio', 'lower_conf', 'upper_conf'].sort()

def test_do_cox_fail():
  time = np.random.randint(0,1, 5)
  censor = np.random.randint(0,1, 5)
  split = np.random.randint(0,1, 5)

  cox_dict = analysis.do_cox(time, censor, split)
  if len(list(cox_dict.keys())) == 0:
    assert list(cox_dict.keys()) == []
  else:
    assert np.isnan(cox_dict['p'])
    assert list(cox_dict.keys()).sort() == ['n', 'z', 'p', 'hazard_ratio', 'lower_conf', 'upper_conf'].sort()


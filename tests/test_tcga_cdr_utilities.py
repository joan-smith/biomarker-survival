import os
import pytest

from biomarker_survival import TCGA_CDR_util

FIXTURE_DIR = os.path.join(
   os.path.dirname(os.path.realpath(__file__)),
   'test_data',
  )
@pytest.fixture(scope="module")
def tcga_cdr():
  path = os.path.join(FIXTURE_DIR, 'TCGA-CDR-SupplementalTableS1-2019-05-27.xlsx')
  return TCGA_CDR_util(path)

def test_read_table(tcga_cdr):
  assert tcga_cdr.df.shape == (11103, 33)
  assert list(tcga_cdr.df.index)[0] == 'TCGA-OR-A5J1'

testdata = [
  ['ACC', '', [92, 34, 58]],
  ['BLCA', '',  [408, 178, 230]],
  ['BRCA', '', [1091, 145, 946]],
  ['CESC', '', [307, 71, 236]],
  ['CHOL', '', [45, 22, 23]],
  ['COAD', '', [457, 102, 355]],
  ['DLBC', '', [48, 12, 36]],
  ['ESCA', '', [185, 77, 108]],
  ['GBM', '', [595, 490, 105]],
  ['HNSC', '', [527, 223, 304]],
  ['KICH', '', [112, 12, 100]],
  ['KIRC', '', [537, 177, 360]],
  ['KIRP', '', [290, 44, 246]],
  ['LAML', '', [186, 120, 66]],
  ['LGG', '', [514, 192, 322]],
  ['LIHC', '', [375, 131, 244]],
  ['LUAD', '', [513, 184, 329]],
  ['LUSC', '', [498, 215, 283]],
  ['MESO', '', [86, 73, 13]],
  ['OV', '', [538, 322, 216]],
  ['PAAD', '', [185, 100, 85]],
  ['PCPG', '', [179, 21, 158]],
  ['PRAD', '', [500, 93, 407]],
  ['READ', '', [170, 39, 131]],
  ['SARC', '', [261, 99, 162]],
  ['SKCM', '', [455, 214, 241]],
  ['STAD', '', [437, 169, 268]],
  ['TGCT', '', [134, 35, 99]],
  ['THCA', '', [507, 52, 455]],
  ['THYM', '', [123, 22, 101]],
  ['UCEC', '', [546, 91, 455]],
  ['UCS', '', [57, 35, 22]],
  ['UVM', '', [80, 23, 57]]
]

@pytest.mark.parametrize("a,b,expected", testdata, ids=[i[0] for i in testdata])
def test_cancer_type_patients(a, b, expected, tcga_cdr):
  ctype, _ = a, b
  ctype_df  = tcga_cdr.cancer_type_data(a)
  patients, event, censored = expected
  assert ctype_df.shape == (patients, 2)

@pytest.mark.parametrize("a,b,expected", testdata, ids=[i[0] for i in testdata])
def test_cancer_type_event(a, b, expected, tcga_cdr):
  ctype, _ = a, b
  ctype_df  = tcga_cdr.cancer_type_data(a)
  patients, event, censored = expected
  assert ctype_df['censor'].sum() == event

@pytest.mark.parametrize("a,b,expected", testdata, ids=[i[0] for i in testdata])
def test_cancer_type_censored(a, b, expected, tcga_cdr):
  ctype, _ = a, b
  ctype_df  = tcga_cdr.cancer_type_data(a)
  patients, event, censored = expected
  assert (ctype_df['censor'] == 0).sum() == censored


def test_extra_cols(tcga_cdr):
  df = tcga_cdr.cancer_type_data('BLCA',
                extra_cols=['ajcc_pathologic_tumor_stage',  'histological_grade'])
  assert df.shape == (408, 4)
  assert list(df.columns) == ['censor', 'time',
                        'ajcc_pathologic_tumor_stage', 'histological_grade']

def test_all_cancers(tcga_cdr):
  df = tcga_cdr.cancer_type_data('*')
  assert df.shape == (11038, 3)
  assert list(df.columns) == ['type', 'censor', 'time']

def test_all_cancers_extra_cols(tcga_cdr):
  df = tcga_cdr.cancer_type_data('*', extra_cols=['histological_grade'])
  assert df.shape == (11038, 4)
  assert list(df.columns) == ['type', 'censor', 'time', 'histological_grade']

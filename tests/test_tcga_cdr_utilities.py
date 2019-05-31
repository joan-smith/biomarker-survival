import os
import pytest

from biomarker_survival import TCGA_CDR_util

FIXTURE_DIR = os.path.join(
   os.path.dirname(os.path.realpath(__file__)),
   'test_data',
  )
@pytest.fixture(scope="module")
# @pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'TCGA-CDR-SupplementalTableS1-2019-05-27.xlsx'))
def tcga_cdr():
  path = os.path.join(FIXTURE_DIR, 'TCGA-CDR-SupplementalTableS1-2019-05-27.xlsx')
  return TCGA_CDR_util(path)

# @pytest.mark.datafiles(os.path.join(FIXTURE_DIR, 'TCGA-CDR-SupplementalTableS1-2019-05-27.xlsx'))
def test_read_table(tcga_cdr):
  assert tcga_cdr.df.shape == (11103, 33)

testdata = [
  ['ACC', '', [92, 34, 58]],
  ['BLCA', '',  [409, 179, 230]],
  ['BRCA', '', [1092, 145, 947]],
  ['CESC', '', [307, 71, 236]],
  ['CHOL', '', [45, 22, 23]],
  ['COAD', '', [458, 102, 356]],
  ['DLBC', '', [48, 12, 36]],
  ['ESCA', '', [185, 77, 108]],
  ['GBM', '', [595, 490, 105]],
  ['HNSC', '', [528, 223, 305]],
  ['KICH', '', [113, 13, 100]],
  ['KIRC', '', [537, 177, 360]],
  ['KIRP', '', [291, 44, 247]],
  ['LAML', '', [200, 133, 67]],
  ['LGG', '', [515, 192, 323]],
  ['LIHC', '', [376, 131, 245]],
  ['LUAD', '', [522, 188, 334]],
  ['LUSC', '', [504, 219, 285]],
  ['MESO', '', [87, 74, 13]],
  ['OV', '', [542, 322, 218]],
  ['PAAD', '', [185, 100, 85]],
  ['PCPG', '', [179, 21, 158]],
  ['PRAD', '', [500, 93, 407]],
  ['READ', '', [170, 39, 131]],
  ['SARC', '', [261, 99, 162]],
  ['SKCM', '', [470, 216, 247]],
  ['STAD', '', [443, 172, 271]],
  ['TGCT', '', [134, 35, 99]],
  ['THCA', '', [507, 52, 455]],
  ['THYM', '', [124, 22, 102]],
  ['UCEC', '', [547, 91, 456]],
  ['UCS', '', [57, 35, 22]],
  ['UVM', '', [80, 23, 57]]
]

@pytest.mark.parametrize("a,b,expected", testdata, ids=[i[0] for i in testdata])
def test_cancer_type_data(a, b, expected, tcga_cdr):
  ctype, _ = a, b
  ctype_df  = tcga_cdr.cancer_type_data(a)
  patients, event, censored = expected
  assert ctype_df.shape == (patients, 2)
  assert ctype_df['censor'].sum() == event
  assert (ctype_df['censor'] == 0).sum() == censored


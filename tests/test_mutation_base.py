import os
import pytest
from biomarker_survival import mutation_base
from biomarker_survival import TCGA_CDR_util

FIXTURE_DIR = os.path.join(
   os.path.dirname(os.path.realpath(__file__)),
   'test_data',
  )

@pytest.fixture(scope="module")
def tcga_cdr():
  path = os.path.join(FIXTURE_DIR, 'TCGA-CDR-SupplementalTableS1-2019-05-27.xlsx')
  return TCGA_CDR_util(path)

def test_prep_mutation_data_alone(tcga_cdr):
  path = os.path.join(FIXTURE_DIR, 'mutations-first-thousand-lines-2019-05-19.txt')

  muts = mutation_base.prep_mutation_data_alone(path)
  patient_genes = mutation_base.prep_mutation_data(muts, tcga_cdr.cancer_type_data('*'), 'GBM')
  assert list(patient_genes.index)[0] == 'TCGA-02-0003'
  assert patient_genes.columns[0] == '\'ABR'
  assert patient_genes.values.max() == 1
  assert patient_genes.values.min() == 0



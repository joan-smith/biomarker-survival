import os
import pytest

from biomarker_survival import pancan

FIXTURE_DIR = os.path.join(
   os.path.dirname(os.path.realpath(__file__)),
   'test_data',
  )

@pytest.fixture(scope="module")
def cancer_type_dir():
  path = os.path.join(FIXTURE_DIR, 'pancan')
  return path

def test_pancan(cancer_type_dir):
  pancan_df = pancan(cancer_type_dir)

  print pancan_df.columns
  assert pancan_df.shape == (11825, 12)
  assert 'stouffer unweighted' in list(pancan_df.columns)
  assert 'ACC' in list(pancan_df.columns)
  assert pancan_df['ACC'].count() == 1708

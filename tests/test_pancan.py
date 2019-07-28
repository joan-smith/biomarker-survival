import os
import pytest

from biomarker_survival import pancan

FIXTURE_DIR = os.path.join(
   os.path.dirname(os.path.realpath(__file__)),
   'test_data',
  )

@pytest.fixture(scope="module")
def pancan_data():
  path = os.path.join(FIXTURE_DIR, 'pancan')
  return path

def test_pancan_mutations(pancan_data):
  pancan_df = pancan(os.path.join(pancan_data, 'pancan_mutations'))

  assert pancan_df.shape == (11825, 12)
  assert 'stouffer unweighted' in list(pancan_df.columns)
  assert 'ACC' in list(pancan_df.columns)
  assert pancan_df['ACC'].count() == 1708


def test_pancan_rnaseq(pancan_data):
  pancan_df = pancan(os.path.join(pancan_data, 'pancan_rnaseq'))

  assert pancan_df.shape == (20531, 10)
  assert 'stouffer unweighted' in list(pancan_df.columns)
  assert 'ACC' in list(pancan_df.columns)
  assert pancan_df['ACC'].count() == 19800

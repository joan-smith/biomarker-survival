import pandas as pd
import numpy as np
import sys
import os
import re

from . import analysis


def pancan(cancer_types_dir, multivariate=False):
  files = os.listdir(cancer_types_dir)
  ctype = re.compile('([A-Z]+).*.zscores.out.csv')

  z_name = 'z'
  if multivariate:
    z_name = 'var-z'

  pancan_dict = {}
  for f in files:
    cancer_type_match = re.match(ctype, f)
    if not cancer_type_match:
      continue
    cancer_type = cancer_type_match.group(1)

    # sometimes rpy2 gives back this monstrosity of a NaN value.
    df = pd.read_csv(os.path.join(cancer_types_dir, f), index_col=0, na_values=[' NA'])
    if df.shape[0] > 0:
      if '\'' not in df.index[0]:
        # ADD ' to index
        df.reset_index(inplace=True)
        df['gene'] = '\'' + df['gene']
        df.set_index('gene', inplace=True)
      if z_name in df:
        pancan_dict[cancer_type] = df[z_name].astype(float)

  pancan_df = pd.DataFrame(pancan_dict)
  pancan_df = pancan_df.reindex(sorted(pancan_df.columns), axis=1)
  pancan_df['stouffer unweighted'] = analysis.stouffer_unweighted(pancan_df)
  return pancan_df


import pandas as pd
import numpy as np
import sys
import os

class TCGA_CDR_util:
  # Cancer types with OS recommended are excluded for brevity.
  # OS is the default.
  RECOMMENDED_ENDPOINTS = {
    'BRCA': 'PFI',  # alternative: DFI
    'DLBC': 'PFI',  # none rec w/o reservation
    'KICH': 'OS',   # none rec w/o reservation
    'LGG':  'PFI',  # alternative: DFI
    'PCPG': 'PFI',  # not recommended, but largest number of events
    'PRAD': 'PFI',  # alternative: DFI
    'READ': 'PFI',  # only recommended
    'TGCT': 'PFI',  # alternative: DFI
    'THCA': 'PFI',  # alternative: DFI
    'THYM': 'PFI',  # alternative: DFI
  }

  def __init__(self, tcga_cgr_table):
    self.tcga_cgr_table_path = tcga_cgr_table
    self.df = self.read_table()

  def read_table(self):
    '''
    Pull the table into a dataframe and remove redacted patients.
    '''
    df = pd.read_excel(self.tcga_cgr_table_path,
                       sheet_name=0,
                       header=0,
                       na_values=['[Not Applicable]', '[Not Available]'])
    df = df[df['Redaction'].isnull()]
    return df

  def cancer_type_data(self, cancer_type, extra_data=[]):
    """
    Given a path to the TCGA-CDR Supplemental Table 1, and a cancer type, produce a pandas dataframe
    with the recommended time/censor columns and any extra clinical data explicitly requested.

    For all cancer types, cancer_type='*'
    """
    if cancer_type == '*':
      raise NotImplementedError

    ctype_df = self.df[self.df['type'] == cancer_type]

    endpoint = 'OS'
    if cancer_type in self.RECOMMENDED_ENDPOINTS:
      endpoint = self.RECOMMENDED_ENDPOINTS[cancer_type]

    ctype_df = ctype_df[[endpoint, endpoint + '.time']]
    ctype_df.columns = ['censor', 'time']
    return ctype_df


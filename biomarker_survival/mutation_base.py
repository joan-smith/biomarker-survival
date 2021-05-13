import pandas as pd
import numpy as np

from . import utilities as util

def prep_mutation_data_alone(mutation):
  df = pd.read_csv(mutation, sep='\t', low_memory=True, dtype=str)

  # remove column headers from combined mutation sheet
  df = df[~df['Hugo_Symbol'].str.contains('Hugo_Symbol')].copy(deep=True)
  df['Tumor_Sample_Barcode'] = df['Tumor_Sample_Barcode'].str.strip()

  number_barcodes_in_mutation_data = df['Tumor_Sample_Barcode'].unique().size
  print('Number of total sequenced barcodes:   ', number_barcodes_in_mutation_data)
  df = util.add_identifier_column(df, 'Tumor_Sample_Barcode')
  return df


def prep_data(df, clinical_data, cancer_type):
  df = util.maybe_clear_non_01s(df, 'Tumor_Sample_Barcode', cancer_type).copy(deep=True)
  df = util.add_identifier_column(df, 'Tumor_Sample_Barcode')

  # Reduce mutation data to patients that also have clinical data
  df = df.join(clinical_data, on='identifier', how='inner')
  df.set_index(['Hugo_Symbol', 'identifier'], inplace=True)

  # symmetrically filter clinical data down to patients that were also sequenced
  unique_patients =  df.index.get_level_values('identifier').unique()
  unique_patients_df = pd.DataFrame(unique_patients, index=unique_patients)
  clinical_data_with_sequenced_patients = clinical_data.join(unique_patients_df, how='inner')
  num_patients = clinical_data_with_sequenced_patients.shape[0]
  print('Number of patients with sequence and clinical data: ', num_patients)
  return df, clinical_data_with_sequenced_patients, num_patients

def mutations_for_gene(df):
  mutated_patients = df['identifier'].unique()
  return pd.DataFrame({'mutated': np.ones(len(mutated_patients))}, index=mutated_patients)

def drop_non_silent(mutation):
  # include only nonsilent mutations
  non_silent = mutation.where(mutation['Variant_Classification'] != 'Silent')
  mutation = non_silent.dropna(subset=['Variant_Classification'])
  return mutation

def pivot_mutation_list_to_mutations_per_gene(mutation):
  gene_mutation_df = mutation.groupby(['Hugo_Symbol']).apply(mutations_for_gene)
  gene_mutation_df.index.set_names(['Hugo_Symbol', 'patient'], inplace=True)
  gene_mutation_df = gene_mutation_df.reset_index()
  gene_patient_mutations = gene_mutation_df.pivot(index='Hugo_Symbol', columns='patient', values='mutated')

  return gene_patient_mutations.transpose().fillna(0)

def prep_mutation_data(mutation, clinical_data, cancer_type):
  mutation, clinical_data_w_seq_patients, num_patients = prep_data(mutation, clinical_data, cancer_type)
  mutation = drop_non_silent(mutation)

  mutation = mutation.reset_index()
  mutation['Hugo_Symbol'] = '\'' + mutation['Hugo_Symbol'].astype(str)

  return pivot_mutation_list_to_mutations_per_gene(mutation)


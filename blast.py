import pandas as pd
import numpy as np 



#read file and convert it into dataframe 
file_path= '/home/nguyenah/Bureau/raven_vs_GCA_025209345_blastn.txt'

def read_blast_output(file_path):
    result_data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming tab-delimited columns in the BLAST output
            columns = line.strip().split('\t')
            result_data.append(columns)
    return result_data

#call the function
blast_results = read_blast_output(file_path)
df_blast_results = pd.DataFrame(blast_results)
print(df_blast_results)

df_blast_results.to_csv('df_blast_result_raven.csv')


#separate each contig 

unique_contig = print(df_blast_results[0].unique())


def group_by_contig(df):
    grouped_dfs = {}

    for name, group in df.groupby(0):
        grouped_dfs[name] = group.reset_index(drop=True)

    return grouped_dfs

# Assuming df_blast_results is your DataFrame
# (replace it with the actual name of your DataFrame)
grouped_contig_dfs = group_by_contig(df_blast_results)

# Access individual DataFrames using contig IDs
for contig_id, contig_df in grouped_contig_dfs.items():
    print(f"Contig ID: {contig_id}")
    print(contig_df)
    print("\n")




def group_by_contig_with_calculation(df):
    grouped_dfs = {}
    subtract_result = {}

    for name, group in df.groupby(0):
        contig_df = group.copy()

        # Attempt to convert columns 6 and 7 to numeric
        contig_df[6] = pd.to_numeric(contig_df[6], errors='coerce')
        contig_df[7] = pd.to_numeric(contig_df[7], errors='coerce')

        # Calculate subtraction only if both columns are numeric
        if contig_df[6].dtype.kind == 'f' and contig_df[7].dtype.kind == 'f':
            contig_df['Subtraction_Result'] = contig_df[7] - contig_df[6]
        else:
            print(f"Skipping subtraction for contig {name} due to non-numeric values.")

        grouped_dfs[name] = group.reset_index(drop=True)
        subtract_result[name] = contig_df.reset_index(drop=True)

    return grouped_dfs, subtract_result

# Assuming df_blast_results is your DataFrame
# (replace it with the actual name of your DataFrame)
grouped_contig_dfs, subtract_result_dfs = group_by_contig_with_calculation(df_blast_results)

# Access individual DataFrames using contig IDs for grouping
for contig_id, contig_df in grouped_contig_dfs.items():
    print(f"Contig ID: {contig_id}")
    print(contig_df)
    print("\n")

# Access individual DataFrames using contig IDs for subtraction result
for contig_id, contig_df in subtract_result_dfs.items():
    print(f"Contig ID: {contig_id}")
    print(contig_df)
    print("\n")



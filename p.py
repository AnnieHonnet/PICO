ref_genome_path = "/home/nguyenah/Téléchargements/ncbi_dataset/data/GCA_025209345.1/GCA_025209345.1_ASM2520934v1_genomic.fna"

"""
def process_fna_file():
    with open(ref_genome_path, 'r') as ref_genome:
        # Initialize variables to store sequence information
        current_sequence_name = ""
        current_sequence = ""

        # Loop through each line in the file
        for line in ref_genome:
            # Skip lines starting with ">"
            if line.startswith('>'):
                # Process the previous sequence, if any
                if current_sequence_name:
                    process_sequence(current_sequence_name, current_sequence)
                
                # Get the name of the new sequence
                current_sequence_name = line.strip()[1:]
                current_sequence = ""
            else:
                # Append the sequence content
                current_sequence += line.strip()

        # Process the last sequence in the file
        if current_sequence_name:
            process_sequence(current_sequence_name, current_sequence)

def process_sequence(name, sequence):
    # Add your logic here to process each sequence
    # For example, you can print the name and length of each sequence
    print(f"Sequence Name: {name}, Length: {len(sequence)}")

# Call the function
process_fna_file()
"""

def calculate_total_length():
    total_length = 0
    with open(ref_genome_path, 'r') as ref_genome:
        # Initialize variables to store sequence information
        current_sequence = ""

        # Loop through each line in the file
        for line in ref_genome:
            # Skip lines starting with ">"
            if not line.startswith('>'):
                # Accumulate the length of the sequence
                current_sequence += line.strip()
        
        # Add the length of the last sequence in the file
        total_length += len(current_sequence)

    print("Total Length of All Sequences:", total_length)

# Call the function
calculate_total_length()



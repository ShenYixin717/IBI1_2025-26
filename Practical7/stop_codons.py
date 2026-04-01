import re
import os

start = 'ATG'
stop = 'TAG|TGA|TAA'

# location of the file
script_dir = os.path.dirname(os.path.abspath(__file__))
fasta_file = os.path.join(script_dir, "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
output_file = os.path.join(script_dir, "stop_genes.fa")

# read the inputfile
record = {'id': [], 'seq': []}
current_id = ""
current_seq = ""

with open(fasta_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            if current_id:
                record['id'].append(current_id)
                record['seq'].append(current_seq)
            current_id = line.split()[0][1:]
            current_seq = ""
        else:
            current_seq += line
if current_id:
    record['id'].append(current_id)
    record['seq'].append(current_seq)



# open the output file for writing
with open(output_file, "w") as out_f:
    # iterate through each gene and search for stop codons
    for i in range(len(record['id'])):
        gene_id = record['id'][i]
        seq = record['seq'][i]
        found_stops = set() # delete duplicates
        pattern = re.compile(rf'ATG(?:...)*?({stop})')
        for match in pattern.finditer(seq):
            if (match.end(1) - match.start()) % 3 == 0:
                found_stops.add(match.group(1))
        if found_stops:
            out_f.write(f">{gene_id} {','.join(found_stops)}\n{seq}\n")

print(f"Results have been written to {output_file}")

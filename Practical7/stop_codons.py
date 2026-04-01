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

    for i in range(len(record['id'])):
        gene_id = record['id'][i]
        seq = record['seq'][i]
        found_stops = set() # delete duplicates

        # handle the sequence
        for match_start in re.finditer(rf'{start}', seq):
            start_pos = match_start.start()
            sub_seq = seq[start_pos:]
            for match_stop in re.finditer(rf'({stop})', sub_seq):
                stop_pos = match_stop.start()
                if stop_pos % 3 == 0:
                    codon = match_stop.group()
                    found_stops.add(codon)
                    break
            if found_stops:
                header = f">{gene_id} | Start: {start_pos} | Stop codon: {codon}"
                out_f.write(f"{header}\n{seq}\n")


print(f"Results have been written to {output_file}")
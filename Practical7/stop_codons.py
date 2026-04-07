import re

start = 'ATG'

# read the inputfile
data = {"ID":[],"seq":[]}
current_seq = ""

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r") as book:
    text = book.readlines()
for line in text:
    line = line.strip()
    if str(line)[0] == ">": 
        if current_seq:
            data["seq"].append(current_seq)
        current_seq = ""
        name = re.search(r'>(\S*_mRNA)',line)
        if name:
            data["ID"].append(name.group(1))
    else:
        current_seq += line
data["seq"].append(current_seq)

# open the output file for writing
with open("stop_genes.fa", "w") as out_f:
    # handle each gene and search for stop codons
    for i in range(len(data['ID'])):
        seq = data['seq'][i]
        stops = ['TAG','TGA','TAA']
        existing_codes = ''
        if str(seq)[0:3] == 'ATG':
            for j in stops:
                founding = re.search(rf'ATG(?:(?!TAG|TGA|TAA)(...)*?{j}', seq)
                if founding:
                    existing_codes += (f'{j} ')
            if existing_codes:
                out_f.write(f">{data['ID'][i]}; {existing_codes}\n")
                out_f.write(f"{seq}\n")

print(f"Results have been written to stop_genes.fa")
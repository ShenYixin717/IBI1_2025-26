import re
import os
import matplotlib.pyplot as plt

# location of the file
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "stop_genes.fa")
output_png = os.path.join(script_dir, "codon_usage_pie.png")

# read the input words and find the longest ORF
end_code=['TAG', 'TGA', 'TAA']
while True:
    code = input("Enter a codon(TAG, TGA, TAA): ")
    if code in end_code:
        break
    else:
        print(f"{code} is not a stop codon.")


# read the input file
file_record = {"id": [], "seq": [], "ending": [], "length": []}
id = ""
seq = ""
with open(input_file, 'r') as f:
    for line in f:
        if line.startswith('>'):
            id = line.strip().split()[0][1:]
            file_record['id'].append(id)
        else:
            seq = line.strip()
            file_record['seq'].append(seq)
            file_record['length'].append(len(seq))
            file_record['ending'].append(seq[-3:])


# delete the duplicated id and find the longest ORF
temporary_id = file_record['id'][0]
temporary_seq = file_record['seq'][0]
temporary_length = file_record['length'][0]
ORF_record = []

for i in range(len(file_record['id'])):
    if file_record['id'][i] == temporary_id:
        if file_record['length'][i] > temporary_length:
            temporary_seq = file_record['seq'][i]
            temporary_length = file_record['length'][i]
    else:
        if code == file_record['ending'][i-1]:
            ORF_record.append(temporary_seq)


# count the codons
counts={}
for i in range(len(ORF_record)):
    for j in range(0, len(ORF_record[i]), 3):
        codon = ORF_record[i][j:j+3]
        if codon in counts:
            counts[codon] += 1
        else:
            counts[codon] = 1
print(counts)


# draw a pie chart
counts = {k:v for k,v in counts.items() if v>0}
colors = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'PURPLE']
plt.figure(figsize=(8,8), dpi=200)
plt.pie(counts.values(), labels=counts.keys(), colors=colors*10, 
        autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor':'white', 'linewidth':1})
plt.title(f'Codon Usage for {code}', fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig(output_png, bbox_inches='tight')
plt.show()
plt.close()

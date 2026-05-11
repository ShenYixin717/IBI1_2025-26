import re
import matplotlib.pyplot as plt


# read the input words and find the longest ORF
end_code=['TAG', 'TGA', 'TAA']
while True:
    code = input("Enter a codon(TAG, TGA, TAA): ")
    if code in end_code:
        break
    else:
        print(f"{code} is not a stop codon.")


# read the input file
file_record = {"id": [], "seq": []}
id = ""
seq = ""
with open("stop_genes.fa", 'r') as fa:
    for line in fa:
        if str(line)[0] == ">":
            id = line.strip().split()[0][1:]
            file_record['id'].append(id)
        else:
            file_record['seq'].append(line)


# find the longest ORF to replace the sequence
ORF_record = []
end_code = 'TAG|TGA|TAA'
for i in range(len(file_record['id'])):
    recent_seq = file_record['seq'][i]
    possible_ORF = re.findall(f"ATG(?:...)*(?:{end_code})",recent_seq)
    useful_seq = ""
    for j in possible_ORF:
        if len(j) > len(useful_seq):
            useful_seq = j
    if useful_seq[-3:] == code:
        ORF_record.append(useful_seq)

# count the codons
counts={}
for i in range(len(ORF_record)):
    for j in range(0, len(ORF_record[i]), 3):
        codon = ORF_record[i][j:j+3]
        if codon in counts:
            counts[codon] += 1
        else:
            counts[codon] = 1


# draw a pie chart
counts = {k:v for k,v in counts.items() if v>0}
colors = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'PURPLE']
plt.figure(figsize=(8,8), dpi=200)
plt.pie(counts.values(), labels=counts.keys(), colors=colors*10, 
        autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor':'white', 'linewidth':1})
plt.title(f'Codon Usage for {code}', fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig("codon_usage_pie.png", bbox_inches='tight')
plt.show()
plt.close()

import re
# initiate the sequence and the codons
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start = 'AUG'
stop = 'UAG|UGA|UAA'

# find all the ORF
ORF = re.findall(rf'{start}.*?(?:{stop})', seq)
print(ORF)

# find the longest ORF
longest_ORF = max(ORF, key=len)
print(f"The longest ORF is: {longest_ORF}")
print(f"It's length is: {len(longest_ORF)}")
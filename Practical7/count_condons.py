end_code=['TAG', 'TGA', 'TAA']
while True:
    code = input("Enter a codon(TAG, TGA, TAA): ")
    if code in end_code:
        break
    else:
        print(f"{code} is not a stop codon.")

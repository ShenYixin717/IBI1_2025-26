def calculate_protein_mass(seq):
    amino_acid_mass = {
        'G': 57.02,  # Glycine
        'A': 71.04,  # Alanine
        'S': 87.03,  # Serine
        'P': 97.05,  # Proline
        'V': 99.07,  # Valine
        'T': 101.05, # Threonine
        'C': 103.01, # Cysteine
        'I': 113.08, # Isoleucine
        'L': 113.08, # Leucine
        'N': 114.04, # Asparagine
        'D': 115.03, # Aspartic Acid
        'Q': 128.06, # Glutamine
        'K': 128.09, # Lysine
        'E': 129.04, # Glutamic Acid
        'M': 131.04, # Methionine
        'H': 137.06, # Histidine
        'F': 147.07, # Phenylalanine
        'R': 156.10, # Arginine
        'Y': 163.06, # Tyrosine
        'W': 186.08  # Tryptophan
    }

    mass = 0
    for i in seq:
        if i not in amino_acid_mass:
            return("The sequence is incorrect")
        mass += amino_acid_mass[i]
    return(f"The mass of the protein is {mass}")

#example
sequence = "DQKEM"
print(calculate_protein_mass(sequence))
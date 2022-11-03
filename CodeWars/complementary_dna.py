def DNA_strand(dna):
    strand = { "A": "T", "C": "G"}
    muntant = " "
    for i in dna:
        for key, value in strand.items():
            if i == key:
                muntant  += value
            elif i == value:
                muntant += key
    return muntant
            
print(DNA_strand("AAAA"))
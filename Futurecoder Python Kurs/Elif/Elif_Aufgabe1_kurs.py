dna = 'AGTAGCGTC'
opposite_dna = ''
for char in dna:
    if char == 'A':
        char = 'T'
    elif char == 'T':
        char = 'A'
    elif char == 'G':
        char = 'C'
    elif char == 'C':
        char = 'G'
    opposite_dna += char

print(opposite_dna)
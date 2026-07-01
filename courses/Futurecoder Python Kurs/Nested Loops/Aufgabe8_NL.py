#Excersice: For this exercise you are given a list of strings of equal length. 
# Write a program that prints the first letter of each string on one line, 
# then the second letter of each string on the next line, and so on.

strings = ['  b n', 'f ete', 'liths', 'astat', 't ene', '  r d']
max_length = max(len(s) for s in strings)

# Iterate over each column index
for i in range(max_length):
    print("".join(words[i] for words in strings if i < len(words)))
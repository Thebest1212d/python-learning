upper = True
sentence = 'your input sentence here'

result = []

for char in sentence:
    if upper:
        result.append(char.upper())
        upper = False
    else:
        result.append(char.lower())
        upper = True

sentence = ''.join(result)
print(sentence)

# upper = True
# sentence = ''
#
# for char in sentence:
#     if upper:
#         char = char.upper()
#         upper = False
#     else:
#         char = char.lower()
#         upper = True
#     sentence += char
#
# print(sentence)

sentence = 'Hello World'

include = False
new_sentence = ''
for char in sentence:
    if include == False:
        new_sentence += char
    include = True

print(new_sentence)
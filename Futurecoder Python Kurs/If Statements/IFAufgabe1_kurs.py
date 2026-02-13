sentence = 'Hello World'
excited = True
confused = True
if excited and confused == False:
    sentence += '!'
if confused and excited == False:
    sentence += '?'
if excited and confused:
    sentence += '!?'
print(sentence)
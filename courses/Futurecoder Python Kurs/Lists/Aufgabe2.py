string1 = 'Hello'
string2 = 'Elizabeth'

while(len(string1) < len(string2)):
    string1 += " "
while(len(string2) < len(string1)):
    string2 += " "

max_length = max(len(string1), len(string2))

for i in range(max_length):
    print(string1[i], string2[i])
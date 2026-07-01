#Excersice: Write a program to print every string that contains word. It should work for any word and strings.
# strings = [['hello there', 'how are you'], ['goodbye world', 'hello world']]
# word = 'hello'

# for sub in strings:
#     for words in sub:
#         if word in words:
#             print(words)


#Excersice: This time the output should tell us which sublists contain word, rather than which inner strings. 
#In particular, we want to print a boolean for each sublist: True if the sublist contains the word in any of its strings, False if it's not there at all.

# strings = [['hello there', 'how are you'], ['goodbye world', 'hello world']]
# word = 'hello'

# for sub in strings:
#     condi = False
#     for words in sub:
#         if word in words:
#             condi = True
#     print(condi)


#Excersice: Next, print only one boolean to indicate if word is present in any string in the entire nested list at all.

strings = [['hello there', 'how are you'], ['goodbye world', 'hello world']]
word = 'Python'
condi = False


for sub in strings:
    for words in sub:
        if word in words:
            condi = True
            
print(condi) 
    
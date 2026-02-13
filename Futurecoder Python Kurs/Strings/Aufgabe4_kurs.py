# name = 'World'
# line = name * len(name)

# print("+" + name + "+")
# print(name + line + name)
# print("+" + name + "+")


name = 'World'
line = " " * len(name)

print("+" + name + "+")

for char in name:
    print(char + line + char)

print("+" + name + "+")

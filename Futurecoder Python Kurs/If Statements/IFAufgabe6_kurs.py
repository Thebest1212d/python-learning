x1 = 30
x2 = 10
x3 = 20
res = 0
if x1 > x2 and x3 > x2:
    res = x2
elif x2 > x1 and x3 > x1:
    res = x1
elif x2 > x3 and x1 > x3:
    res = x3

print(res)
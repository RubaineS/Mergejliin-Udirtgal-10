a = int(input())
c = 0
for i in range(0, a, 1):
    b = int(input())
    c+= b if b>0 else 0
print(c)
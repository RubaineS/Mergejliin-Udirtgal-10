l = []
a = int(input())
c = 0
for i in range(0, a, 1):
    b = int(input())
    l.append(b)
    c+=l[i]
print(c)
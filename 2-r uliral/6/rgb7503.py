a = int(input())
l = []
y = 0
n = 0
for i in range(0, a, 1):
    b = int(input())
    if b%2==0:
        n+=1
    else:
        y+=1
print("YES" if y>n else "NO")
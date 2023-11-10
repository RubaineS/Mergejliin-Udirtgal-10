n = int(input())
for j in range(1, n, 1):
    o = 0
    for i in range (1, j, 1):
        if (j%i==0):
            o+=i
    if(j==o):
        print(j)
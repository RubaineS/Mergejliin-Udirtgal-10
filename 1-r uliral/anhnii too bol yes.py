import math #anhnii too
n = int(input())
s = 0
m = int(math.sqrt(n)+1)
for i in range (2, m, 1):
    if (n%i==0):
        s = 1
    else:
        s="yes"
if (s!=1):
    print(s)
else:
    print('NO')
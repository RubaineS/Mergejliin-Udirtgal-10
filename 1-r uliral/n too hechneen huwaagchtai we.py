n = int(input())#n too hechneen huwaagchtai
o = 0
for i in range (1, n+1, 1):
    if (n%i==0):
        o+=1
print(o)
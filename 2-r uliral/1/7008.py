a = int(input())

def d(a):
    b = int(a/10) #123 12.3
    c = int(b/10) #123 1
    d = b-(c*10)
    return d
print(d(a))
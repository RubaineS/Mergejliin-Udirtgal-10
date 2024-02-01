a = int(input())
def f(a):
    b = a%10 
    c = a%100
    d = (a-c)/100
    e = (c-b)/10
    f = b+d+e
    return f
print(int(f(a)))
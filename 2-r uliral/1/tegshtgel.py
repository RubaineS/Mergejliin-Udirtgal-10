#y = x^2+5x-20
import sys
sys.stdin = open(r"c:\Users\ruby0\OneDrive\Documents\GitHub\MergejliinUdirtgal\2-1\tegshtgel.in", "r")
sys.stdout = open(r"c:\Users\ruby0\OneDrive\Documents\GitHub\MergejliinUdirtgal\2-1\tegshtgel.out", "w")
def tegshtgel(x, y, z):
    x0 = (y ** 2) - (4 * x * z)
    x1 = (-y + (x0**0.5))/(2*x)
    x2 = (-y - (x0**0.5))/(2*x)
    return "{:.2f}".format(x1), f"{x2:.2f}", round(x1, 3), round(x2, 3)
a, b, c = map(int, input().split())
d = tegshtgel(a, b, c)
print(d)

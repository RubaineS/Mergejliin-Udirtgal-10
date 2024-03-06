import time
start = time.time()

a, b, c = map(int, input().split())
h=input("(1) 2 Digit LCM Or \n(2) 3 Digit LCM\n :")
if h == "2":
    while True:
        def lcm(x, y, z):
            gcd2 = gcd(y, z)
            gcd3 = gcd(x, gcd2)

            lcm2 = y*z // gcd2
            lcm3 = x*lcm2 // gcd(x, lcm2)
            return lcm3

        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        z = int(input("Number 3: "))
        print("The LCM Of " + str(x) + " And " + str(y) + " And " + str(z) + " Is " + str(lcm(x, y, z)))
print(lcm(a, b, c))

end = time.time()
print(end-start)
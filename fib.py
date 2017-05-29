# fibonacci sequence

def fib(n):
    if (n < 2):
        return 1
    a, b = 1, 1
    while (n-2 > 0):
        a, b = b, a+b
        n = n - 1
    return b

def F(n):
    if n == 0: return 0   # == means equal to
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)

#for i in range(40):
 #    print i, F(i)
print map(F, range(0, 30))

# checking a number prime or not
num = 23

for i in range(2,num):
    if (num % i) == 0:
        print "not prime: it is product of", i, "and", num//i
        break
else:
    print "Prime"
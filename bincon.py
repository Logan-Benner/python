# bincon.py lb
# Convert a base 10 number to binary
# Use 191 base 10 equal to 1011 1111 base 2
# q(quotient) d(divisor) r(remainder) n(integer input)
# div 128 * * * * * * *
n = int(input("Input an integer less 256 : "))
d = 128
q = int (n / d)
r = int (n % d) 
print(d,q,r)
n = r
# div 128 * * * * * * *
d = int (d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
# div 128 * * * * * * *
d = int (d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
# div 128 * * * * * * *
d = int (d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
# div 128 * * * * * * *
d = int (d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
# div 128 * * * * * * *
d = int (d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
# div 128 * * * * * * *
d = int (d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r
# div 128 * * * * * * *
d = int (d / 2)
q = int(n / d)
r = int(n % d)
print(d,q,r)
n = r


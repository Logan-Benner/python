# bincon_loop.py lb
# Convert a base 10 number to binary
# q(quotient) d(divisor) n(integer input)
# div 128 * * * * * * *
n = int(input("Input and integer less than 256 : "))
n_orginal = n
d = 128
binString ="" #create a string called binString
for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		print(d,q,r)# debug line
		n = r
		d = int(d / 2)
		binString = binString+str(q)
print("\n*********\t")
print
print(str(n_orginal)+" base 10 = "+binString+" base 2")
print("\n*********\t")

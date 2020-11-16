#asc2.py lb
for i in range (32,127):
	c = chr(i)
	print("[",i,"=",c,"]",end="")
	if (i % 5 == 0):
		print("\n")

#!/usr/bin/env python3
#dec2bin.py lb
# 10 base 10 = 1010 base 2

def dec2bin(n):
	# bs is the binary string
	binValue = bin(n)
	bs = str(binValue)
	#print(bs)
	b = bs.replace('0b','')
	return b # b is a string
	
def main():
	bString = dec2bin(10)
	print(10,"=",bString)
	bString = dec2bin(23)
	print(23,"=",bString)
	
main()

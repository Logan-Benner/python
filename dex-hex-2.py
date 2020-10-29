#!/usr/bin/env python3
# dec2hex.py
def dec2hex(dec):
	hexValue = hex(dec)
	hexS = str(hex(dec))
	h = hexS.replace('0x', '')
	#print(dec,hexValue,h) #debug
	return h
	
def main():
	print(" DECIMAL TO HEXADECIMAL CONVERTION ")
	hexString = dec2hex(10)
	print(10,hexString)
	hexString = dec2hex(245)
	print(245,hexString)
	
main()

'''
functions
return a string from a function
the string funcdtion "replace"
'''

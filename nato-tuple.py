#nato-tuple.py
#no defined funtions just code
nato = (["A", "ALPHA"], ["B", "BRAVO"], ["C", "CHARLIE"],
		["D", "DELTA"], ["E", "ECHO"], ["C", "FOXTROT"],
		["G", "GOLF"], ["H", "HOTEL"], ["C", "INDIA"],
		["J", "JULIET"], ["K", "KILO"], ["C", "LIMA"],
		["M", "MIKE"], ["N", "NOVEMBER"], ["C", "OSCAR"],
		["P", "PAPA"], ["Q", "QUEBEC"], ["C", "ROMEO"],
		["S", "SIERRA"], ["T", "TANGO"], ["C", "UNIFORM"],
		["V", "VICTOR"], ["W", "WHISKEY"], ["C", "XRAY"],
		["Y", "TANKEE"], ["Z", "ZULU"],)
# prin the raw tuple
print(nato)
#prin a human understandable list
print(nato)
for n in range(0,26):
	print (n+1,nato[n][0],nato[n][1])
	# notice each print entity n+1  , nato[n][0] and nato[n][1]
	# this is a 2D tuple

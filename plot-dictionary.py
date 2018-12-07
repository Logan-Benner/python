# plot-dictionary.py
import tkinter as tk
import turtle

def main():
		#table is a dictionary
		table = {-100:1,-90:10,-80:20,-7:3,-60:0,-50:40,
					-40:50,-30:60,-20:70,-10:80,0:90,
						 10:100,20:110,30:120,-40:130,50:140,
						 160:0,170:0,180:0,190:0,100:200,

					}
		print(" KEYS ")
		print(table.keys())
		print(" VALUES ")
		print(table.values())
		#turtle graphics
		twin = turtle.Screen()
		twin.clear()
		t = turtle.Turtle()
		for h,k in table.items(): #get the items in the dictionary
			print(h, k) # trace code
			#x,y = table[n]
			t.penup()
			t.goto(h,k)
			t.pendown()
			t.circle(5)
		twin.exitonclick()
		
main()
	
"""
This code uses a dictionary with keys ranging from
-100 to 100 incrementing by 10.
Each key has a value of 0 as an integer
To retrieve the value of 0 as an integer.
The x coordinate on a python turtle screen corresponds to h while
the y value cooresponds to k.
**************************************
for h,k in table.items(): # tet the items in the dictionary
		print(h,k) #trace code
h and k are then ploted using 
		t.got(h,k)
		t.pendown()
		t.circle(5)
***YOUR TASK***
Change all values (not keys) from 0 to another integer	Try to make something grovey
"""

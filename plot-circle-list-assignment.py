'''
Test this.
https://tritech-testsite.smapply.io/

python-circle-list-assignment.py
Get the code: 10.183.1.26 code python
Plot circle data using python
- Use your data
- Change the background color
- Change the graph line colors
- Change the plot line color
- Change the plot dot color
- Label the graph with text Plotting Circumference and Diameter
- Label the axis with text (Circumference and Diameter)
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py

'''

import turtle
import math
wdth = 800; hgth = 800; bgstring = "#ffffed"
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"

def grid(t):
	x = 0; y = 0
	while (x < 400):
		t.penup()
		t.color("#0000ff")
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = 0; y = 0
	while (y < 400):
		t.penup()
		t.color("#ff0000")
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	t.penup()
	t.goto(-170,300)
	t.pendown()
	t.color('#00ff00')
	style = ('Courier', 19, 'bold')
	t.penup()
	t.goto(-40, 0)
	t.write('C\ni\nr\nc\nu\nm\nf\ne\nr\ne\nn\nc\ne ', font=style, align='left')
	t.penup()
	t.goto(0, -40)
	t.pendown()
	style = ('Courier', 20, 'bold')
	t.write('Diameter', font=style, align='left')
	t.penup()
	t.goto(210,300)
	t.pendown()
	t.write('Circumference and diameter', font=style, align='center')
	t.hideturtle()
	t.penup()

def plotCircles(t):
	#list  named d and c
	c =  [64.3, 32.97, 16, 8,  4, 2] 
	d =  [20.10, 10.5, 4.3, 3.3,  1.3, .60] 
	# list dsorted and csorted
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.goto(0,0)
	t.pendown()
	t.color("#ff00ff")
	t.dot(3, blue)
	t.goto(dsorted[0],csorted[0])
	t.dot(3, blue)
	t.goto(dsorted[1],csorted[1])
	t.dot(3, blue)
	t.goto(dsorted[2],csorted[2])
	t.dot(3, blue)
	t.goto(dsorted[3],csorted[3])
	t.dot(3, blue)
	t.goto(dsorted[4],csorted[4])
	t.dot(3, blue)
	t.goto(dsorted[5],csorted[5])
	t.dot(3, blue)
	
def main():
	try:
		turtle.tracer(0)
		turtle.speed(100)
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		turtle.bgcolor("#d9d9d9")
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.hideturtle()
		grid(t)
		plotCircles(t)
		w.exitonclick()
		
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''

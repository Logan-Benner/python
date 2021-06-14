import turtle
import math
import random 

def circles(t,x,y,size):
	t.circle(size)
	for i in range(1, 10):
		t.circle(size * i)
	
	
def main():
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#tWin = turtle.Screen()
	t.penup()
	t.goto(100,100)
	t.pendown() 
	t.color("#ff00ff")
	x = 10;y = 20
	circles(t,x,y,100)
	t.color("#ff0000")
	t.width(5)
	t.goto(100,100)

	t.goto(-100,100)
	t.goto(-100,-100)
	t.goto(100,-100)
	t.goto(100,100)
	twin.exitonclick()
	
if __name__ == "__main__":
	main()

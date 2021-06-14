import turtle
import math
import random 

def circles(t,x,y,size):
	for i in range(1,5):
		t.circle(size * i)
	
	
def main():
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#tWin = turtle.Screen()
	t.penup()
	t.goto(100,100)
	t.pendown() 
	x = 10;y = 20
	circles(t,x,y,100)
	t.width(10)
	t.goto(100,100)
	t.color("#00ff00")
	t.goto(-100,100)
	t.color("#0000ff")
	t.goto(-100,-100)
	t.color("#ffff00")
	t.goto(100,-100)
	t.color("#00ffff")
	t.goto(100,100)
	twin.exitonclick()
	
if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

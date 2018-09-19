# ex4b.pycwc
import turtle  
w = turtle.Screen()
w.bgcolor("#00cc00")
t = turtle.Turtle()
t.color("#ffffff")
t.width(20)
def thepoly(size):
	for i in range(4):
		t.fd(size)
        t.left(90)
        size = size + 5

thepoly(5)
thepoly(10)
thepoly(15)
thepoly(20)
thepoly(25)
holdit = input();

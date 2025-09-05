# imports turtle module
import turtle

# "t" is the name of the turtle & "screen" creates the screen for the turtle.
t = turtle.Turtle()
screen = turtle.Screen()

# function filledSquare creates a filledSquare using "t" the turtle.
def filledSquare(t, w, color):
	
	t.fillcolor(color)
	t.begin_fill()
	for i in range(4):
		t.forward(w)
		t.right(90)
	t.end_fill()
	
t.up()
t.goto(-200,0)
t.down()

# function filledRectangle creates a filledRectangle using "t" the turtle.
def filledRectangle(t, w, h, color):
	t.fillcolor(color)
	t.begin_fill()
	for i in range(2):
		t.forward(w)
		t.right(90)
		t.forward(h)
		t.right(90)
	t.end_fill()
	
def main():
    #filledSquare(t, 40, "red")
    filledRectangle(t, 100, 50, "red")

main()
turtle.done()
    
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

# function trainCar simulates a train car utilzing the function filledRectangle, "t" the turtle, and other turtle functions in the turtle module.
def trainCar(t, x, y, color):
	wheelY = y - 80 - 15
	t.up()
	t.goto(x, y)
	t.down()
	t.fillcolor(color)
	t.begin_fill()
	for i in range(2):
		t.forward(150)
		t.right(90)
		t.forward(80)
		t.right(90)

	# the left wheel for the train car.
	t.end_fill()
	t.up()
	t.goto(x + 15, wheelY)
	t.down()
	t.fillcolor("black")
	t.begin_fill()
	t.circle(15)
	t.end_fill()

	# the right wheel for the train car.
	t.up()
	t.goto(x + 150 - 15, wheelY)
	t.down()
	t.fillcolor("black")
	t.begin_fill()
	t.circle(15)
	t.end_fill()	

# main function will run the application.
def main():
	trainCar(t, 150, 0, "yellow")
	trainCar(t, -50, 0, "green")
	trainCar(t, -250, 0, "blue")
main()
turtle.done()
    
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

# function drawTrainCar simulates a train car utilzing the function filledRectangle, "t" the turtle, and other turtle functions in the turtle module.
def drawTrainCar(t, x, y, color):
	wheelY = y - 80 - 15
	t.up()
	t.goto(x, y)
	t.down()
	filledRectangle(t, 150, 80, color)

	# the left wheel for the train car.
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

# function  drawLocomotive simulates a locomotive utilzing the functions filledRectangle and filledSquare, "t" the turtle, and other turtle functions in the turtle module.
def drawLocomotive(t, x, y):
	wheelY = y - 80 - 15
	t.up()
	t.goto(x, y)
	t.down()
	t.fillcolor("red")
	t.begin_fill()
	for i in range(2):
		t.forward(150)
		t.right(90)
		t.forward(80)
		t.right(90)
	t.end_fill()

	# creates the smoke stack for the locomotive.
	t.up()
	t.goto(x + 20, y + 30)
	t.down()
	filledRectangle(t, 20, 60, "gray")

	# creates the area where the driver of the locomotive resides.
	t.up()
	t.goto(x + 80, y + 30)
	t.down()
	filledSquare(t, 50, "red")

	# the left wheel for the train car.
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

	# divides the x coordinate by 2 so "t" the turtle can be centered properly, then subtracts the y coordinate to align the text "Evan Garcia" properly in the locomotive.
	t.up()
	t.goto(x + 150/2, y - 60)
	t.down()
	t.color("black")
	t.write("Evan Garcia", align="center", font=("Arial", 16, "bold"))
	t.color("black")        

# main function will run the application and create our trains!
def main():
	drawLocomotive(t, -450, 0)
	drawTrainCar(t, 150, 0, "yellow")
	drawTrainCar(t, -50, 0, "green")
	drawTrainCar(t, -250, 0, "blue")
main()
turtle.done()
    
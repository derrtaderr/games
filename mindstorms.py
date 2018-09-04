import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def daraw_art():
	window = turtle.Screen()
	window.bgcolor("red")
    # create the turtle sax - draws a square
	sax = turtle.Turtle()
	turtle.shape("turtle")
	turtle.color("blue",)
	turtle.speed(10)
	for i in range(1,37):
		draw_square(sax)
		sax.right(10)

	window.exitonclick()

daraw_art()
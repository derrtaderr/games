import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("orange")

	flower = turtle.Turtle()
	flower.speed(50)
	flower.shape("turtle")
	flower.right(45)
	for i in range(1,37):
		for j in range(1,5):
			draw_circle(flower,i,"green")
			flower.left(90)
	flower.right(45)
	flower.color("green")
	flower.forward(200)

	window.exitonclick()

def draw_circle(circle,radius, color):
	circle.color(color)
	circle.circle(radius)

draw_shapes()
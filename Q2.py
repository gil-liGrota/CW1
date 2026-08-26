#Name: Gil-li Ness Grota
import turtle


t = turtle.Turtle()

# t.forward(100) # will go forward x steps
# t.goto(-100,100) # will go to the x, y coordinate
# t.home() # will go to the start point
# t.circle(100) #drow a circle in x radios
# t.pen(fillcolor="black", pencolor="red", pensize=10) #control on the pen outline size, fill and size
# t.color("pink") #change the color of the line
# t.pencolor("red") #change the color of the pen


for i in range(4):
    t.forward(90)
    t.left(90)

t.fillcolor("blue")
t.begin_fill()
t.circle(100)
t.end_fill()

t.reset()
t.goto(100,80)
t.goto(45,80)

t.screen.bgcolor("red")
t.screen.title("session practice turtle")

t.pensize(4)
t.forward(200)
x = input()
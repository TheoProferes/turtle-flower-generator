import turtle
turtle1=turtle.Turtle()
def petal (turtle,petalnum):
    turtle.forward(100)
    turtle.left(51.15)
    turtle.forward(100)
    turtle.left(128.85)
    turtle.forward(100)
    turtle.left(51.15)
    turtle.forward(100)
petalnum= 10
degrees = 0
turtle1.speed(0)

for count in range (petalnum):
    turtle1.setheading(degrees)
    petal(turtle1,petalnum)
    degrees=degrees+360/petalnum
    
    




turtle.done()

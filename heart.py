import turtle as t
t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
s.speed(1)
t.hideturtle()
t.goto(0,-10)

t.pensize(5)
t.color("red")
t.befin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-90, 130)
t.pendown()
t.color("whithe")
t.write("Te Amo Juan David!", font=("Verdana",25, "bold"))

t.penup()
t.goto(-50,90)
t.pendown()
t.color("white")
t.write("Espero que esto te haga felix", font=("Verdana", 10, "bold"))


t.hideturtle()
t.done()

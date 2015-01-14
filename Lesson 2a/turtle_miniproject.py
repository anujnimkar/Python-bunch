import turtle

def first_letter(firstletter):
    firstletter.forward(50)
    firstletter.right(90)
    firstletter.forward(100)
    firstletter.backward(100)
    firstletter.right(90)
    firstletter.forward(50)
    firstletter.left(90)
    firstletter.forward(100)
    firstletter.left(90)
    firstletter.left(90)
    firstletter.forward(50)
    firstletter.right(90)
    firstletter.forward(50)

def second_letter(secondletter):
    secondletter.forward(50) 
    secondletter.color("red")
    secondletter.forward(50) 
    secondletter.color("black")
    secondletter.forward(50)
    secondletter.right(90)
    secondletter.forward(100)
    secondletter.right(90)
    secondletter.right(90)
    secondletter.forward(100)
    secondletter.left(90)
    secondletter.forward(50)
    secondletter.left(90)
    secondletter.forward(100) 
 
def turtle_def():
    window = turtle.Screen()
    window.bgcolor("red") 

    a = turtle.Turtle()
    a.color("black") 
    a.speed(1)
    first_letter(a)

    n = turtle.Turtle()
    n.color("black")
    n.speed(1)
    second_letter(n)

    window.exitonclick()
 
turtle_def()
 

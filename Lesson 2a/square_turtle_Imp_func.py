import turtle

def draw_fig(turtlename):
    for j in range(0,36):   
        for k in range(1,4):
            turtlename.forward(100)
            turtlename.right(90) 
        turtlename.forward(100)
        turtlename.right(80) 

def turtle_def():
    window = turtle.Screen()
    window.bgcolor("red")

    pitt = turtle.Turtle()

    pitt.color("black")
    pitt.speed(100000)

    draw_fig(pitt) 

    angie = turtle.Turtle()
    angie.color("blue")
    angie.speed(10)

    angie.forward(300)
    angie.right(120)

    angie.forward(300)
    angie.right(120)

    angie.forward(300)
     
    window.exitonclick()

turtle_def()
 

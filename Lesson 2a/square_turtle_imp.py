import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    pitt = turtle.Turtle()

    pitt.color("black")
    pitt.speed(100000) 

    
    for j in range(0,36):   
        for k in range(1,4):
            pitt.forward(100)
            pitt.right(90) 
        pitt.forward(100)
        pitt.right(80)

    angie = turtle.Turtle()
    angie.color("blue")
    angie.speed(10)

    angie.forward(300)
    angie.right(120)

    angie.forward(300)
    angie.right(120)

    angie.forward(300)
    
        
    window.exitonclick()   
      
draw_square()

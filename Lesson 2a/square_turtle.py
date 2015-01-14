import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    pitt = turtle.Turtle()

    pitt.color("black")
    pitt.speed(1) 

    for i in range(0,200):
        for j in range(0,200):  
            pitt.forward(100)
            pitt.right(90) 

            pitt.forward(100)
            pitt.right(90)

            pitt.forward(100)
            pitt.right(90) 

            pitt.forward(100)
            pitt.right(80)
                

    window.exitonclick() 
     
    

draw_square()

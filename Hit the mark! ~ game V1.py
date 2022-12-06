import turtle
import random
import math
A=0
B=0
scor=0



afisare=turtle.Turtle()
afisare.hideturtle()
afisare.penup()
afisare.setposition(-460,340)
afisare.pendown()
def afisarescor():
     afisare.clear()
     mesaj='Puncte: '+str(scor)
     afisare.write(mesaj, font=('Arial',40,'italic'))
afisare.color('green')
     
poz=turtle.Turtle()
poz.hideturtle()
turtle.listen
def click(x,y):
     global scor
     poz.penup()
     poz.goto(x,y)
     poz.pendown()
     print(x,y)
     if(math.fabs(A-x)<=20 and math.fabs(B-y)<=20):
          scor=scor+1
          afisarescor()
          




     
            
tinta=turtle.Turtle()
tinta.hideturtle()
tinta.color('red')
def deseneazatinta():
     global A,B
     tinta.clear()
     A=random.randint(-220,200)
     B=random.randint(-220,200)
     tinta.begin_fill()
     tinta.penup()
     tinta.goto(A,B)
     tinta.pendown()
     tinta.circle(10)
     tinta.end_fill()
     turtle.ontimer(deseneazatinta,1000)
     print(A,B)





afisarescor() 
deseneazatinta()
turtle.onscreenclick(click)

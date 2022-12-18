import turtle
import random
import math
A=0
B=0
scor=0
F=3

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
    
tinta=turtle.Turtle()
tinta.hideturtle()
tinta.color('red')
tinta.speed(11)
def deseneazatinta():
     global A,B
     tinta.clear()
     A=random.randint(-220,200)
     B=random.randint(-220,200)
     tinta.begin_fill()
     tinta.penup()
     tinta.goto(A,B)
     tinta.pendown()
     tinta.circle(12)
     tinta.end_fill()

poz=turtle.Turtle()
poz.hideturtle()
turtle.listen
def click(x,y):
     global scor,F
     if(math.fabs(A-x)<=20 and math.fabs(B-y)<=20):
          poz.clear()
          tinta.clear()
          scor=scor+1
          afisarescor()
          deseneazatinta()
          F=F+1
     elif(math.fabs(A-x)>10 and math.fabs(B-y)>10):
          F=F-1
     if(F==10):
          tinta.color("green")
     if(F==20):
          tinta.color("purple")
     if(F==30):
          tinta.color("brown")
     if(F==40):
          tinta.color("red")      
     if(F==2):
          vt3.clear()
     if(F==1):
          vt2.clear()
     if(F==0):
          vt1.clear()
          tinta.clear()
          end=turtle.Turtle()
          end.hideturtle()
          end.color('red')
          end.penup()
          end.goto(-200,0)
          end.pendown()
          mj="You lost!!!"
          end.write(mj,font=("Ebrima",60,'bold',))

vt1=turtle.Turtle()
vt1.hideturtle()
vt1.speed(11)
vt1.penup()
vt1.goto(100,350)
vt1.pendown()
vt1.color('brown')
def viata1():
     m1=("\u2764\ufe0f")
     vt1.write(m1, font=("Arial", 45, "normal"))

vt2=turtle.Turtle()
vt2.hideturtle()
vt2.speed(11)
vt2.penup()
vt2.goto(200,350)
vt2.pendown()
vt2.color('brown')
def viata2():
     m1=("\u2764\ufe0f")
     vt2.write(m1, font=("Arial", 45, "normal"))
     
vt3=turtle.Turtle()
vt3.hideturtle()
vt3.speed(11)
vt3.penup()
vt3.goto(300,350)
vt3.pendown()
vt3.color('brown')
def viata3():
     m1=("\u2764\ufe0f")
     vt3.write(m1, font=("Arial", 45, "normal"))

viata1()
viata2()
viata3()
afisarescor()
deseneazatinta()
turtle.onscreenclick(click)

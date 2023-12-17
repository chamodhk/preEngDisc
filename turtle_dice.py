from turtle import *
from random import randint

number = randint(1,6)
ht()
def draw_circle(x,y,r=10):
  penup()
  setheading(0)
  setpos(x,y-r)
  pendown()
  begin_fill()
  circle(r)
  penup()
  end_fill()
  
  
speed(0)

home()
for i in range(4):
  forward(100)
  left(90)
  
if number == 1:
  draw_circle(50,50)

elif number == 2:
  draw_circle(25,75)
  draw_circle(75,25)
  
elif number ==3:
  draw_circle(25,75)
  draw_circle(50,50)
  draw_circle(75,25)
  
elif number == 4:
  draw_circle(25,75)
  draw_circle(25,25)
  draw_circle(75,75)
  draw_circle(75,25)
  
elif number == 5:
  draw_circle(25,75)
  draw_circle(25,25)
  draw_circle(75,75)
  draw_circle(75,25)
  draw_circle(50,50)
  
else:
  draw_circle(25,75)
  draw_circle(25,50)
  draw_circle(25,25)
  draw_circle(75,75)
  draw_circle(75,50)
  draw_circle(75,25)
  

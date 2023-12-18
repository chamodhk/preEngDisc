from turtle import *

first_row = ["blue","black","red"]
second_row = ['yellow','green']

pensize(7)
def draw_row(x,colors,y=0):
  for color in colors:
    pencolor(color)
    penup()
    setpos(x,y)
    pendown()
    circle(75)
    x = x + 100
  
draw_row(-100,first_row)

draw_row(-50,second_row,-75)

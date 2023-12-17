#to draw a circle around a point using turtle graphics, we can use this simple function.

from turtle import penup, pendown, circle,setheading

def centerCircle(center_x, center_y, r):
  '''This function takes three positional parameters, 
    center_x = x coordinates of the circle's center
    center_y = y coordinate of the circle's center,
    r = radius of the circle

    '''
  setheading(0)
  penup()
  setpos(center_x, center_y-r)
  pendown()
  circle(r)
  

import turtle as t

r = 50
t.pensize(10)
for i in range(4):
  t.penup()
  t.setpos(r*-2+75*i,0)
  t.pendown()
  t.circle(r)
  t.ht()

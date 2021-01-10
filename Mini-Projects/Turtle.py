import turtle

colors = ['red','yellow','purple','orange','blue','green']

pen = turtle.Pen()

turtle.bgcolor('Black')
turtle.speed(0)

for x in range(1,1200):
    pen.pencolor(colors[x%6])
    pen.width(x/100+1)
    pen.forward(x)
    pen.left(59)
    #pen.right(10*x)
    #pen.backward(x+10)
turtle.done()

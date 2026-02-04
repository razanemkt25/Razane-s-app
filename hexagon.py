import turtle
t=turtle.Turtle()
colors=["white","red","green","white","red","green"]
for i in range(6):
    size=int(input("choose the size of the side: "))
    t.color(colors[i])
    t.forward(size)
    t.right(60)
    
turtle.done()   
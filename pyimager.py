import turtle
pyimg = input("what is the name of the pyimg file you want to open?")
pyimg = pyimg + ".pyimg"
with open(pyimg,"r") as file:
    width = int(file.readline().strip())
    height = int(file.readline().strip())
    pxsize = int(file.readline().strip())
    pixels = [line.strip() for line in file]
    while True:
        line = file.readline()
        if not line:
            break
        pixels.append(line)
x = (0-width)
y = height
drawer = turtle.Turtle()
drawer.speed(0)
drawer.ht()
drawer.pensize(pxsize)
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("grey")
#screen.setup(width,height)
newpos = 0
drawer.setpos(0,0)
pxdrawn = 0
index = 0
drawer.pu()
drawer.setpos(x,y)
for i in range(height):
  for j in range(width):
    if index < len(pixels):
        drawer.color(pixels[index])
    else:
        drawer.color("pink")
    drawer.pd()
    drawer.forward(1)
    drawer.pu()
    drawer.forward(pxsize-1.2)
    index+=1
  drawer.pu()
  y-=pxsize
  drawer.setpos(x,y)
  drawer.pd()
screen.update()
drawer.pu()
drawer.setpos(400,400)
turtle.done()
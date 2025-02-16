import turtle
pixels = []
loading = input("input new to create a new pyimg, input load to load an existing one  ")
if loading == "new":
    loading = 1
else:
    loading = 0
def load_pyimg(filename):
        global pixels, width, height,pixelx,pixely,pxsize,totalpx
        with open(filename, "r") as file:
            lines = file.readlines()
            width = int(lines[0])
            height = int(lines[1])
            pxsize = int(lines[2])
            totalpx = (width*height)
            pixels = [line.strip() for line in lines[3:]]
            pixelx = []
            pixely= []
if loading: 
    global pixelx,pixely,name,pxsize
    name = input("what do you want the file to be named?")
    width = int(input("what do you want the width to be?"))
    height = int(input("what do you want the height to be?"))
    totalpx =  (width*height)
    pxsize = 5
    name = name + ".pyimg"
    pixels = []
    pixelx = []
    pixely = []
    for i in range(totalpx):
        pixels.append("white")
else:
    name = input("what is the name of the pyimg file you want to load?")
    name = name+".pyimg"
    load_pyimg(name)

screen = turtle.Screen()
drawer = turtle.Turtle()
screen.bgcolor("grey")
screen.tracer(0,0)
end = False
def drawgrid():
    global x,y,pixelx,pixely
    pixelx = []
    pixely = []
    index = 0
    x = (0-width)
    y = height
    drawer.pu()
    drawer.goto(x,y)
    drawer.speed(2)
    drawer.pensize(5)
    for i in range(height):
        for j in range(width):
            drawer.color(pixels[index])
            drawer.pd()
            drawer.forward(1)
            drawer.pu()
            pixelx.append(drawer.xcor())
            pixely.append(drawer.ycor())
            drawer.pu()
            drawer.forward(pxsize-1)
            drawer.pd()
            index+=1
        y -= (pxsize*1.2)
        drawer.pu()
        drawer.goto(x,y)
        drawer.pd()
    drawer.ht()

box=turtle.Turtle()
box.pencolor("white")
box.ht()
box.pu()
boxpos = 0
color = "black"
drawer.clear()
drawgrid()
while end == False:
    def update():
        drawer.clear()
        drawgrid()
    box.goto(pixelx[boxpos],pixely[boxpos])
    box.clear()
    box.stamp()
    def right():
        global boxpos
        boxpos += 1
    def left():
        global boxpos
        boxpos -= 1
    def up():
        global boxpos
        boxpos-= width
        if boxpos < 0:
            boxpos = 0
    def down():
        global boxpos,totalpx
        boxpos+= width
        if boxpos > (totalpx-1):
            boxpos = (totalpx-1)
    def changecolor():
        global color
        color = input("what color do you wan to change to?")
    def draw():
        pixels[boxpos] = color
        update()
    def editsize():
        global pxsize
        pxsize = int(input("what do you want to change the pixel size to?"))
        
    def save():
        with open(name, "w") as file:
            file.write(f"{width}\n")
            file.write(f"{height}\n")
            file.write(f"{pxsize}\n")   
            file.write("\n".join(pixels))
        print(f"Image saved to {name}")
        
    screen.onkey(right,"Right")
    screen.onkey(left,"Left")
    screen.onkey(up,"Up")
    screen.onkey(down,"Down")
    screen.onkey(changecolor,"e")
    screen.onkey(draw, "space")
    screen.onkey(save, "s")
    screen.onkey(editsize, "i")
    screen.listen()
    screen.update()

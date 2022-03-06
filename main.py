import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(myturtle=None):
  myturtle.up()
  for i in range(-360,361):
    y = math.sin(math.radians(i))
    myturtle.goto(i,y)
    myturtle.down()

def setupWindow(mywindow=None):
  turtle.setworldcoordinates(-360,-1,360,1)
  turtle.bgcolor("white")

def setupAxis(myturtle=None):
  myturtle.up()
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.goto(0,1)
  myturtle.up()
  myturtle.goto(360,0)
  myturtle.down()
  myturtle.goto(-360,0)

def drawCosineCurve(myturtle=None):
  myturtle.up()
  for i in range(-360,361):
    y = math.cos(math.radians(i))
    myturtle.goto(i,y)
    myturtle.down()

def drawTangentCurve(myturtle=None):
  myturtle.up()
  for i in range(-360,361):
    y = math.tan(math.radians(i))
    myturtle.goto(i,y)
    myturtle.down()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
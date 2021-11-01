import turtle
import random

colors = ["turquoise", "purple", "red", "blue", "orange", "yellow"]

myPencil = turtle.Turtle()
myPencil.color('turquoise')
myPencil.hideturtle()
myPencil.speed(0)

#canvas size
width=250
height=250

#tile size
size = 50



def drawSquare(x, y, size):
  myPencil.up()
  myPencil.color(random.choice(colors))
  myPencil.setposition(x - size / 2 + randomise(), y - size / 2 + randomise())
  myPencil.down()
  myPencil.setposition(x + size / 2 + randomise(), y - size / 2 + randomise())
  myPencil.setposition(x + size / 2 + randomise(), y + size / 2 + randomise())
  myPencil.setposition(x - size / 2 + randomise(), y + size / 2 + randomise())
  myPencil.setposition(x - size / 2 + randomise(), y - size / 2 + randomise())
  

def drawTile(x, y, size):
  for i in range(0,9):
    drawSquare(x, y, size)
    size -= random.randint(0,10)
  
def randomise(): 
  return (random.randint(0,10)/10 - 0.75) * 10

def draw():
  for x in range(0, width + size, size):
    for y in range(0, height + size, size):
      drawTile(x - 100, y - 100, size * 0.80)
       
    
    
draw()      

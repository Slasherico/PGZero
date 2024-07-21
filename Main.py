#Imports the PyGameZero Library
import pgzrun
from random import randint

#Sets the window parameters
WIDTH = 300
HEIGHT = 300

#Allow drawing on screen
def draw():
    r=255
    g=randint(10,255) #0
    b= 0 #randint(120,225)
    width = WIDTH
    height = HEIGHT-200
    for i in range(10):
        rect =  Rect((0,0),(width,height)) #"Rect" is predefined rectangle function
        rect.center = 150,150
        screen.draw.rect(rect,(r,g,b))
        width = width - 10
        height = height + 10
        r = r-10
        b = b+20

#Actually runs the code 
# starts the Pygame Zero event loop, which runs the game.
# (Always place at the send on code)
pgzrun.go()

#Line Comments
#Line 17 - Rect((x,y),(width, height))
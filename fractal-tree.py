from turtle import *

speed('fastest')

rt(-90)

# the acute angle between
# the base and branch of the Y
angle = 30

def y(sz, level): # function to plot a Y
    if level>0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255 // level, 0)

        fd(sz) # drawing the base

        rt(angle)

        y(0.8*sz, level-1)

        pencolor(0, 255 // level, 0)

        lt(2*angle)

        y(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)

y(80, 7)

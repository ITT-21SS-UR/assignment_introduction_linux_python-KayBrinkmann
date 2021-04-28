import math
import sys
from turtle import *

# get radius von command arguments and set to 100 if none were given
if len(sys.argv) < 2:
    print("no radius set, set to 100 by default")
    radius = 100
else:
    radius = int(sys.argv[1])

steve = Turtle()

# sets shape and color of turtle. Shape can be set to "circle" if the turtle is not "circly" enough
steve.shape("turtle")
steve.color("green")

# set radius of steve to the specified radius (ratio is 1 for 20 pixels: https://stackoverflow.com/questions/38103158/how-to-change-size-of-turtle)

steve.shapesize(2*radius/20, 2*radius/20, 1)
# moves steve as many pixels from the middle of the screen to the top as the specified radius
steve.goto(0, radius)

# moves steve in a circle with the specified radius around the middle of the screen
# source: https://3.141592653589793238462643383279502884197169399375105820974944592.eu/kreisumfang-berechnen/ (kind of sad but true^^) (very nice url btw)

while True:
    steve.right(1)
    steve.forward(2*math.pi*radius/360)

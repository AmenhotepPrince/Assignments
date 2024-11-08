# Import the CMU Graphics package:
from cmu_graphics import *

def slightlySerious(x):
    Circle(x,235,40, fill=gradient('yellow','orange'))
    Circle(x-15,230,5)
    Circle(x+15,230,5)
    Rect(x-20,245,40,10)

slightlySerious(200)
#When you comment out the function call it doesn't show anything.
#This is because although the function is already made, we have to call on it.

# Run program:
cmu_graphics.run()

from cmu_graphics import *
Rect(0,0,400,400,fill='blue')

#The face
Star(200,75,100,5,fill='lightBlue',border='black',borderWidth=2)
Circle(200,75,50, fill=gradient('yellow', 'orange'), border='black', borderWidth=2)
#eyes & nose
Oval(175,65,13,32)
Oval(225,65,13,32)
Line(200,62,207,75)
Line(207,75,200,77)
#smile
Line(175,110,225,110)
Line(165,95,235,95)
Line(175,110,165,95)
Line(225,110,235,95)
Polygon(175,110,225,110,235,95,165,95,fill=gradient('white','grey'))
Line(175,110,175,95)
Line(191.6,110,191.6,95)
Line(208.2,110,208.2,95)
Line(225,110,225,95)

cmu_graphics.run()

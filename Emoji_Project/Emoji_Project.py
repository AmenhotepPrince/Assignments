from cmu_graphics import *
#The face
Circle(200,75,50, fill=gradient('white', 'yellow'), border='black', borderWidth=1)
#eyes & nose
Oval(175,65,17,35)
Oval(225,65,17,35)
Line(200,62,207,75)
Line(207,75,200,77)
#smile:The lips
Line(175,110,225,110)
Line(165,95,235,95)
Line(175,110,165,95)
Line(225,110,235,95)
#smile:The teeth
Polygon(175,110,225,110,235,95,165,95,fill='white')
Line(175,110,175,95)
Line(191.6,110,191.6,95)
Line(208.2,110,208.2,95)
Line(225,110,225,95)
#smile:The 
cmu_graphics.run()

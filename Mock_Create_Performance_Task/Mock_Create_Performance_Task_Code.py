from cmu_graphics import *

Rect(0,0,1000,1000,fill='skyBlue')
Rect(0,230,1000,230,fill='Brown')

Body1 = Line(100,100,100,200,lineWidth=3)
Headbody1 = Circle(100,100,25,fill='Black')
Headbody2 = Circle(100,100,20,fill='skyBlue')
Legbody1 = Line(100,200,90,230,lineWidth=3)
Legbody2 = Line(100,200,110,230,lineWidth=3)
Arm1 = Line(100,125,90,175, lineWidth=3)
Arm2 = Line(100,125,110,175, lineWidth=3)

DraggableMan1 = Group(Body1,
                      Headbody1,
                      Headbody2,
                      Legbody1,
                      Legbody2,
                      Arm1,
                      Arm2
                      )
Body2 = Line(350,100,350,200,lineWidth=3)
Headbody3 = Circle(350,100,25,fill='Black')
Headbody4 = Circle(350,100,20,fill='skyBlue')
Legbody3 = Line(350,200,340,230,lineWidth=3)
Legbody4 = Line(350,200,360,230,lineWidth=3)
Arm3 = Line(350,125,340,175, lineWidth=3)
Arm4 = Line(350,125,360,175, lineWidth=3)

DraggableMan1 = Group(Body2,
                      Headbody3,
                      Headbody4,
                      Legbody3,
                      Legbody4,
                      Arm1,
                      Arm2
                      )
def onMouseDrag(mouseX, mouseY):
    
cmu_graphics.run()

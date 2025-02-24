from cmu_graphics import *
Rect(0,0,1000,1000,fill='skyBlue')
C=Circle(200,75,50, fill=gradient('yellow', 'orange'), border='black', borderWidth=3)
Ov1=Oval(175,65,13,32)
Ov2=Oval(225,65,13,32)
Li1=Line(200,62,207,75)
Li2=Line(207,75,200,77)
Li3=Line(225,95,175,95)

'''
#Line(212,65,238,65)
#Line(212,65,238,55)
#Line(212,65,238,75)

Line(200,62,207,75)
Line(207,75,200,77)
#smile

Polygon(175,110,225,110,235,95,165,95,fill=gradient('white','lightGrey',start='top'),border='black', borderWidth=2)
Line(175,110,175,95)
Line(191.6,110,191.6,95)
Line(208.2,110,208.2,95)
Line(225,110,225,95)
'''
Rect(200,300,50,100,fill='gold')
def onMouseDrag(mouseX,mouseY):
    C.centerX = mouseX
    C.centerY = mouseY
    C.radius = 50
    Ov1.centerX = mouseX-25
    Ov1.centerY = mouseY-10
    Ov2.centerX = mouseX+25
    Ov2.centerY = mouseY-10
    Li1.x1 = mouseX
    Li1.y1 = mouseY-13
    Li1.x2 = mouseX+7
    Li1.y2 = mouseY
    Li2.x1  = mouseX + 7
    Li2.y1 = mouseY
    Li2.x2 = mouseX
    Li2.y2 = mouseY + 2
    Li3.x1 = mouseX + 25
    Li3.y1 = mouseY + 20
    Li3.x2 = mouseX - 25
    Li3.y2 = mouseY + 20

cmu_graphics.run()

from graphics import *

win = None
def drawTarget(center, listc):
    global win
    
    win = GraphWin("Bull's Eye", 300, 300)
    for d, c in (listc):
            circle = Circle(Point(center[0], center[1]), (d/2))            
            circle.setFill(c)
            circle.draw(win)
    win.getMouse()



listc = [[80, color_rgb(0, 0, 255)], [60, color_rgb(255, 255, 0)], 
         [40, color_rgb(255, 0, 0)], [20, color_rgb(0, 0, 0)]]

Target = drawTarget((200, 200), listc)
    
    
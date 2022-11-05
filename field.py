from cmu_112_graphics import *

def appStarted(app):
    app.len=app.width
    app.bred=app.height

def redrawAll(app,canvas):
    canvas.create_rectangle(10,10,app.len-10,app.bred-10)

def main():
    runApp(width=400,height=400)

if(__name__=='__main__'):
    main()
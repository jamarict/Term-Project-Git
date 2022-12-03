# This demos using getpixel and putpixel

from cmu_112_graphics import *

def appStarted(app):
    app.image1 = app.loadImage("images/UnitImage.png")
    # now let's make a copy that only uses the red part of each rgb pixel:
    app.image1 = app.image1.convert('RGB')
    app.image2 = Image.new(mode='RGB', size=app.image1.size)
    for x in range(app.image2.width):
        for y in range(app.image2.height):
            r,g,b = app.image1.getpixel((x,y))
            if r > 190 and g > 190 and b > 190:
                continue
            elif r < 100 and g < 100 and b < 100:
                app.image2.putpixel((x,y),(r,g,b))
            else:
                app.image2.putpixel((x,y),(r,0,0))
           
            


def redrawAll(app, canvas):
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
    canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))

runApp(width=700, height=600)
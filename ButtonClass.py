class Button(object):
    def __init__(self, x, y , text, function, color):
        self.x = x
        self.y = y
        self.text = text
        self.f = function
        self.color = color

    def redraw(self, app, canvas):
        canvas.create_text(self.x, self.y, text = f"{self.text}", font = "FixedSys 20", fill = self.color)




class CircleButton(Button):
    def __init__(self, x, y, r, text, function, color):
        super().__init__(x, y, text, function, color)
        self.r = r
    
    def buttonPressed(self, app, event):
        d = ((self.x - event.x) ** 2 + (self.y - event.y) ** 2)**0.5
        if d <= self.r:
            self.functionCall(app)

    def functionCall(self, app):
        self.f(app)
    
    def redraw(self, app, canvas):
        x0, y0, x1, y1 = self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r
        canvas.create_oval(x0, y0, x1, y1, fill = "sienna3")
        super().redraw(app, canvas)

class RectangleButton(Button):
    def __init__(self, x, y, width, height, text, function, color):
        super().__init__(x, y, text, function, color)
        self.leftBound = self.x - width
        self.rightBound = self.x + width
        self.upperBound = self.y - height
        self.lowerBound = self.y + height
        print(self.leftBound, self.rightBound, self.upperBound, self.lowerBound)
    
    def buttonPressed(self, app, event):
        if (self.leftBound <= event.x <= self.rightBound) and (self.upperBound <= event.y <= self.lowerBound):
            self.f(app)
    
    def redraw(self, app, canvas):
        canvas.create_rectangle(self.leftBound, self.upperBound, self.rightBound, self.lowerBound, fill = "sienna3")
        super().redraw(app, canvas)

class ParameterButton(CircleButton):
    def __init__(self, x, y, r, text, function, number, color):
        super().__initII(x, y, r, text, function, color)
        self.numSet = number

    def functionCall(self, app):
        self.f(app, self.numSet)




 



def backToMain(app):
    app.mode = "setupMode"
def goToTitle(app):
    app.mode = "titleScreenMode" 
def goToHelp(app):
    app.mode = "helpScreenMode"
def goToSettings(app):
    app.mode = "settingsScreenMode"
def setParameter(app, number):
    app.playersNum = number

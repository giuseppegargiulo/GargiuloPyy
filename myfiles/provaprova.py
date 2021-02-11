from guizero import *

def clicked(): #lets create a function that will update the title of main window

    app.title = tbox1.value

app = App(title="Hello World")

tbox1 = TextBox(app) #create an empty textbox

but = PushButton(app, text='Enter text in box and press me', command=clicked)

app.display()

from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing\njhu?Hey!? How are you doing\njhu?Hey!? How are you doing\njhu?Hey!? How are you doing\njhu?Hey!? How are you doing\njhu?Hey!? How are you doing\njhu?")
label.pack()
root.mainloop()

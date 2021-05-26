import calendar
from tkinter import *

def printSomething():
    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(2021, 5)
    print(str)
    label = Label(root, text= str)
    label.pack()

root = Tk()

button = Button(root, text="Calendar", command=printSomething)
button.pack()
root.mainloop()



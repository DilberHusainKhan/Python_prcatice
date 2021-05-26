# import webbrowser module
import webbrowser
# import tkinker
from tkinter import *
# Creating root
root = Tk()
# setting GUI Tittle
root.title("Web Browser")
# setting GUI size
root.geometry("500x500")
# function to open webtyx
def webtyx():
    webbrowser.open("www.webtyx.com")
# function to open google
def google():
    webbrowser.open("www.google.com")
# button to call webtyx
webtyx = Button(root, text= "Visit webtyx", command= webtyx).pack(pady=20)
# button to call google
google = Button(root, text= "Open Google", command= google).pack(pady=20)

root.mainloop()



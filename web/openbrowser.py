from tkinter import *
import webbrowser


def google():
    webbrowser.open("www.google.com")


root = Tk( )

root.title("Abrir Browser")
root.geometry('300x200')

mygoogle = Button(root, text="Abrir Google", command=google).pack(pady=20)
root.mainloop()

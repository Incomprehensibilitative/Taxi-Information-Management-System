"""" Listing function """
from tkinter import *
from tkinter.ttk import *
from doctest import master

root = Tk()
#width= root.winfo_screenwidth()
#height= root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))
root.geometry("1000x1000")

def NewWindow():
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("200x200")

btn1 = Button(root, text = "Customer", command = NewWindow).place(x = 30, y = 100)
btn2 = Button(root, text = "Driver", command = NewWindow).place(x = 30, y = 150)
btn3 = Button(root, text = "Invoice", command = NewWindow).place(x = 30, y = 200)
btn4 = Button(root, text = "Vehicle", command = NewWindow).place(x = 30, y = 250)
btn5 = Button(root, text = "Validation", command = NewWindow).place(x = 30, y = 300)
btn6 = Button(root, text = "Feedback", command = NewWindow).place(x = 30, y = 350)

#def print_driver():
#    pass

#"""" Print menu """

#def print_menu():
    # using Tkinter
#    pass
root.mainloop()
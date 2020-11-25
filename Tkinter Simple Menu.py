#Tkinter Menu Sederhana
#Efron Paduansi
#04TPLP002 STMIK Eresha 19202

from Tkinter import *
from tkFileDialog import askopenfilename

def NewFile():
    print "New File!"
def OpenFile():
    name = askopenfilename()
def About():
    print "This is a simple example of a menu"

root = Tk()
root.title("Simple Menu built by Efronius")
menu =Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)

mainloop()

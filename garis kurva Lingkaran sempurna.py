#garis kurva.py
#by efronius
#>>>>>>>>>>>>
from Tkinter import *
root = Tk()
root.title('Garis Kurva')
cw = 300 # lebar kanvas
ch = 300 # lebar kanvas
canvas_1 = Canvas(root, width=cw, height=ch, background="purple")
canvas_1.grid(row=0, column=1)
x1 = 10
y1 = 10
x2 = 200
y2 = 200

canvas_1.create_oval(x1,y1, x2,y2, width=2 )
root.mainloop()
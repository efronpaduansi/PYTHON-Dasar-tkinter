#garis kurva lurus.py
#by efronius Paduansi
#>>>>>>>>>>>>
from tkinter import *
root = Tk()
root.title('Garis Horizontal')
cw = 300 # lebar kanvas
ch = 200 # lebar kanvas
canvas_1 = Canvas(root, width=cw, height=ch, background="purple")
canvas_1.grid(row=0, column=1)
x1 = 10
y1 = 10
x2 = 10
y2 = 150
canvas_1.create_line(x1,y1, x2,y2, smooth='true')
root.mainloop()
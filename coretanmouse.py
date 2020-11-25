#Program Coretan Kursor with python
#Nama : Efronius Paduansi
#Kelas : 04TPLP002
from Tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event):
    python_green = "#476042"
    x1, y1 = ( event.x - 1), ( event.y -1)
    x2, y2 = ( event.x + 1), ( event.y +1)
    w.create_oval(x1, y1, x2, y2, fill = python_green)
master = Tk()
master.title("Drag Mouse untuk Menggambar")
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind("B1-Motion", paint)
message = Label(master, text ="Klik dan Gerakan Mouse Untuk menggambar")
message.pack( side = BOTTOM )

mainloop()

#Menghubungkan dua garis dengan Python
#Created By : Efron Paduansi
#04TPLP002 STMIK ERESHA

from tkinter import *
root = Tk()
root.title('Garis Horizontal & Vertikal by Efron Paduansi')
cvsw = 400
cvsh = 400
Canvas_1 = Canvas(root, width=cvsw, height=cvsh, background= "purple")
Canvas_1.grid(row=0, column=1)
x1 = 150
y1 = 10
x2 = 150
y2 = 150
x3 = 10
y3 = 150 

Canvas_1.create_line(x1,y1, x2,y2, x3,y3)
root.mainloop()

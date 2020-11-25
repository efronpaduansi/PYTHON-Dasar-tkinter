#Menampilkan Message with Python
#Created By Efron Paduansi
#04TPLP002

from Tkinter import *
from TkMessageBox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Note yet implemented')
    else:
        showinfo('No', 'Quit has been canceled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()

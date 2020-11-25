#Program TKinter Form with Python
#Nama : Efronius Paduansi
#Kelas : 04TPLP002

from Tkinter import *
daftar = Tk()
daftar.title('tkinter by Efron Paduansi')

daftar.geometry("400x250") 


nama = Label(daftar, text = "Nama").place(x = 10, y = 50)
alamat = Label(daftar, text = "Alamat").place(x = 10, y = 90)
telp =Label(daftar, text ="No. Telepon").place(x = 10, y = 130)

sbmitbtn = Button(daftar, text = "Submit", background = "purple",
 activebackground = "green", 
 activeforeground = "black", font = "Verdana 16 bold").place(x = 30, y = 170)

e1 = Entry(daftar).place(x = 80, y = 50)
e2 = Entry(daftar).place(x = 80, y = 90)
e3 = Entry(daftar).place(x = 80, y = 130)

daftar.mainloop()

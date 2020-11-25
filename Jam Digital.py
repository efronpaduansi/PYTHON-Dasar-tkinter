#Progam Jam Digital Python
#Efronius Paduansi
#04TPLP002 19202

from tkinter import *

#Memangil module time (untuk mengakses waktu saat ini)
import time 
class JamDigital :
 """ Kelas Jam Digital"""

 def __init__(self, parent, title):
  self.parent = parent

  self.parent.title(title)
  self.parent.protocol ("WM_DELETE_WINDOW" , self.onTutup)
  self.parent.resizable(False, False)

  #buat variabel string untuk teks jam
  self.teksJam = StringVar ()

  self.aturKomponen()
  #melakukan looping untuk tampilan jam
  self.update()

 def aturKomponen (self):
  mainFrame = Frame (self.parent, bd=10)
  mainFrame.pack(fill=BOTH, expand=YES)

  #teks jam dibuat dengan komponen label, yang bisa dirubah
  #setiap waktu.

  self.lblJam = Label(mainFrame, textvariable=self.teksJam,
   font=('Times New Roman ', 40))
  self.lblJam.pack(expand=YES)

  self.lblInfo = Label(mainFrame, text="STMIK ERESHA BY EFRON PADUANSI",
   fg='black')
  self.lblInfo.pack(side=TOP, pady=5)

 def update (self):
  # strftime() berfungsi untuk merubah data waktu secara lokal
  # menjadi bentuk string yang kita ingkan.
  datJam = time.strftime("%H:%M:%S", time.localtime())

  # mengubah teks jam sesuai dengan waktu saat ini
  self .teksJam.set(datJam)

  # perubahan teks jam dalam selang waktu 1 detik (1000 ms)
  self.timer = self.parent.after(1000, self.update)

 def onTutup(self, event=None):
  self.parent.dedtroy()

if __name__ == '__main__':
 root = Tk()

 app = JamDigital(root, "Jam Digital")

 root.mainloop()
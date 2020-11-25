#Program Dialog Standar with Python
#Efronius Paduansi
#04TPLP002

from Tkinter import *
import tkMessageBox as mb 

class DemoDialog:
    def __init__(self, induk, judul):
        self.induk = induk

        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
        self.induk.resizable(False, False)

        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)

        box = Frame(mainFrame, bd=20)
        box.pack(fill=BOTH, expand=YES)

        btnInfo = Button(box, text='Dialog Info',
                command=self.onKlikInfo)
        btnInfo.pack(side=LEFT)

        btnWarning = Button(box, text='Dialog Warning',
                    command=self.onKlikWarning)
        btnWarning.pack(side=LEFT)

        btnError = Button(box, text='Dialog Error',
                    command=self.onKlikError)
        btnError.pack(side=LEFT)

        btnKeluar = Button(box, text='Keluar',
                    command=self.tutup)
        btnKeluar.pack(side=LEFT, padx=5)

    def onKlikInfo(self, event=None):
        mb.showinfo("Info Penting !", "Ini adalah Dialog Show Info")

    def onKlikError(self, event=None):
        mb.showerror("Kesalahan Fatal!", "Ini adalah Dialog Show Error")

    def onKlikWarning(self, event=None):
        mb.showwarning("Peringatan!", "Ini adalah Dialog Show Warning")

    def tutup(self, event=None):
        self.induk.destroy()
if __name__ =='__main__':
    root = Tk()

    app = DemoDialog(root, ":: Demo Dialog ::")

    root.mainloop()
        
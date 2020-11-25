#Ruang Ketik with Python
#Built with : Efron Paduansi 04TPLP002 STMIK Eresha 19202

from tkinter import *
class scrollTxtArea:
    def __init__(self,root):
        frame=Frame(root)
        frame.pack()
        self.textPad(frame)
        return
    def textPad(self,frame):
        #atur bingkai dan ruang tulisan
        textPad=Frame(frame)
        self.text=Text(textPad, height=3, width=20,)

        #atur scroll bar pada ruang tulisan
        scroll=Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)

        #eksekusi Program
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        textPad.pack(side=TOP)
        return
def main():
    root =Tk()
    foo=scrollTxtArea(root)
    root.title('Ruang Ketik-Efron Paduansi')
    root.mainloop()
main()

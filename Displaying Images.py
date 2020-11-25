#Programming With Python
#Displying Images in Python
#by : Efron Paduansi
#04TPLP002 STMIK Eresha 19202

import time
try:
    #Python version 2
    import Tkinter as tk 
except ImportError:
    #Python Version 3
    import tkinter as tk 

images_files =[
    #Displaying 3 Imgages
    'image1.png',
    'image2.png',
    'image3.png',

]
root = tk.Tk()
label = tk.Label(root)
label.pack()
delay =3.2 #Long time to Displaying Images
for image in images_files:
    image_object = tk.PhotoImage(file=image)
    label.config(image=image_object)
    root.title(image)
    root.update()
    time.sleep(delay)
root.mainloop()



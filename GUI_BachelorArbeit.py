from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox as msg
import os
import cv2
import numpy as np

"""

import os


class MainWindows(Frame):
    def __init__(self):

        super().__init__()
        self.setUI()

    def setUI(self):
        self.master.title("Foto Galery")
        self.pack(fill=BOTH, expand=True)
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        subMenu = Menu(menubar)  # add a submenu into my menu
        menubar.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New_Project")
        subMenu.add_command(label="New")
        subMenu = Menu(menubar)
        menubar.add_cascade(label="Help", menu=subMenu)
        subMenu.add_command(label="Choose Fotos ",  command=self.display_fotos)
        subMenu.add_command(label="Close project")
        subMenu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=subMenu)
        subMenu.add_command(label="delete")
        subMenu.add_command(label="save")


        button1 = Button(text="Load", width=10)
        button1.pack(padx=4)




        abtn = Button(self, text="Load", width=10,
                      command=self.display_fotos)
        abtn.grid(row=1, column=0,pady=10,padx=3)
        #abtn.pack(pady = 10, padx = 10)

        abtn1 = Button(self, text="Save", width=5,
                      command=self.display_fotos)
        abtn1.grid(row=1, column=1, pady=10, padx=4)

        cbtn = Button(self, text="Close", width=10, command=self.newWindows)
        cbtn.grid(row=1, column=3, pady=4)

        area = Frame(self, relief=RAISED, borderwidth=1)
        area.grid(row=3, column=0, columnspan=2, rowspan=4,
                  padx=5, sticky=E+W+S+N, pady=10)





        hbtn = Button(self, text="Help", width=10)
        hbtn.grid(row=5, column=0, padx=5, pady=10)

        obtn = Button(self, text="OK", width=10)
        obtn.grid(row=5, column=3, pady=10)


    def browse_Module(self):

        filename = filedialog.askdirectory()
        return filename





    def set_fotos(self, PILimagesfotos):
        xrichtung, yrichtung = 20, 20
        i = 0
        for foto in PILimagesfotos:
            resize_foto = self.resize_fotos(foto)
            labelfoto = Label(area)
            photo = ImageTk.PhotoImage(resize_foto)
            labelfoto.image = photo
            labelfoto.place(x=xrichtung, y=yrichtung)
            labelfoto.config(image=photo)
            labelfoto.bind('<Button-1>', lambda event,
                           fotoname=self.PILimagesfotos[0]: self.buttonClick(event, fotoname))
            labelfoto.bind("<Enter>", lambda event,
                           label=labelfoto: self.on_enter(event, label))
            labelfoto.bind("<Leave>", lambda event,
                           label=labelfoto: self.on_leave)

            xrichtung += 120
            i += 1
            if(i % 4 == 0):
                yrichtung += 120
                xrichtung = 0


    def resize_fotos(self, image):

        width, height = 100, 100
        resize_image = image.resize((width, height), Image.ANTIALIAS)
        return resize_image

    def display_fotos(self):
        filename = self.browse_Module()
        src_files = os.listdir(filename)

        for file in src_files:
            extension = os.path.splitext(file)[1]
            if extension == ".jpg":
                self.imagesfotos.append(file)
                print(self.imagesfotos)
                img = Image.open(filename + "/" + file)
                self.PILimagesfotos.append(img)

            elif extension == ".png":
                self.imagesfotos.append(file)
                img = Image.open(filename + "/" + file)
                self.PILimagesfotos.append(img)

        if len(self.PILimagesfotos) == 0:
            msg.showerror("MessageError", "File Empty")
        else:
            self.set_fotos(self.PILimagesfotos)

    def newWindows(self):
        newWindow = Toplevel(self.master)
        self.app = secondWindows(self.newWindows)

    def buttonClick(self, event, fotoname):
        print(fotoname)

    def on_enter(self, event, label):
        label.configure(text="Hello world")

    def on_leave(self, enter, label):
        label.configure(text="")


class secondWindows(Frame):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        quitbutton = Button(self.frame, text="Quit", command=self.closeWindow)
        quitbutton.pack()
        self.frame.pack()

    def closeWindow(self):
        self.master.destroy()


def main():
    root = Tk()
    app = MainWindows()
    root.geometry("500x500+300+300")
    # root.resizable(0,0)  to have a not resizable windows
    root.mainloop()


if __name__ == "__main__":
    main()
"""

#import tkinter as tk

"""


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.setUI()
        self.frame.pack(fill=BOTH, expand=True)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Demo2(self.newWindow)



    def setUI(self):
        self.master.title("Foto Galery")
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        subMenu = Menu(menubar)  # add a submenu into my menu
        menubar.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New_Project")
        subMenu.add_command(label="New")
        subMenu = Menu(menubar)
        menubar.add_cascade(label="Help", menu=subMenu)
        #  subMenu.add_command(label="Choose Fotos ", command=self.display_fotos)
        subMenu.add_command(label="Close project")
        subMenu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=subMenu)
        subMenu.add_command(label="delete")
        subMenu.add_command(label="save")


        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)




class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = Tk()
    root.geometry("600x400+400+200")
    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()

"""
"""

from tkinter import *

root = Tk()

buttonA0 = Button(root,  text = 'Hi')
buttonB0 = Button(root, text = 'Bye')
buttonC0 = Button(root, text = 'Option 0')
buttonC1 = Button(root, text = 'Option 1')
buttonC2 = Button(root, text = 'Option 2')
buttonC3 = Button(root, text = 'Option 3')
buttonC4 = Button(root, text = 'Option 4')

buttonA0.grid(column = 0, row = 0, sticky = NE+SW)
buttonB0.grid(column = 0, row = 5, sticky = E+W)
buttonC0.grid(column = 1, row = 0)
buttonC1.grid(column = 1, row = 1)
buttonC2.grid(column = 1, row = 2)
buttonC3.grid(column = 1, row = 3)
buttonC4.grid(column = 1, row = 4)

root.mainloop()
"""

"""

:return: 
""""""
 
 self.button1 = tk.Button(self.frame, text="Load", width=12)

 self.button2 = tk.Button(self.frame, text='Save', width=12, command=self.new_window)

  #self.button3 = tk.Button(self.frame, text='Processing ', width=10, command=self.new_window)

 self.text1 = Label(self.frame, text=" x = ", width=1)
 self.text2 = Label(self.frame, text="y = ")
 self.text3 = Label(self.frame, text=" z = ")
 self.entry1 = Entry(self.frame, width=6)
 self.entry2 = Entry(self.frame, width=6)
 self.entry3 = Entry(self.frame, width=6)
 L = ['Pizza Diavolo', 'Pizza Margherita', 'Pizza quattro stagioni']
 self.vS = tk.StringVar(self.frame)
 self.vS.set(L[2])
 self.oS = tk.OptionMenu(self.frame, self.vS, *L)
 # self.oS.place(x=20, y=20, width=200)




 self.button1.grid(column=0, row=0, sticky=W, pady=20, padx=10)
 self.button2.grid(column=1, row=0, pady=10, padx=10)
# self.button3.grid(column=0, row=1)
 self.text1.place(x = 20, y = 30)
 self.text2.grid(column=0, row=2, pady=10, padx=10, sticky=W)
 self.text3.grid(column=0, row=3, pady=10, padx=10, sticky=W)
 self.entry1.place(x= 40, y=30)
 self.entry2.grid(column=1, row=2)
 self.entry3.grid(column=1, row=3)
 self.oS.grid(column=5, row=0, sticky=E + W)
"""

from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        self.master.title("Review")
        self.pack(fill=BOTH, expand=True)

        self.frame1 = Frame(self)
        self.frame1.pack(fill=X)

        btn1 = Button(self.frame1, text="Load", width=6,command=self.browse_Module)
        btn1.pack(side=LEFT, padx=20, pady=10)

       # btn2 = Button(self.frame1, text="Save", width=6)
        #btn2.pack(side=LEFT, padx=50, pady=10,expand=True)

        L = ['Processing','full ahe', 'intensiv normalization', 'deconvolution']
        self.vS = StringVar(self.frame1)
        self.vS.set(L[0])
        self.oS = OptionMenu(self.frame1, self.vS, *L)
        self.oS.pack(side=RIGHT, padx=80, pady=10)



        self.frame2 = Frame(self)
        self.frame2.pack(fill=X)

        lbl2 = Label(self.frame2, text="X =", width=2)
        lbl2.pack(side=LEFT,anchor=N, padx=2, pady=5)

        entry1 = Entry(self.frame2,width=8)
        entry1.pack(side=LEFT,pady=5)

        self.frame3 = Frame(self)
        self.frame3.pack(fill=X)

        lbl3 = Label(self.frame3, text="Y =", width=2)
        lbl3.pack(side=LEFT, anchor=N, padx=2, pady=5)

        entry2 = Entry(self.frame3,width=8)
        entry2.pack(side=LEFT, pady=5)

        self.frame4 = Frame(self)
        self.frame4.pack(fill=X)

        lbl4 = Label(self.frame4, text="Z =", width=2)
        lbl4.pack(side=LEFT, anchor=N, padx=2, pady=5)

        entry3 = Entry(self.frame4,width=8)
        entry3.pack(side=LEFT, pady=5)

        self.frame5 = Frame(self, relief=RAISED, borderwidth=1)
        self.frame5.pack(fill=BOTH,expand=True)

        self.frame6 = Frame(self)
        self.frame6.pack(fill=X)
        s = Style()
        s.configure("TProgressbar", thickness=100)
        mpb = Progressbar(self.frame6, orient="horizontal", length=200, mode="determinate",style="TProgressbar")
        mpb.pack(fill=X,expand=True,pady=10,padx=100)
        mpb["maximum"] = 100
        mpb["value"] = 50


        startButton = Button(self,text="Start", state=DISABLED)
        startButton.pack(side=RIGHT, padx=10, pady=10)
        saveButton = Button(self, text="Save")
        saveButton.pack(side=LEFT,padx=10,pady=10)




    def browse_Module(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"),("TIFF files", "*.tif"), ("all files", "*.*")))
        #filename = filedialog.askdirectory()
        extension = os.path.splitext(filename)[1]
        print(extension)
        if extension == ".jpg" or extension == ".png" or extension == ".tif":
            print(filename)
        else:
            msg.showerror("FileError", "The file Format is not supported")

        #resizedImage = self.resize_fotos(filename)
        #labelfoto= ImageTk.PhotoImage(resizedImage)
        #label1 = Label(self.frame5,image=labelfoto)
        #label1.image = labelfoto
        #print("width = "+self.frame5.winfo_width())
        #print("height = "+ self.frame5.winfo_height())
       # label1.pack(padx=10,pady=10,expand=True)
        return filename

    """
     
    def set_fotos(self, PILimagesfotos):
        xrichtung, yrichtung = 20, 20
        i = 0
        for foto in PILimagesfotos:
            resize_foto = self.resize_fotos(foto)
            labelfoto = Label(area)
            photo = ImageTk.PhotoImage(resize_foto)
            labelfoto.image = photo
            labelfoto.place(x=xrichtung, y=yrichtung)
            labelfoto.config(image=photo)
            labelfoto.bind('<Button-1>', lambda event,
                                                fotoname=self.PILimagesfotos[0]: self.buttonClick(event, fotoname))
            labelfoto.bind("<Enter>", lambda event,
                                             label=labelfoto: self.on_enter(event, label))
            labelfoto.bind("<Leave>", lambda event,
                                             label=labelfoto: self.on_leave)

            xrichtung += 120
            i += 1
            if (i % 4 == 0):
                yrichtung += 120
                xrichtung = 0
    """
    def resize_fotos(self, filename):
        self.update()
        width = self.frame5.winfo_width()
        height = self.frame5.winfo_height()
        img = cv2.imread(filename)
        resize_image = cv2.resize(img, dsize=(width, height), interpolation=cv2.INTER_CUBIC)
        return resize_image

    def display_fotos(self):
        pass


       #filename = self.browse_Module()


    """
    
    def newWindows(self):
        newWindow = Toplevel(self.master)
        self.app = secondWindows(self.newWindows)

    def buttonClick(self, event, fotoname):
        print(fotoname)

    def on_enter(self, event, label):
        label.configure(text="Hello world")

    def on_leave(self, enter, label):
        label.configure(text="")
"""

def main():
    root = Tk()
    root.geometry("600x600+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
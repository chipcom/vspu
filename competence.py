#!/usr/local/bin/python
"""
Tk8.0 style main window menus
menu/tool bars packed before middle, fill=X (pack first=clip last);
adds photo menu entries; see also: add_checkbutton, add_radiobutton
"""

from tkinter import *                              # get widget classes
from tkinter.messagebox import *                   # get standard dialogs

class NewWindow():
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.createWindow()

def createWindow(self):
        L = Label(self, text='Конструктор компетенций')
        L.config(relief=SUNKEN, width=40, height=10, bg='white')
        L.pack(expand=YES, fill=BOTH)


class NewMenuDemo(Frame):                          # an extended frame
    def __init__(self, parent=None):               # attach to top-level?
        Frame.__init__(self, parent)               # do superclass init
        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()                       # attach frames/widgets
        self.master.title("Конструктор компетенций")    # set window-manager info
        self.master.iconname("tkpython")           # label when iconified

    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolBar()
        L = Label(self, text='Конструктор компетенций Demo')
        L.config(relief=SUNKEN, width=40, height=10, bg='white')
        L.pack(expand=YES, fill=BOTH)

    def makeToolBar(self):
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Quit',  command=self.quit    ).pack(side=RIGHT)
        Button(toolbar, text='Hello', command=self.greeting).pack(side=LEFT)

    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)    # master=top-level window
        self.fileMenu()
        self.editMenu()
        # self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Открыть...', command=self.notdone)
        pulldown.add_command(label='Выход',    command=self.quit)
        self.menubar.add_cascade(label='Файл', underline=0, menu=pulldown)

    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Программы',   command=NewWindow)
        pulldown.add_separator()

        submenu = Menu(pulldown, tearoff=True)
        submenu.add_command(label='Универсальные', command=self.notdone, underline=0)
        submenu.add_command(label='Общепрофессиональные', command=self.notdone,  underline=0)
        pulldown.add_cascade(label='Компетенции',   menu=submenu,     underline=0)

        # pulldown.add_command(label='Spam',    command=self.greeting)
        # pulldown.add_command(label='Delete',  command=self.greeting)

        # pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Справочники', underline=0, menu=pulldown)


    # def imageMenu(self):
    #     photoFiles = ('ora-lp4e.gif', 'pythonPowered.gif', 'python_conf_ora.gif')
    #     pulldown = Menu(self.menubar)
    #     self.photoObjs = []
    #     for file in photoFiles:
    #         img = PhotoImage(file='../gifs/' + file)
    #         pulldown.add_command(image=img, command=self.notdone)
    #         self.photoObjs.append(img)   # keep a reference
    #     self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)

    def greeting(self):
        showinfo('приветствие', 'Добрый день')
    def notdone(self):
        showerror('Не реализовано', 'Пока не реализовано')
    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)

if __name__ == '__main__':
    NewMenuDemo().mainloop()  # if I'm run as a script

import sys
from tkinter import *

def quit():
    print("Hello, I must be going...")
    sys.exit()

# root =Tk()
# widget =  tkinter.Label(None, text='Hello GUI world!')
# widget.pack(expand=YES,fill=BOTH)
# widget.pack(expand=YES,fill=BOTH)
# widget =  Label()
# widget1 =  Label()
# widget1['text'] = 'Good bay!'
# widget.config(text='Hello GUI world!')
# widget.pack(side=TOP,expand=YES,fill=BOTH)
widget = Button(None, text="Hello event world", command=quit)
widget.pack(side=LEFT,expand=YES)
# root.title('gui1g.py')

# root.mainloop()
widget.mainloop()
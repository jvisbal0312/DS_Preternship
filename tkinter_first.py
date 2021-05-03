#!/usr/bin/env python3
from tkinter import *
import tkinter.font as tkFont
import boolean

# Feel free to change colors(see TkinterColorCharts.png)
# Variables
window = Tk()
modeChange = StringVar()
modeInt = IntVar()
    
# Configurations 
window.title("animated waveform")
window.geometry('500x500')
window.minsize(500,500)
window.maxsize(500,500)
window.config(bg="white smoke")

# Dark mode OR Light mode
modeChange.set("dark mode")
modeInt.set(1)
def change_mode():
    if modeInt.get() == 1:
        modeChange.set("light mode")
        window.config(bg="gray35")
        modeInt.set(0)
    else:
        modeChange.set("dark mode")
        window.config(bg="white smoke")
        modeInt.set(1)
mode = Button(window,command=change_mode,activebackground = "LightSkyBlue1",font=("consolas",11),textvariable = modeChange,width=10,bd=0.15,bg="SlateGray1",relief="flat",justify=CENTER).place(x=21,y=20)

# Labels
# Simple Evaluation: input two expression strings, output whether they are equal to each other
simpleEvaluation = Label(window,font=("consolas",11),text = "simple evaluation",width=20,bd=0.2,relief="flat").place(x=20,y=70)
input1 = Label(window,font=("consolas",11),text = "input1",width=9,bd=0.2,bg="SlateGray1",relief="flat").place(x=20,y=100)
input2 = Label(window,font=("consolas",11),text = "input2",width=9,bd=0.2,bg="SlateGray1",relief="flat").place(x=20,y=130)

# Simplification: when clicked, display a simplied expression
simplified = Button(window,command=simplification)
def simplification():
    '''
    '''

# Kmap (optional): when clicked, display Kmaps of the expressions
kmap = Button(window,command=k_map)
def k_map():
    '''
    '''

window.mainloop()

if __name__ == '__main__':
    window.mainloop()
#!/usr/bin/env python3

from tkinter import *
import tkinter.font as tkFont
import boolean

algebra = boolean.BooleanAlgebra()

# Feel free to change colors(see TkinterColorCharts.png)
# Variables
window = Tk()
modeChange = StringVar()
modeInt = IntVar()
inputExpr1 = StringVar()
inputExpr2 = StringVar()
evalD = StringVar()
    
# Configurations 
window.title("animated waveform")
window.geometry('700x700')
window.minsize(700,700)
window.maxsize(700,700)
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
mode = Button(window,
                command=change_mode,
                activebackground = "LightSkyBlue1",
                font=("consolas",11),
                textvariable = modeChange,
                width=10,
                bd=0.15,
                bg="SlateGray1",
                relief="flat",
                justify=CENTER).place(x=21,y=20)

# Labels
# Simple Evaluation: input two expression strings, output whether they are equal to each other
simpleEvaluation = Label(window,font=("consolas",11),text = "simple evaluation",width=20,bd=0.2,relief="flat").place(x=20,y=70)

def sim_eval():
    expr1 = algebra.parse(inputExpr1.get())
    expr2 = algebra.parse(inputExpr2.get())
    if expr1 == expr2:
        evalD.set("The input expressions are equal.")
    else:
        evalD.set("The input expressions are not equal.")
input1 = Label(window,
                font=("consolas",11),
                text = "input1",
                width=11,
                bd=0.2,
                bg="SlateGray1",
                relief="flat").place(x=20,y=100)
entry1 = Entry(window,
                font=("consolas bold",11),
                justify=LEFT,
                relief=SUNKEN,
                textvariable=inputExpr1).place(x=150,y=100)
input2 = Label(window,
                font=("consolas",11),
                text = "input2",
                width=11,
                bd=0.2,
                bg="SlateGray1",
                relief="flat").place(x=20,y=130)
entry2 = Entry(window,
                font=("consolas bold",11),
                justify=LEFT,
                relief=SUNKEN,
                textvariable=inputExpr2).place(x=150,y=130)
simpEva = Button(window,
                    command=lambda:sim_eval(),
                    activebackground = "LightSkyBlue1",
                    font=("consolas italic",11),
                    text="Evaluate!",
                    width=11,
                    bd=0.1,
                    bg="SlateGray1",
                    relief="flat",
                    justify=CENTER).place(x=20,y=160)
evalDisplay = Label(window,
                    font=("consolas",11),
                    textvariable=evalD,
                    width=43,
                    bd=4,
                    justify=LEFT,
                    relief="flat").place(x=150,y=160)

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
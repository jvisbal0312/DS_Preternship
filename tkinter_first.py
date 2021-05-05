#!/usr/bin/env python3

from tkinter import *
import tkinter.font as tkFont
import time

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
simpOutput1 = StringVar()
simpOutput2 = StringVar()
    
# Configurations 
window.title("animated waveform")
window.geometry('700x700')
window.resizable(False,False)
window.config(bg="white smoke")

# Dark mode OR Light mode
modeChange.set("dark mode")
modeInt.set(1)
def change_mode():
    if modeInt.get() == 1:
        modeChange.set("light mode")
        window.config(bg="gray30")
        canvas.config(bg="gray35")
        modeInt.set(0)
    else:
        modeChange.set("dark mode")
        window.config(bg="white smoke")
        canvas.config(bg="azure")
        modeInt.set(1)
mode = Button(window,
              command=change_mode,
              activebackground = "LightSkyBlue1",
              font=("consolas",11),
              textvariable = modeChange,
              width=11,
              bd=0.15,
              bg="SlateGray1",
              relief="flat",
              justify=CENTER).place(x=21,y=530)

# Simple Evaluation: input two expression strings, output whether they are equal to each other

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
               relief="flat").place(x=20,y=570)
entry1 = Entry(window,
              font=("consolas bold",11),
              justify=LEFT,
              relief=SUNKEN,
              textvariable=inputExpr1).place(x=150,y=570)
input2 = Label(window,
               font=("consolas",11),
               text = "input2",
               width=11,
               bd=0.2,
               bg="SlateGray1",
               relief="flat").place(x=20,y=600)
entry2 = Entry(window,
              font=("consolas bold",11),
              justify=LEFT,
              relief=SUNKEN,
              textvariable=inputExpr2).place(x=150,y=600)
simpEva = Button(window,
                 command=sim_eval,
                 activebackground = "LightSkyBlue1",
                 font=("consolas italic",11),
                 text="Evaluate!",
                 width=11,
                 bd=0.1,
                 bg="SlateGray1",
                 relief="flat",
                 justify=CENTER).place(x=20,y=640)
evalDisplay = Label(window,
               font=("consolas",11),
               textvariable=evalD,
               width=40,
               bd=4,
               justify=LEFT,
               relief="flat").place(x=150,y=640)

# Evaluation animation: when clicked, display a waveform of the two input expressions
animation = Button(window,
                 command=Graph,
                 activebackground = "LightSkyBlue1",
                 font=("consolas italic",11),
                 text="Generate waveform!",
                 width=20,
                 bd=0.1,
                 bg="SlateGray1",
                 relief="flat",
                 justify=CENTER).place(x=500,y=640)
def Graph(step=0.001):
    '''
    Delete later
    # Parameters for graph: input expression 1, input expression 2, dark or light mode
    # Get symbols
    # Generate the waveform of the the two expressions 
    for instance e1 = x&y, e2 = x|y
        1s  2s  3s  4s
    x   0   1   1   0
    y   0   0   1   1
    e1  0   0   1   0
    e2  0   1   1   1
    # End of animation

    '''
    canvas.create_line(0,0,200,200,fill='black')
    canvas.update()
canvas = Canvas(window,
                width=700,
                height=500,
                bg="azure",
                relief=SUNKEN)
canvas.pack()
canvas.bind('<1>',change_mode)

# Simplification: when clicked, display a simplied expression
def simplify_one():
    expr1 = algebra.parse(inputExpr1.get())
    simpOutput1.set(expr1.simplify())
def simplify_two():
    expr2 = algebra.parse(inputExpr2.get())
    simpOutput2.set(expr2.simplify())
simplify1 = Button(window,
                 command=simplify_one,
                 activebackground = "LightSkyBlue1",
                 font=("consolas italic",10),
                 text="Simplify!",
                 width=10,
                 bg="SlateGray1",
                 relief="flat",
                 justify=CENTER).place(x=330,y=570)
simplify2 = Button(window,
                 command=simplify_two,
                 activebackground = "LightSkyBlue1",
                 font=("consolas italic",10),
                 text="Simplify!",
                 width=10,
                 bg="SlateGray1",
                 relief="flat",
                 justify=CENTER).place(x=330,y=600)
simplifyOutput1 = Label(window,
                   font=("consolas",11),
                   textvariable = simpOutput1,
                   width=15,
                   bd=0.2,
                   relief="flat").place(x=450,y=570)
simplifyOutput2 = Label(window,
                   font=("consolas",11),
                   textvariable = simpOutput2,
                   width=15,
                   bd=0.2,
                   relief="flat").place(x=450,y=600)


window.mainloop()

if __name__ == '__main__':
    window.mainloop()
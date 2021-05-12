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
# Instructions
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
def parseToZero(expr,integer=0):
    string = []
    for i in expr:
        if i.isalpha():
            string.append(i)
    string = list(set(string))
    for i in expr:
        if i == string[integer]:
            expr = expr.replace(i,"0")
    return expr
def parseToOne(expr,integer=0):
    string = []
    for i in expr:
        if i.isalpha():
            string.append(i)
    string = list(set(string))
    for i in expr:
        if i == string[integer]:
            expr = expr.replace(i,"1")
    return expr

def lineDisplay(t1,t2,TempExpr1,TempExpr2,seg=2,x):
# def lineDisplay(t1,t2,TempExpr,seg=2):
	
	
    startX = int(40 + (seg-1)*160)
    endX = int(40 + (seg)*160)
	startY = int(75+x(150))
	endY = int(150+x(150))
	
    # Specify the starting_x and ending_x
    if t1 == 0: # prev1 = 0
        if type(TempExpr1) == FALSE: # prev1 = 0, curr1 = 0
            t1 = 0 
            if modeInt.get() == 1: # color scheme(light)
                if type(TempExpr2) == FALSE: # curr2 = 0
                    if t2 == 1: # expr1 from 0 to 0, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                    else: # expr1 from 0 to 0, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                    t2 = 0
                else: # current truth value of expr2 is 1
                    if t2 == 1: # expr1 from 0 to 0, expr2 from 1 to 1
                        canvas.create_line(startX,300,endX,300,width=2,fill="RoyalBlue1")
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                    else: # expr1 from 0 to 0, expr2 from 0 to 1
                        canvas.create_line(startX,300,endX,300,width=2,fill="RoyalBlue1")
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                    t2 = 1
            else: # color scheme(dark)
                if type(TempExpr2) == FALSE: # current truth value of expr2 is 0
                    if t2 == 1: # expr1 from 0 to 0, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                    else: # expr1 from 0 to 0, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                    t2 = 0
                else: # current truth value of expr2 is 1
                    if t2 == 1: # expr1 from 0 to 0, expr2 from 1 to 1
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,300,endX,300,width=2,fill="mint cream")
                    else: # expr1 from 0 to 0, expr2 from 0 to 1
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,300,endX,300,width=2,fill="mint cream")
                    t2 = 1
        else: # prev1 = 0, curr1 = 1
            t1 = 1 
            if modeInt.get() == 1: # color scheme(light)
                if type(TempExpr2) == FALSE: # curr2 = 0
                    if t2 == 1: # expr1 from 0 to 1, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,endX,130,width=2,fill="RoyalBlue1")
                    else: # expr1 from 0 to 1, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="RoyalBlue1")
                    t2 = 0
                else: # curr2 = 1
                    if t2 == 1: # expr1 from 0 to 1, expr2 from 1 to 1
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,300,endX,300,width=2,fill="RoyalBlue1")
                    else: # expr1 from 0 to 1, expr2 from 0 to 1
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                    t2 = 1
            else: # color scheme(dark)
                if type(TempExpr2) == FALSE: # curr2 = 0
                    if t2 == 1: # expr1 from 0 to 1, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,endX,130,width=2,fill="mint cream")
                    else: # expr1 from 0 to 1, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="mint cream")
                    t2 = 0
                else: # curr2 = 1
                    if t2 == 1: # expr1 from 0 to 1, expr2 from 1 to 1
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,300,endX,300,width=2,fill="mint cream")
                    else: # expr1 from 0 to 1, expr2 from 0 to 1
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                    t2 = 1
    else: # prev1 = 1
        if type(TempExpr1) == FALSE: # prev1 = 1, curr1 = 0
            t1 = 0
            if modeInt.get() == 1: # color scheme(light)
                if type(TempExpr2) == FALSE: # curr2 = 0
                    if t2 == 1: # expr1 from 1 to 0, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                    else: # expr1 from 1 to 0, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,startX,300,width=2,fill="RoyalBlue1")
                    t2 = 0
                else: # curr2 = 1
                    if t2 == 1: # expr1 from 1 to 0, expr2 from 1 to 1
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="RoyalBlue1")
                    else: # expr1 from 1 to 0, expr2 from 0 to 1
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,300,endX,300,width=2,fill="RoyalBlue1")
                    t2 = 1
            else: # color scheme(dark)
                if type(TempExpr2) == FALSE: # curr2 = 0
                    if t2 == 1: # expr1 from 1 to 0, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                    else: # expr1 from 1 to 0, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,startX,300,width=2,fill="mint cream")
                    t2 = 0
                else: # curr2 = 1
                    if t2 == 1: # expr1 from 1 to 0, expr2 from 1 to 1
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="mint cream")
                    else: # expr1 from 1 to 0, expr2 from 0 to 1
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                        canvas.create_line(startX,300,endX,300,width=2,fill="mint cream")
                    t2 = 1
        else: # prev1 = 1, curr1 = 1
            t1 = 1
            if modeInt.get() == 1: # color scheme(light)
                if type(TempExpr2) == FALSE: # curr2 = 0
                    if t2 == 1: # expr1 from 1 to 1, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,endX,130,width=2,fill="RoyalBlue1")
                    else: # expr1 from 1 to 1, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,endX,130,width=2,fill="RoyalBlue1")
                    t2 = 0
                else: # curr2 = 1
                    if t2 == 1: # expr1 from 1 to 1, expr2 from 1 to 1
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                    else: # expr1 from 1 to 1, expr2 from 0 to 1
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                    t2 = 1
            else: # color scheme(dark)
                if type(TempExpr2) == FALSE: # curr2 = 0
                    if t2 == 1: # expr1 from 1 to 1, expr2 from 1 to 0
                        canvas.create_line(startX,130,startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,endX,130,width=2,fill="mint cream")
                    else: # expr1 from 1 to 1, expr2 from 0 to 0
                        canvas.create_line(startX,300,endX,300,width=2,fill="deep pink")
                        canvas.create_line(startX,130,endX,130,width=2,fill="mint cream")
                    t2 = 0
                else: # curr2 = 1
                    if t2 == 1: # expr1 from 1 to 1, expr2 from 1 to 1
                        canvas.create_line(startX,130,endX,130,width=2,fill="deep pink")
                    else: # expr1 from 1 to 1, expr2 from 0 to 1
                        canvas.create_line(startX,300,startX,130,endX,130,width=2,fill="deep pink")
                    t2 = 1
    return t1,t2

def printAlert():
    if modeInt.get() == 1:
        canvas.create_text(330,400,
                              text="Sorry, we currently support expression waveforms of up to 2 variables.",
                              fill="RoyalBlue1",
                              font=("consolas bold",13))
    else:
        canvas.create_text(330,400,
                              text="Sorry, we currently support expression waveforms of up to 2 variables.",
                              fill="mint cream",
                              font=("consolas bold",13))
def Graph():
    t1 = time.time()
    global canvas
    
    if modeInt.get() == 1:
        rect = canvas.create_rectangle(40, 100, 1000, 320, 
                                fill="azure",
                                outline="")
        canvas.create_text(230,70,
                           text="waveforms of the two input expressions",
                           fill="RoyalBlue1",
                           font=("consolas bold",15))
        canvas.create_text(25,130,
                          text="1",
                          fill="RoyalBlue1",
                          font=("consolas bold",15))
        canvas.create_text(25,300,
                          text="0",
                          fill="RoyalBlue1",
                          font=("consolas bold",15))
    else:
        rect = canvas.create_rectangle(40, 100, 1000, 320,
                                       fill="gray35",
                                       outline="")
        canvas.create_text(230,70,
                           text="waveforms of the two input expressions",
                           fill="mint cream",
                           font=("consolas bold",15))
        canvas.create_text(25,130,
                          text="1",
                          fill="mint cream",
                          font=("consolas bold",15))
        canvas.create_text(25,300,
                          text="0",
                          fill="mint cream",
                          font=("consolas bold",15))
    global symbol_list1
    global symbol_list2
    
    symbol_list1=algebra.parse(inputExpr1.get()).get_symbols()
    expr1 = algebra.parse(inputExpr1.get())
    symbol_list2=algebra.parse(inputExpr2.get()).get_symbols()
    expr2 = algebra.parse(inputExpr2.get())
    if len(set(symbol_list1))==2 and len(set(symbol_list2))==2:
        if symbol_list1 == symbol_list2:
            t1 = 0
            t2 = 0
            # First line
            Temp1 = parseToZero(inputExpr1.get(),0)
            Temp1 = parseToZero(Temp1,0)
            TempExpr1 = algebra.parse(Temp1).simplify()

            Temp2 = parseToZero(inputExpr2.get(),0)
            Temp2 = parseToOne(Temp2,0)
            TempExpr2 = algebra.parse(Temp2)

            if type(TempExpr1) == FALSE:
                t1 = 0
                if type(TempExpr2  == FALSE):
                    t2 = 0
                    canvas.create_line(40,300,200,300,width=2,fill="deep pink")
                    if modeInt.get() == 1:
                        canvas.create_line(40,300,200,300,width=2,fill="RoyalBlue1")
                    else:
                        canvas.create_line(40,300,200,300,width=2,fill="mint cream")
                elif type(TempExpr2 == TRUE):
                    t2 = 1
                    canvas.create_line(40,130,200,130,width=2,fill="deep pink")
                    if modeInt.get() == 1:
                        canvas.create_line(40,300,200,300,width=2,fill="RoyalBlue1")
                    else:
                        canvas.create_line(40,300,200,300,width=2,fill="mint cream")
            elif type(TempExpr1) == TRUE:
                t1 = 1
                if type(TempExpr2  == FALSE):
                    t2 = 0
                    canvas.create_line(40,300,200,300,width=2,fill="deep pink")
                    if modeInt.get() == 1:
                        canvas.create_line(40,130,200,130,width=2,fill="RoyalBlue1")
                    else:
                        canvas.create_line(40,130,200,130,width=2,fill="mint cream")
                elif type(TempEXpr2 == TRUE):
                    t2 = 1
                    canvas.create_line(40,130,200,130,width=2,fill="deep pink")
                    if modeInt.get() == 1:
                        canvas.create_line(40,130,200,130,width=2,fill="RoyalBlue1")
                    else:
                        canvas.create_line(40,130,200,130,width=2,fill="mint cream")
            
            # Second line
            Temp1 = parseToZero(inputExpr1.get(),0)
            Temp1 = parseToOne(Temp1,0)
            TempExpr1 = algebra.parse(Temp1).simplify()

            Temp2 = parseToZero(inputExpr2.get(),0)
            Temp2 = parseToOne(Temp2,0)
            TempExpr2 = algebra.parse(Temp2)

            
            t1,t2 = lineDisplay(t1,t2,TempExpr1,2, 0)
            t1,t2 = lineDisplay(t1,t2,TempExpr2,2, 1)
            
            
            #Third line
            Temp1 = parseToOne(inputExpr1.get(),0)
            Temp1 = parseToOne(Temp1,0)
            TempExpr1 = algebra.parse(Temp1).simplify()

            Temp2 = parseToOne(inputExpr2.get(),0)
            Temp2 = parseToOne(Temp2,0)
            TempExpr2 = algebra.parse(Temp2)
            
            t1,t2 = lineDisplay(t1,t2,TempExpr1,TempExpr2,3)
            
            #Fourth line
            Temp1 = parseToOne(inputExpr1.get(),0)
            Temp1 = parseToZero(Temp1,0)
            TempExpr1 = algebra.parse(Temp1).simplify()

            Temp2 = parseToOne(inputExpr2.get(),0)
            Temp2 = parseToZero(Temp2,0)
            TempExpr2 = algebra.parse(Temp2)
            
            t1,t2 = lineDisplay(t1,t2,TempExpr1,TempExpr2,4)
                
        else:
            printAlert()
    elif len(symbol_list1)==1 and len(symbol_list2)==1:
        if symbol_list1[0]==symbol_list2[0]:
            if modeInt.get() == 1:
                canvas.create_line(40,300,330,300,330,130,630,130,width=2,fill="RoyalBlue1")
            else:
                canvas.create_line(40,300,330,300,330,130,630,130,width=2,fill="mint cream")
        else:
            if modeInt.get() == 1:
                canvas.create_line(40,300,330,300,330,130,630,130,width=2,fill="RoyalBlue1")
                canvas.create_line(40,130,330,130,330,300,630,300,width=2,fill="deep pink")
            else:
                canvas.create_line(40,300,330,300,330,130,630,130,width=2,fill="mint cream")
                canvas.create_line(40,130,330,130,330,300,630,300,width=2,fill="deep pink")
    else:
        printAlert()
     
    canvas.tag_raise(rect)
    for i in range(0,150):
        canvas.move(rect,5,0)
        window.update()
        time.sleep(0.07)
    
    

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

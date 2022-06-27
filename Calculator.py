from tkinter import *

def button_pressed(num):

    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Cannot Divide By 0")
        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")
    equation_text = ""

window = Tk()

window.title("Calculator")
window.geometry("500x500")
window.configure(background="#000000")

equation_text = ""

equation_label = StringVar()

label = Label(window,textvariable=equation_label,font=("Arial",20),fg="#FFFFFF",bg="#000000",width=28,height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text="7",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(7))
button1.grid(row=0,column=0)

button2 = Button(frame,text="8",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(8))
button2.grid(row=0,column=1)
button3 = Button(frame,text="9",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(9))
button3.grid(row=0,column=2)
button4 = Button(frame,text="4",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(4))
button4.grid(row=1,column=0)
button5 = Button(frame,text="5",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(5))
button5.grid(row=1,column=1)
button6 = Button(frame,text="6",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(6))
button6.grid(row=1,column=2)
button7 = Button(frame,text="1",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(1))
button7.grid(row=2,column=0)
button8 = Button(frame,text="2",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(2))
button8.grid(row=2,column=1)
button9 = Button(frame,text="3",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(3))
button9.grid(row=2,column=2)
button0 = Button(frame,text="0",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed(0))
button0.grid(row=3,column=0)
plus = Button(frame,text="+",highlightbackground="#FF9500",height=4,width=9,font=35,
                 command=lambda:button_pressed("+"))
plus.grid(row=0,column=3)
minus = Button(frame,text="-",highlightbackground="#FF9500",height=4,width=9,font=35,
                 command=lambda:button_pressed("-"))
minus.grid(row=1,column=3)
multiply = Button(frame,text="*",highlightbackground="#FF9500",height=4,width=9,font=35,
                 command=lambda:button_pressed("*"))
multiply.grid(row=2,column=3)
divide = Button(frame,text="/",highlightbackground="#FF9500",height=4,width=9,font=35,
                 command=lambda:button_pressed("/"))
divide.grid(row=3,column=3)
equal = Button(frame,text="=",highlightbackground="#FF9500",height=4,width=9,font=35,
                 command=equals)
equal.grid(row=3,column=2)
decimal = Button(frame,text=".",highlightbackground="#505050",height=4,width=9,font=35,
                 command=lambda:button_pressed("."))
decimal.grid(row=3,column=1)
clear = Button(window,text="Clear",highlightbackground="#D4D4D2",height=4,width=12,font=35,
                 command=clear)
clear.pack()

window.mainloop()
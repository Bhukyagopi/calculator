from tkinter import *

expression=''
def press(num):
    global expression
    expression+=str(num)
    equation.set(expression)

def clear():
    global expression
    expression=''
    equation.set('')

def equal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ") 
        expression = "" 
if __name__ == "__main__": 
    main = Tk()
    main.title("My Application")
    main.geometry("400x300")
    main.configure(background="#b2ffff")
    equation=StringVar()
    exp=Entry(main,textvariable=equation,font=('arial',16))
    exp.grid(columnspan=4)
    btn1 = Button(main, text="1",width=4,height=1,font="bold",foreground="black",command=lambda:press(1),background="#cb4154")
    btn1.grid(row=4,column=0)
    btn2 = Button(main, text="2",width=4,height=1,font="bold",foreground="black",command=lambda:press(2),background="#cb4154")
    btn2.grid(row=4,column=1)
    btn3 = Button(main, text="3",width=4,height=1,font="bold",foreground="black",command=lambda:press(3),background="#cb4154")
    btn3.grid(row=4,column=2)
    btnplus = Button(main, text="+",width=4,height=1,font="bold",foreground="black",command=lambda:press('+'),background="#cb4154")
    btnplus.grid(row=4,column=3)

    btn4 = Button(main, text="4",width=4,height=1,font="bold",foreground="black",command=lambda:press(4),background="#cb4154")
    btn4.grid(row=5,column=0)
    btn5 = Button(main, text="5",width=4,height=1,font="bold",foreground="black",command=lambda:press(5),background="#cb4154")
    btn5.grid(row=5,column=1)
    btn6 = Button(main, text="6",width=4,height=1,font="bold",foreground="black",command=lambda:press(6),background="#cb4154")
    btn6.grid(row=5,column=2)
    btnminus = Button(main, text="-",width=4,height=1,font="bold",foreground="black",command=lambda:press('-'),background="#cb4154")
    btnminus.grid(row=5,column=3)

    btn7 = Button(main, text="7",width=4,height=1,font="bold",foreground="black",command=lambda:press(7),background="#cb4154")
    btn7.grid(row=6,column=0)
    btn8 = Button(main, text="8",width=4,height=1,font="bold",foreground="black",command=lambda:press(8),background="#cb4154")
    btn8.grid(row=6,column=1)
    btn9 = Button(main, text="9",width=4,height=1,font="bold",foreground="black",command=lambda:press(9),background="#cb4154")
    btn9.grid(row=6,column=2)
    btnmul = Button(main, text="*",width=4,height=1,font="bold",foreground="black",command=lambda:press('*'),background="#cb4154")
    btnmul.grid(row=6,column=3)

    btn0 = Button(main, text="0",width=4,height=1,font="bold",foreground="black",command=lambda:press(0),background="#cb4154")
    btn0.grid(row=7,column=0)
    btnC = Button(main, text="C",width=4,height=1,font="bold",foreground="black",command=clear,background="#cb4154")
    btnC.grid(row=7,column=1)
    btndot = Button(main, text=".",width=4,height=1,font="bold",foreground="black",command=lambda:press('.'),background="#cb4154")
    btndot.grid(row=7,column=2)
    btndiv = Button(main, text="/",width=4,height=1,font="bold",foreground="black",command=lambda:press('/'),background="#cb4154")
    btndiv.grid(row=7,column=3)

    btneql = Button(main, text="=",width=21,height=1,font="bold",foreground="black",command=equal,background="#cb4154")
    btneql.grid(row=8, column=0, columnspan=4)
    main.mainloop()
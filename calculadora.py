from tkinter import *
from math import *

root = Tk()
root.configure(background='skyblue4')
root.title('Calc')
root.geometry('365x510')
root.resizable(0,0)

equation = StringVar()

def press(num):
    equation.set(equation.get() + str(num))

def equalPress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('Math Error')

def clear():
    equation.set('')

display = Entry(root, textvariable=equation)
display.grid(row=0, columnspan=5, sticky='nswe', ipady=10, padx=2, pady=25)
display.config(bg='powder blue', font=('arial', 20, 'bold'), justify='right', bd=10)

btnln = Button(root, text=' ln ',bd=3 ,fg='#fff', background='#EF9A53', height=3 ,width=11, command=lambda: press('log('))
btnln.grid(row=1, column=3, sticky='nswe', padx=1, pady=1)

btnModulo = Button(root, text=' % ',bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('%'))
btnModulo.grid(row=2, column=2, sticky='nswe', padx=1, pady=1)

btnPR = Button(root, text=' ) ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press(')'))
btnPR.grid(row=2, column=1, sticky='nswe', padx=1, pady=1)

btnPL = Button(root, text=' ( ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('('))
btnPL.grid(row=2, column=0, sticky='nswe', padx=1, pady=1)

btnRaiz = Button(root, text=' √ ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('sqrt('))
btnRaiz.grid(row=1, column=0, sticky='nswe', padx=1, pady=1)

btnPot = Button(root, text=' ^ ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('**'))
btnPot.grid(row=1, column=2, sticky='nswe', padx=1, pady=1)

btnPi = Button(root, text=' π ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('pi'))
btnPi.grid(row=1, column=1, sticky='nswe', padx=1, pady=1)

btn7 = Button(root, text=' 7 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(7))
btn7.grid(row=3, column=0, sticky='nswe', padx=1, pady=1)

btn8 = Button(root, text=' 8 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(8))
btn8.grid(row=3, column=1, sticky='nswe', padx=1, pady=1)

btn9 = Button(root, text=' 9 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(9))
btn9.grid(row=3, column=2, sticky='nswe', padx=1, pady=1)

btn4 = Button(root, text=' 4 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(4))
btn4.grid(row=4, column=0, sticky='nswe', padx=1, pady=1)

btn5 = Button(root, text=' 5 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(5))
btn5.grid(row=4, column=1, sticky='nswe', padx=1, pady=1)

btn6 = Button(root, text=' 6 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(6))
btn6.grid(row=4, column=2, sticky='nswe', padx=1, pady=1)

btn1 = Button(root, text=' 1 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(1))
btn1.grid(row=5, column=0, sticky='nswe', padx=1, pady=1)

btn2 = Button(root, text=' 2 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(2))
btn2.grid(row=5, column=1, sticky='nswe', padx=1, pady=1)

btn3 = Button(root, text=' 3 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(3))
btn3.grid(row=5, column=2, sticky='nswe', padx=1, pady=1)

btn0 = Button(root, text=' 0 ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press(0))
btn0.grid(row=6, column=0, sticky='nswe', padx=1, pady=1)

decimal = Button(root, text=' . ', bd=3 ,fg='#fff', background='#666', height=3, width=11, command=lambda: press('.'))
decimal.grid(row=6, column=1, sticky='nswe', padx=1, pady=1)

plus = Button(root, text=' + ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('+'))
plus.grid(row=5, column=3, sticky='nswe', padx=1, pady=1)

minus = Button(root, text=' - ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('-'))
minus.grid(row=4, column=3, sticky='nswe', padx=1, pady=1)

multiply = Button(root, text=' * ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('*'))
multiply.grid(row=3, column=3, sticky='nswe', padx=1, pady=1)

divide = Button(root, text=' / ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=lambda: press('/'))
divide.grid(row=2, column=3, sticky='nswe', padx=1, pady=1)

equal = Button(root, text=' = ', bd=3 ,fg='#fff', background='#EF9A53', height=3, width=11, command=equalPress)
equal.grid(row=6, column=3, sticky='nswe', padx=1, pady=1)

clear = Button(root, text=' C ', bd=3 ,fg='#fff', background='#999', height=3, width=11, command=clear)
clear.grid(row=6, column=2, sticky='nswe', padx=1, pady=1)

display.focus()

root.mainloop() 
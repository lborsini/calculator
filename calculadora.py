from tkinter import *

root = Tk()
root.configure(background='#333333')
root.title('Calculadora')
root.geometry('330x260')

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
display.grid(row=0, columnspan=4, sticky='nswe', ipady=8, padx=2, pady=1)

btn7 = Button(root, text=' 7 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(7))
btn7.grid(row=1, column=0, sticky='nswe', padx=1, pady=1)

btn8 = Button(root, text=' 8 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(8))
btn8.grid(row=1, column=1, sticky='nswe', padx=1, pady=1)

btn9 = Button(root, text=' 9 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(9))
btn9.grid(row=1, column=2, sticky='nswe', padx=1, pady=1)

btn4 = Button(root, text=' 4 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(4))
btn4.grid(row=2, column=0, sticky='nswe', padx=1, pady=1)

btn5 = Button(root, text=' 5 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(5))
btn5.grid(row=2, column=1, sticky='nswe', padx=1, pady=1)

btn6 = Button(root, text=' 6 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(6))
btn6.grid(row=2, column=2, sticky='nswe', padx=1, pady=1)

btn1 = Button(root, text=' 1 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(1))
btn1.grid(row=3, column=0, sticky='nswe', padx=1, pady=1)

btn2 = Button(root, text=' 2 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(2))
btn2.grid(row=3, column=1, sticky='nswe', padx=1, pady=1)

btn3 = Button(root, text=' 3 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(3))
btn3.grid(row=3, column=2, sticky='nswe', padx=1, pady=1)

btn0 = Button(root, text=' 0 ', fg='#fff', background='#666', height=2, width=10, command=lambda: press(0))
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2, padx=1, pady=1)

decimal = Button(root, text=' . ', fg='#fff', background='#666', height=2, width=10, command=lambda: press('.'))
decimal.grid(row=4, column=2, sticky='nswe', padx=1, pady=1)

plus = Button(root, text=' + ', fg='#fff', background='#fe9727', height=2, width=10, command=lambda: press('+'))
plus.grid(row=1, column=3, sticky='nswe', padx=1, pady=1)

minus = Button(root, text=' - ', fg='#fff', background='#fe9727', height=2, width=10, command=lambda: press('-'))
minus.grid(row=2, column=3, sticky='nswe', padx=1, pady=1)

multiply = Button(root, text=' * ', fg='#fff', background='#fe9727', height=2, width=10, command=lambda: press('*'))
multiply.grid(row=3, column=3, sticky='nswe', padx=1, pady=1)

divide = Button(root, text=' / ', fg='#fff', background='#fe9727', height=2, width=10, command=lambda: press('/'))
divide.grid(row=4, column=3, sticky='nswe', padx=1, pady=1)

equal = Button(root, text=' = ', fg='#fff', background='#fe9727', height=2, width=10, command=equalPress)
equal.grid(row=5, column=3, sticky='nswe', padx=1, pady=1)

clear = Button(root, text=' C ', fg='#fff', background='#999', height=2, width=10, command=clear)
clear.grid(row=5, column=2, sticky='nswe', padx=1, pady=1)

root.mainloop() 
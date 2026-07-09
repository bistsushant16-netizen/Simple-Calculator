import tkinter as tk

app = tk.Tk()
app.title("Simple Calculator")
app.geometry("250x300")
screen = tk.Entry(app, width=16, font=('Arial', 20))
screen.grid(row=0, column=0, columnspan=4)
def get_value(value):
    screen.insert(tk.END, value)

def result():
    old_value = screen.get()
    res = eval(old_value)
    screen.delete(0, tk.END)
    screen.insert(tk.END, str(res))

# Row 1
one = tk.Button(app, text='1', command=lambda: get_value('1'))
one.grid(row=1, column=0)
two = tk.Button(app, text='2', command=lambda: get_value('2'))
two.grid(row=1, column=1)
three = tk.Button(app, text='3', command=lambda: get_value('3'))
three.grid(row=1, column=2)
four = tk.Button(app, text='4', command=lambda: get_value('4'))
four.grid(row=1, column=3)

# Row 2
five = tk.Button(app, text='5', command=lambda: get_value('5'))
five.grid(row=2, column=0)
six = tk.Button(app, text='6', command=lambda: get_value('6'))
six.grid(row=2, column=1)
seven = tk.Button(app, text='7', command=lambda: get_value('7'))
seven.grid(row=2, column=2)
eight = tk.Button(app, text='8', command=lambda: get_value('8'))
eight.grid(row=2, column=3)

# Row 3
nine = tk.Button(app, text='9', command=lambda: get_value('9'))
nine.grid(row=3, column=0)
zero = tk.Button(app, text='0', command=lambda: get_value('0'))
zero.grid(row=3, column=1)
plus = tk.Button(app, text='+', command=lambda: get_value('+'))
plus.grid(row=3, column=2)
minus = tk.Button(app, text='-', command=lambda: get_value('-'))
minus.grid(row=3, column=3)
#Row 4
multiply = tk.Button(app, text='*', command=lambda: get_value('*'))
multiply.grid(row=4, column=0)
divide = tk.Button(app, text='/', command=lambda: get_value('/'))
divide.grid(row=4, column=1)
percentage = tk.Button(app, text='%', command=lambda: get_value('%'))
percentage.grid(row=4, column=2)
equal = tk.Button(app, text='=', command=result)
equal.grid(row=4, column=3)
#Row 5
def clear_screen():
    screen.delete(0, tk.END) 

clear = tk.Button(app, text='clear', command=clear_screen)
clear.grid(row=5, column=3)
app.mainloop()

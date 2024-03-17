from tkinter import *
from tkinter import END, RIGHT, DISABLED, NORMAL, ACTIVE

#define window
root = Tk()
root.title("Dan's Calculator")
root.geometry('250x330')
root.resizable(0,0)

#display frame
display = LabelFrame(root, width=285, height=80, bg='#404040', borderwidth=6)
display.pack(pady=(10, 20))

text_entry = Entry(display, bg='#404040', fg='#ffffff', justify=RIGHT, font=('Calibri', 10, 'bold'))
text_entry.grid(row=0, column=0, padx=6, pady=(10, 20), ipady=5)

button_frame = Frame(root, width=220, height=400, bg='#470A14')
button_frame.pack()

#buttons

#allows the number to show on the display
def submit(number):
  text_entry.insert(END, number)

#switches the decimal from disabled to enabled and vice-versa
def switch_disable():
  if decimal['state'] == ACTIVE:
    decimal['state'] = DISABLED

def switch_enable():
  if decimal['state'] == DISABLED:
    decimal['state'] = NORMAL

#creates a function for Clear and Quit
def top_buttons(string, rowpos, columnpos, action=print('button works yo')):
  
  clear_button = Button(button_frame, text=string, borderwidth=7, bg="#d43d54", fg='#000000', activebackground='#DE541E', activeforeground='#000000', command=action)
  clear_button.grid(row=rowpos, column=columnpos, columnspan=2, sticky='WE')

#creates function for buttons 0-9
def number_buttons(number, rowpos, columnpos, color="#721121"):
  
  button = Button(button_frame, text=number, bg=color, fg='#ffffff', activebackground='#DE541E', activeforeground='#ffffff', borderwidth=4, command=lambda: submit(number))
  button.grid(row=rowpos, column=columnpos, columnspan=1, sticky='WE')

color = "#721121"
  
#operations

def operate(operator):
  global operation
  global x
  x = text_entry.get()
  operation = operator
  
  text_entry.delete(0, END)
  decimal['state'] = NORMAL

def equals():
  global operation
  global x
  global value
  z = text_entry.get()
  text_entry.delete(0, END)

  if operation == '+':
    value = (float(x) + float(z))
  elif operation == '-':
    value = (float(x) - float(z))
  elif operation == '*':
    value = (float(x) * float(z))
  elif operation == '/':
    try:
      value = (float(x) / float(z))
    except ZeroDivisionError:
      text_entry.delete(0, END)
      submit("CANNOT DIVIDE BY 0")

  elif operation == '**':
    value = submit(float(x) ** float(z))

  decimal['state'] = NORMAL

  print(float(x), float(z))
  submit(value)
  print(value)
  
#Top Buttons (text, row, column, command)
clear = top_buttons('Clear', 0, 0, lambda: [text_entry.delete(0, END), switch_enable()])
quit = top_buttons('Quit', 0, 2, root.destroy)

#number buttons (text, row, column)
num7 = number_buttons(7, 2, 0)
num4 = number_buttons(4, 3, 0)
num1 = number_buttons(1, 4, 0)
num8 = number_buttons(8, 2, 1)
num5 = number_buttons(5, 3, 1)
num2 = number_buttons(2, 4, 1)
num0 = number_buttons(0, 5, 1)
num9 = number_buttons(9, 2, 2)
num6 = number_buttons(6, 3, 2)
num3 = number_buttons(3, 4, 2)

#decimal
decimal = Button(button_frame, text='.', bg="#721121", fg='#ffffff', activebackground='#DE541E', activeforeground='#ffffff', borderwidth=4, command=lambda: [submit('.'), switch_disable()])
decimal.grid(row=5, column=2, columnspan=1, sticky='WE')

#operator button function
def operator_button(number, rowpos, columnpos, color="#721121", action=print('button works yo')):
  button = Button(button_frame, text=number, bg=color, fg='#ffffff', activebackground='#DE541E', activeforeground='#ffffff', borderwidth=4, command=action)
  button.grid(row=rowpos, column=columnpos, columnspan=1, sticky='WE')

#operator buttons
div = operator_button('/', 1, 3, '#380a11', lambda:operate("/"))
multiply = operator_button('*', 2, 3, '#380a11', lambda:operate("*"))
subtract = operator_button('-', 3, 3, '#380a11', lambda:operate("-"))
add = operator_button('+', 4, 3, '#380a11', lambda:operate("+"))
xpowern = operator_button('x^n', 1, 2, '#380a11', lambda:operate('**'))
equal = operator_button('=', 5, 3, '#380a11', equals)

def fraction():
  try:
    value = 1 / float(text_entry.get())
    text_entry.delete(0, END)
  except ZeroDivisionError:
    text_entry.delete(0, END)
    submit('CANNOT DIVIDE BY 0')
  submit(value)

def negative():
  x = float(text_entry.get())
  value = x - (x*2)
  text_entry.delete(0, END)
  submit(value)

def square():
  value = float(text_entry.get())**2
  text_entry.delete(0, END)
  submit(value)

fraction_btn = operator_button('1//x', 1, 0, '#380a11', lambda: fraction())
negative_btn = operator_button('+/-', 5, 0, color, lambda: negative())
xpower2 = operator_button('x^2', 1, 1, '#380a11', lambda: square())

root.mainloop()
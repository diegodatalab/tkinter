#
# * 61. 1 Window and the widgets

import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')

def hello():
    print('helloooo')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
# todo - syntax -> window.geometry('widthxheight')
window.geometry('800x500')

# ttk widgets
label = ttk.Label(master = window, text = 'this is a text')
label.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# exercise label
label2 = ttk.Label(master = window, text = 'my label')
label2.pack()

# ttk button
button = ttk.Button(master = window, text = 'a button', command = button_func)
button.pack()

# ? exercise
"""
add one more text label and a button with a function that prints 'hello' ...
the label should say 'my label' and be between the entry widget and the button
"""

# exercise_button = ttk.Button(master = window, text = 'exercise', command = hello)
exercise_button = ttk.Button(master = window, text = 'exercise', command = lambda: print('hello'))
exercise_button.pack()




# run 
window.mainloop()

#
# * 62. Settings and getting data

import tkinter as tk
from tkinter import ttk


def button_func():
    '''get the content of the entry'''
    entry_text = entry.get()
    
    # ! uptdate the label
    # label.config(text='some other text')
    label['text'] = entry_text
    entry['state']='disabled'


# window
window = tk.Tk()
window.title('getting and setting widgets')

# widgets
# todo - label
label = ttk.Label(master=window, text='some text')
label.pack()

# todo - entry
entry = ttk.Entry(master=window)
entry.pack()

# todo - button
button = ttk.Button(master=window, text='a button', command=button_func)
button.pack()

# exercise
def reset_func():
    label['text']='some text'
    entry['state']='enabled'

exercise_button = ttk.Button(master=window, text='exercise button', command=reset_func)
exercise_button.pack()

# run
window.mainloop()
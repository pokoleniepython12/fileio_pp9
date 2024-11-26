from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import ttk

def upload():
    pass

window=Tk()
window.title("Файл в облако")
window.geometry("250x50")

button=ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry=ttk.Entry()
entry.pack()

window.mainloop()
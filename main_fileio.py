from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import ttk

def upload():
    filepath=fd.askopenfilename()
    if filepath:
        files={"file":open(filepath, "rb")}
        response=requests.post('https://file.io/', files=files)
        if response.status_code==200:
            data=response.json()
            link=data["link"]
            entry.insert(0, link)

window=Tk()
window.title("Файл в облако")
window.geometry("250x50")

button=ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry=ttk.Entry()
entry.pack()

window.mainloop()
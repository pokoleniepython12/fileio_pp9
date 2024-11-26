from tkinter import *
import requests
import pyperclip
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk

def upload():
    try:
        filepath=fd.askopenfilename()
        if filepath:
            with open(filepath, "rb") as f:
                files={"file":f}
                response=requests.post('https://file.io/', files=files)
                response.raise_for_status()
                data=response.json()
                link=data["link"]
                pyperclip.copy(link)
                entry.delete(0,END)
                entry.insert(0, link)
                mb.showinfo("Успешно","Ссылка успешно скопирована в буфер обмена")
    except KeyError:
        mb.showerror("Ошибка!","Невозможно получить ссылку")
    except Exception as e:
        mb.showerror("Ошибка",e)

window=Tk()
window.title("Файл в облако")
window.geometry("250x50")

button=ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry=ttk.Entry()
entry.pack()

window.mainloop()
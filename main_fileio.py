from tkinter import *
import os
import json
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
                save_history(filepath, link)
                mb.showinfo("Успешно","Ссылка успешно скопирована в буфер обмена")
    except KeyError:
        mb.showerror("Ошибка!","Невозможно получить ссылку")
    except Exception as e:
        mb.showerror("Ошибка",e)

def save_history(filepath, link):
    history=[]

    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            history=json.load(f)

    history.append({"file_path":os.path.basename(filepath),
                    "download_link":link})

    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)


history_file = "upload_history.json"

window=Tk()
window.title("Файл в облако")
window.geometry("250x50")

button=ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry=ttk.Entry()
entry.pack()

window.mainloop()
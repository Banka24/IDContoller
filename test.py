from tkinter import *
import tkinter as tk
import webbrowser

def add_user_bd():
    print("")

def check_bd_user():
    print("")

def remove_bd_user():
    print("")

def add():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('500x300')
    newWindow.resizable(width=False, height=False)

    label1 = Label(newWindow, text="Введите нового пользователя в Базу Данных")
    ent = tk.Entry(newWindow, justify="center")
    btn_3 = tk.Button(newWindow, text="Готово!", padx=20, pady=6, command=add_user_bd)

    ent.pack(anchor=NW, padx=200, pady=6)
    btn_3.pack()
    label1.pack()

def check():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('500x300')
    newWindow.resizable(width=False, height=False)

    ent = tk.Entry(newWindow, justify="center")
    label13 = Label(newWindow, text="Проверка пользователя в Базе Данных")
    btn_5 = tk.Button(newWindow, text="Готово", command=check_bd_user)

    ent.pack(anchor=NW, padx=200, pady=6)
    btn_5.pack()
    label13.pack()

def remove():
    newWindow = tk.Toplevel(window)
    newWindow.geometry('500x350')
    newWindow.resizable(width=False, height=False)

    ent = tk.Entry(newWindow, justify="center")
    label14 = Label(newWindow, text="Удалить пользователя из Базы Данных")
    btn_6 = tk.Button(newWindow, text="Готово", command=remove_bd_user)

    ent.pack(anchor=NW, padx=200, pady=6)
    btn_6.pack()
    label14.pack()

def callback(e=None):
    webbrowser.open('https://github.com/Banka24')

window = tk.Tk()
window.title("IDController")
window.geometry('400x400')
window.resizable(width=False, height=False)

btn = tk.Button(window, text="Добавление в БД", width=40, command=add)
btn.place(x=60, y=50)

button1 = tk.Button(window, text="Проверка польз. в БД", width=40, command=check)
button1.place(x=60, y=100)

button2 = tk.Button(window, text="Удаление польз. из БД", width=40, command=remove)
button2.place(x=60, y=150)

btn3 = tk.Button(window, text="Обновление БД\n( Недоступно (next update version) )", width=40)
btn3.place(x=60, y=200)

btn45 = tk.Button(window, text="Наш проект на GitHub", width=40, command=callback)
btn45.place(x=60, y=350)

window.mainloop()
from tkinter import *
from tkinter import ttk

import sqlite3 as sql

con = sql.connect('test.db')
cur = con.cursor()
soc = cur.fetchall()

def absolutepog ():
    s = float(entry.get()) * float(entry2.get()) / 100
    label["text"] = s
def ne_znaiu ():
    hui = str(float(entry3.get()) - float((entry4.get())))
    hui = str(round(float(hui), 5))
    label1 ["text"] = hui

def procent_govna ():
    hui = str(float(entry3.get()) - float((entry4.get())))
    hui = str(round(float(hui), 5))
    loh = str(float(hui) / float(entry2.get()) * 100)
    loh = (round(float(loh), 2))
    label2 ["text"] = loh

root = Tk ()
root.title("Рассчет погрешности")
root.geometry("1280x720")

lbl = Label(root, text="Класс точности")
lbl.pack(anchor=NW, padx=6, pady=6)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

lbl1 = Label(root, text="Диапазон")
lbl1.pack(anchor=NW, padx=6, pady=6)

entry2 = ttk.Entry()
entry2.pack(anchor=NW, padx=6, pady=6)

lbl11 = Label(root, text="СИ")
lbl11.pack(anchor=NW, padx=6, pady=6)

entry22 = ttk.Entry()
entry22.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Рассчет допустимой погрешности", command=absolutepog)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

lbl2 = Label(root, text="Оцифрованная точка")
lbl2.pack(anchor=NW, padx=6, pady=6)

entry3 = ttk.Entry()
entry3.pack(anchor=NW, padx=6, pady=6)

lbl3 = Label(root, text="Показания эталона")
lbl3.pack(anchor=NW, padx=6, pady=6)

entry4 = ttk.Entry()
entry4.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Рассчет разности шага", command=ne_znaiu)
btn.pack(anchor=NW, padx=6, pady=6)

label1 = ttk.Label()
label1.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Рассчет % погрешности шага", command=procent_govna)
btn.pack(anchor=NW, padx=6, pady=6)

label2 = ttk.Label()
label2.pack(anchor=NW, padx=6, pady=6)

lbl4 = Label(root, text="Название манометра")
lbl4.pack(anchor=CENTER, padx=6, pady=6)

entry5 = ttk.Entry()
entry5.pack(anchor=CENTER, padx=6, pady=6)

lbl5 = Label(root, text="Номер манометра")
lbl5.pack(anchor=CENTER, padx=6, pady=6)

entry6 = ttk.Entry()
entry6.pack(anchor=CENTER, padx=6, pady=6)




def centrtxt():

    cur.execute("CREATE TABLE IF NOT EXISTS `test` (`name` STRING, `number` STRING, `kt` STRING, `diap` STRING)")
    con.commit()
    print('Внесено')

centrtext = ttk.Button(text="Внести данные", command=centrtxt)
centrtext.pack(anchor=CENTER, padx=6, pady=6)

def centrtxt2():
    name = str(entry5.get())
    number = str(entry6.get())
    kt = str(entry.get())
    diap = str(entry2.get() + entry22.get())
    cur.execute("SELECT * FROM `test`")
    #records = cur.fetchall()
    print("Название - " + name + ' Номер - ' + number + ' Класс точности - ' + kt + ' Диапазон - ' + diap )
    print("Вывод каждой строки")

centrtext2 = ttk.Button(text="Вынести данные", command=centrtxt2)
centrtext2.pack(anchor=CENTER, padx=6, pady=6)



root.mainloop()
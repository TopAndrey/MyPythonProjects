from tkinter import *
import time
from math import *
from random import randint
import pypyodbc

root = Tk()
root.geometry("650x200")
i = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
timeS = 5
number = str(randint(2, 9)+randint(1, 9)+randint(1, 9))
number = number + str(randint(1, 9))
print(number)


online_users_table = '''CREATE TABLE online_players
                        id INTEGER PRIMARY KEY,
                        in_lobby INTEGER PRIMARY KEY);'''



''''//////////////////////////////////////////////////////////////////////'''
'''//////////////////////////////////////////////////////////////////////'''
#==================  БЭКАП  ==========================================#
def progress(status, remaining, total):
    pass
    #print(f'Скопировано {total-remaining} из {total}...')
    
try:
    sqlite_con = sqlite3.connect('sqlite_python.db')
    backup_con = sqlite3.connect('sqlite_backup.db')
    with backup_con:
        sqlite_con.backup(backup_con, pages=3, progress=progress)
    #print("Резервное копирование выполнено успешно")
except sqlite3.Error as error:
    print("Ошибка при резервном копировании: ", error)
finally:
    if(backup_con):
        backup_con.close()
        sqlite_con.close()
# == = = = = = == = = = == = = = = == = = == = = = == = = = = == = = =#
but1 = Button(font= ('Dubai',30,'bold'), text = i)
but2 = Button(font= ('Dubai',30,'bold'), text = i2)
but3 = Button(font= ('Dubai',30,'bold'), text = i3)


def newtk2():
    rot = Tk() #-------- ВТОРОЕ ОКНО (EASY) ---------#
    rot.geometry('400x400')
    global i
    global i2
    global i3
    global timeS
    global number
    i = 0
    i2 = 0
    i3 = 0
#================ СЧЕТЧИК ===========================#

    '''
    for i in range(500):
        timeS -= 0.01
        lab2['text'] = 'Осталось : '+str(round(timeS))+' сек.'
        print(timeS)
    '''

#================ ИГРА / GAME ==============================#
    number = str(randint(2, 9)+randint(1, 9)+randint(1, 9))
    number = number + str(randint(1, 9))

    def add1():
        global i
        i=i+1
        if i <= 9:
            but1['text'] = i
        else:
            i = 0
        if i == 10:
            i = 0
            but2['text'] = i
        
    def add2():
        global i2
        i2=i2+1
        if i2 <= 9:
            but2['text'] = i2
        else:
            i2 = 0
        if i2 == 10:
            i2 = 0
            but2['text'] = i2
        
    def add3():
        global i3
        i3=i3+1
        if i3 <= 9:
            but3['text'] = i3
        else:
            i3 = 0
        if i3 == 10:
            i3 = 0
            but2['text'] = i3

    def proceed():
        print(str(str(i3)+str(i2)+str(i)))
        if str(str(i3)+str(i2)+str(i)) == str(number):
            lab2['text'] = 'Вы ПОБЕДИЛИ!'
            rot.destroy()
    
    but1 = Button(rot, font= ('Dubai',30,'bold'), text = i, command = add1)
    but2 = Button(rot, font= ('Dubai',30,'bold'), text = i2, command = add2)
    but3 = Button(rot, font= ('Dubai',30,'bold'), text = i3, command = add3)
    butt1 = Button(rot, font = ('Dubai',20,'bold'), text = 'ГОТОВО!', command = proceed)

    f_top = LabelFrame(text="Твоё Окно")    
    f_top.pack()
    
    but1.pack(side=RIGHT, padx = 5)
    but2.pack(side=RIGHT, padx = 5)
    but3.pack(side=RIGHT, padx = 5)
    butt1.pack(side=BOTTOM)

#===================== СКРИПТ ПОБЕДЫ ================# 
    lab2 = Label(rot, font = 'Courier', text = 'Ваше число : '+str(number))
    lab2.pack(side = TOP)
    


def newtk():
    rot = Tk() #-------- ВТОРОЕ ОКНО (HARD) ---------#

    def add1():
        global i
        i=i+1
        if i <= 9:
            but1['text'] = i
        else:
            i = 0
        if i == 10:
            i = 0
            but2['text'] = i
        
    def add2():
        global i2
        i2=i2+1
        if i2 <= 9:
            but2['text'] = i2
        else:
            i2 = 0
        if i2 == 10:
            i2 = 0
            but2['text'] = i2
        
    def add3():
        global i3
        i3=i3+1
        if i3 <= 9:
            but3['text'] = i3
        else:
            i3 = 0
        if i3 == 10:
            i3 = 0
            but2['text'] = i3

    def add4():
        global i4
        i4=i4+1
        if i4 <= 9:
            but3['text'] = i4
        else:
            i4 = 0
        if i4 == 10:
            i4 = 0
            but2['text'] = i4
            
    def add5():
        global i5
        i5=i5+1
        if i5 <= 9:
            but3['text'] = i5
        else:
            i5 = 0
        if i5 == 10:
            i5 = 0
            but2['text'] = i5

    def add6():
        global i6
        i6=i6+1
        if i6 <= 9:
            but3['text'] = i6
        else:
            i6 = 0
        if i6 == 10:
            i6 = 0
            but2['text'] = i6
    

    
    but1 = Button(rot, font= ('Dubai',30,'bold'), text = i, command = add1)
    but2 = Button(rot, font= ('Dubai',30,'bold'), text = i2, command = add2)
    but3 = Button(rot, font= ('Dubai',30,'bold'), text = i3, command = add3)
    but4 = Button(rot, font= ('Dubai',30,'bold'), text = i4, command = add4)
    but5 = Button(rot, font= ('Dubai',30,'bold'), text = i5, command = add5)
    but6 = Button(rot, font= ('Dubai',30,'bold'), text = i6, command = add6)

    but1.pack(side=RIGHT)
    but2.pack(side=RIGHT)
    but3.pack(side=RIGHT)
    but4.pack(side=RIGHT)
    but5.pack(side=RIGHT)
    but6.pack(side=RIGHT)
#==============================#
time.sleep(0.2)
menubut1 = Button(root, font = ('Comic Sans MS', 20), text = 'Играть (Easy) 5⌘',
                 command = newtk2)
menubut2 = Button(root, font = ('Comic Sans MS', 20), text = 'Играть (Hard) 10⌘',
                 command = newtk)
#menubut2.place(relx=0.5, rely=0.45)
menubut1.place(relx=0.5, rely=0.10)
lab = Label(root, font = ('Kristen ITC', 20), text = 'Добро\nПожаловать!')
lab.pack(side = LEFT, padx = 45)

root.mainloop()

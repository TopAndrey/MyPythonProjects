from tkinter import *
import tkinter as tk
import time
root = Tk()
root.geometry("788x330")
x = 0
root.title('CMD')

def command(event):
    global x
    if x == 0:
        cmd.insert(END,'\n>>>')
        x += 1
    else:    # if x >= 1
        cmd.insert(END,'>>>')
        cmd.insert(END,'\n>>>')
        
cmd = Text(root, width = 85, height=25, font = "Courier 13", bg = 'black',fg='#e3e3e3',wrap=WORD)
cmd.bind('<Return>', command)
scroll = Scrollbar(command=cmd.yview)
scroll.pack(side=RIGHT, fill=Y)
cmd.config(yscrollcommand=scroll.set)
cmd.pack()
time.sleep(0.5)
cmd.insert(END,'Microsoft Windows [Version 10.0.19042.870]\n')
cmd.insert(END,'(c) Microsoft Corporation, 2020. All rigts reserved.')
cmd.insert(END,'\n>>>')

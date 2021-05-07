##class Car:
##    count=0
##    def__init__(self):
##        self.speed=0
##        Car.count +=1
##
##
##mycar1=Car()
##mycar1.speed=0
##print("자동차2의 현재속도눈 %dkm 생산된 자동차는 %d 입니다")


##import tkinter
##win = tkinter.Tk()
##win.geometry("500x300")
##win.resizable(True, True)
##win.title("Lable test")
##win.mainloop()

##import tkinter
##win = tkinter.Tk()
##win.geometry("640x400+100+100")
##win.resizable(False, False)
##win.title("Lable test")
##label=tkinter.Label(win, text='파이썬', width=10, height=5, fg='red', relief='solid')
##label.pack()
##win.mainloop()

##import tkinter
##win = tkinter.Tk()
##win.geometry("500x300")
##win.resizable(True, True)
##win.title("Lable test")
##win.geometry("640x400+100+100")
##win.resizable(False, False)
##win.title("Lable test")
##label=tkinter.Label(win, text='파이썬', width=10, height=5, fg='red', relief='solid')
##label.pack()
##win.mainloop()

##import tkinter as tk
##win = tk.Tk()
##B = tk.Button(win,width=10, height= 10, text = "push")
##B.place(x = 10 , y = 10)
##win.mainloop()

from tkinter import *
from tkinter import messagebox
def Callhello():
    msg = messagebox.showinfo('Hello Sangil','Welcome, please click 확인')
win = Tk()
B = Button(win, text = '클릭', command = Callhello)
B.place(x = 50,y = 50)
win.mainloop()






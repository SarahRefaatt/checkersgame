from tkinter import *
from main import main
choice=0
level=0


window =Tk()
window.title("CHECKERS")
window.geometry('500x300')

label1=Label(window,text='          choose between minimax algorithm and alphabeta',fg='red',font=('Arial',14))
label1.grid(row=0,column=0,padx=5,pady=10)

#textbox1=Entry(window,fg='blue',font=('Arial',14))
#textbox1.grid(row=0,column=0)
def call1():
    choice=1

def call2():
    choice=2


button1=Button(window,command=call2,text='minimax',fg='blue',font=('Arial',14))
button1.grid(row=1,column=1,sticky=W)

button2=Button(window,command=call1,text='alpha_beta',fg='blue',font=('Arial',14))
button2.grid(row=1,column=0,sticky=W)

def lev1():
    level=1
def lev2():
    level=2

def lev3():
    level=3


label1=Label(window,text='choose the level of difficulty(easy by default)',fg='red',font=('Arial',14))
label1.grid(row=3,column=0,padx=5,pady=10)


button1=Button(window,command=lev1,text='EASY',fg='blue',font=('Arial',14))
button1.grid(row=4,column=1,sticky=W)
button2=Button(window,command=lev2,text='MODERETE',fg='blue',font=('Arial',14))
button2.grid(row=5,column=1,sticky=W)
button2=Button(window,command=lev3,text='HARD',fg='blue',font=('Arial',14))
button2.grid(row=6,column=1,sticky=W)

def run():
    main(choice,level)


button2=Button(window,command=run,text='**RUN**',fg='red',font=('Arial',14))
button2.grid(row=7,column=0,sticky=W)



window.mainloop()
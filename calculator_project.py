from tkinter import *


root = Tk()
root.geometry("428x926")
#funtions

def click(num):
    result=en1.get()
    en1.delete(0,END)
    en1.insert(0,str(result) + str(num))



def add():
    n1=en1.get()
    global math
    math="Addition"
    global i
    i = int(n1)
    en1.delete(0,END)


def sub():
    n1=en1.get()
    global math
    math="Sub"
    global i
    i = int(n1)
    en1.delete(0,END)


def mul():
    n1=en1.get()
    global math
    math="Mul"
    global i
    i = int(n1)
    en1.delete(0,END)


def div():
    n1=en1.get()
    global math
    math="Div"
    global i
    i = int(n1)
    en1.delete(0,END)

syntaax = 'Invaild Command'



def equal():
    ans='Answer = '
    n2=en1.get()
    en1.delete(0,END)
    if math == "Addition" :
        add = i + int(n2)
        en1.insert(0, str(ans) + str(add))
    elif math== 'Sub':
        en1.insert(0,i - int(n2))
    elif math == "Mul":
        en1.insert(0,i  * int(n2))
    elif math=="Div":
        en1.insert(0,i / int(n2))
    else :
        en1.insert(0,str(syntaax))


def clear ():
    en1.delete(0,END)




#Title

root.title('root')
root['bg'] = '#161F2F'




#EntryBox
en1 = Entry(root,width=55,borderwidth=0 , bg='#87A173',foreground='Black')

en1.place(x=39,y=48)



#ImageBt


#Label

operatorss=Label(root,text='OPERATORS',bg='#1D2734')
operatorss.place(x=170,y=146)




#Buttons
bt = Button(root,text='+', borderwidth=0 , bg='#1D2734' , width=7 ,activebackground='#87A173',command=lambda:add() )
bt.place(x=36,y=192)


bt = Button(root,text='-', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command=lambda:sub())
bt.place(x=173,y=192)

bt = Button(root,text='X', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command=lambda:mul())
bt.place(x=310,y=192)

bt = Button(root,text='/', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command=lambda:div())
bt.place(x=36,y=300)

bt = Button(root,text='=', borderwidth=5,bg='#1D2734' , width=28,activebackground='#87A173',command=lambda:equal())
bt.place(x=173,y=300)

#NumericalButtons


bt = Button(root,text='1', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(1))
bt.place(x=44,y=393)

bt = Button(root,text='2', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(2))
bt.place(x=173,y=393)

bt = Button(root,text='3', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(3))
bt.place(x=310,y=393)



bt = Button(root,text='4', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(4))
bt.place(x=44,y=501)

bt = Button(root,text='5', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(5))
bt.place(x=173,y=501)

bt = Button(root,text='6', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(6))
bt.place(x=310,y=501)




bt = Button(root,text='7', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(7))
bt.place(x=44,y=609)

bt = Button(root,text='8', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(8))
bt.place(x=173,y=609)

bt = Button(root,text='9', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(9))
bt.place(x=310,y=609)




bt = Button(root,text='.', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(0))
bt.place(x=44,y=717)

bt = Button(root,text='0', borderwidth=0,bg='#1D2734' , width=7,activebackground='#87A173',command= lambda:click(0))
bt.place(x=173,y=717)

bt = Button(root,text='C', borderwidth=5,bg='#1D2734' , width=7,activebackground='#87A173' , command=lambda:clear())
bt.place(x=310,y=717)










#MainLoop
mainloop()
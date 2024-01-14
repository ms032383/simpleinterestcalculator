from tkinter import *
import psycopg2


#GUI

root=Tk()

root.title('Simple Interest')
root.config(bg='#161F2F')
root.geometry('428x926')

#funtion
def amount():
    result = e.get()
    e.delete(0,END)
    global a
    a=int(result)

def time(): 
    result = e.get()
    e.delete(0,END)
    global t
    t =int(result)

def rate():
 result =e.get()
 e.delete(0,END)
 global r
 r=int(result)

def cal():
   e.delete(0,END)
   e.insert(0,(a*t*r)/100)
   global calu
   calu = int((a*r*t)/100)


def total():
   
   e.delete(0,END)
   e.insert(0,calu+a)
   connectt = psycopg2.connect(dbname = "postgres",user="postgres",password="0000",host="localhost",port="5432")

   cursor = connectt.cursor()
   

   cursor.execute('''Create table nokar3(Amount Int ,Rate Int,Time Int );''')
   query = '''insert into nokar2(Name,age) values(%s,%s.%s);'''
   cursor.execute(query,(a,r,t))

   connectt.commit()
   connectt.close()
    
   


def clear ():
    e.delete(0,END)
   
   
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(num))


    
      


#Entry
e=Entry(root,bg='#87A173',foreground='black',borderwidth=5,width=55,)
e.place(x=39,y=48)
#label
operatorss=Label(root,text='OPERATORS',bg='#1D2734')
operatorss.place(x=170,y=146)


#Box

c=Canvas(root,width=350,height=115,bg='#1D2734')
c.place(x=39,y=196)


#buttons 
bt=Button(root,text='Amount',width=12,bg='#1D2734',activebackground='#87A173',foreground='#707070',borderwidth=2,command=lambda:amount())
bt.place(x=56,y=213)


bt=Button(root,text='Rate',width=12,bg='#1D2734',activebackground='#87A173',foreground='#707070',borderwidth=2,command=lambda:rate())
bt.place(x=251,y=213)


bt=Button(root,text='Time',width=12,bg='#1D2734',activebackground='#87A173',foreground='#707070',borderwidth=2,command=lambda:time())
bt.place(x=56,y=268)


bt=Button(root,text='Calculate',width=12,bg='#1D2734',activebackground='#87A173',foreground='#707070',borderwidth=2,command=lambda:cal())
bt.place(x=251,y=268)



bt=Button(root,text='Total Amount',width=12,bg='#1D2734',activebackground='#87A173',foreground='#707070',borderwidth=2,command=lambda:total())
bt.place(x=170,y=340)


#Numericalbt
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
#mainLoop
mainloop()
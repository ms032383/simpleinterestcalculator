from tkinter import *
from tkinter import filedialog as fd






def cmddd():
    print("What Happens")

def open_file():
    filename = fd.askopenfile(mode="r")
    if filename:
        print("You selected the file: {}".format(filename))

    

window = Tk()



menu=Menu(window)
file = Menu(menu,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open" , command= open_file)
file.add_separator()

file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Exit" , command= window.quit)

menu.add_cascade(label="File",menu=file)
window.config(menu=menu)
entry_text=StringVar()
var = StringVar()

def show():
    result=entry_text.get()
    var.set(result)


check_box1= IntVar()
check_box2= IntVar()

check_box3= IntVar()

check_box4= IntVar()



window.title('My Application')
window.geometry("500x700")
window.config(bg="Grey")
frame1= Frame(window,bg="White",width=200,height=200,cursor="Dot")
but1=Button(frame1,text="Hello",bg="grey", command= cmddd )
but2=Button(frame1,text="Send",bg="grey", command= show )

ent1=Entry(window,width=10 , textvariable=entry_text)

label2=Label(window,text="Position")
c=Canvas(window,width=500,height=500)

c.create_line(0,0,500,500,  width=5 , fill="Green",dash=(3,3))


meg=Message(window,textvariable=var , relief=RAISED,padx=20,pady=20 )
check_box1=Checkbutton(window,text="100%",onvalue=1,offvalue=0,height=2,width=10)
check_box2=Checkbutton(window,text="80%",onvalue=1,offvalue=0,height=2,width=10)

check_box3=Checkbutton(window,text="60%",onvalue=1,offvalue=0,height=2,width=10)

check_box4=Checkbutton(window,text="50%",onvalue=1,offvalue=0,height=2,width=10)






inp=Label(window,text='Your System is hack')
inp.pack()
frame1.pack()
but1.pack()
ent1.pack()
but2.pack()
label2.pack()
c.pack()
meg.pack()
check_box1.pack()
check_box2.pack()

check_box3.pack()

check_box4.pack()


window.mainloop()
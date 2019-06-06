from tkinter import *

root=Tk()
#khaki1 wheat3 tan1 khhaki3
root.title('calculator')
root.configure(background="Lightgoldenrod2")
root.geometry('500x500')
expression = " "
equation = StringVar()


def press(num):
    global expression


    expression=expression+str(num)
    equation.set(expression)



def equal():
    global expression

    total = str(eval(expression))
    equation.set(total)
    expression=" "

def clear():
    enmain.delete(first=0, last=200)



lb1 = Label(root,width=20,text='CALCULATOR',fg ='Black',bg='Lightgoldenrod2',font=('times',15,'bold'))
lb1.place(x=125,y=50)

enmain = Entry(root,width=30,text=equation,fg ='Black',bg='tan1',font=('times',15,'bold'))
enmain.place(x=100,y=100)

bt1= Button(root,width=5,command=lambda: press('1'),text='1',activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt1.place(x=100,y=150)

bt2= Button(root,width=5,text='2',command=lambda: press('2'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt2.place(x=175,y=150)

bt3= Button(root,width=5,text='3',command=lambda: press('3'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt3.place(x=250,y=150)

btplus= Button(root,width=5,text='+',command=lambda: press('+'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
btplus.place(x=325,y=150)

bt4= Button(root,width=5,text='4',command=lambda: press('4'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt4.place(x=100,y=200)

bt5= Button(root,width=5,text='5',command=lambda: press('5'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt5.place(x=175,y=200)

bt6= Button(root,width=5,text='6',command=lambda: press('6'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt6.place(x=250,y=200)

btmin= Button(root,width=5,text='-',command=lambda: press('-'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
btmin.place(x=325,y=200)

bt7= Button(root,width=5,text='7',command=lambda: press('7'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt7.place(x=100,y=250)

bt8= Button(root,width=5,text='8',command=lambda: press('8'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt8.place(x=175,y=250)

bt9= Button(root,width=5,text='9',command=lambda: press('9'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt9.place(x=250,y=250)

btdev= Button(root,width=5,text='/',command=lambda: press('/'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
btdev.place(x=325,y=250)


btclear= Button(root,width=5,text='c',command=clear,activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
btclear.place(x=100,y=300)

bt0= Button(root,width=5,text='0',command=lambda: press('0'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bt0.place(x=175,y=300)

bteql= Button(root,width=5,text='=',command=equal,activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
bteql.place(x=250,y=300)

btmul= Button(root,width=5,text='*',command=lambda: press('*'),activebackground="Khaki1",bg='khaki3',font=('times',15,'bold'))
btmul.place(x=325,y=300)

root.mainloop()


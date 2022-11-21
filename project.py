from cgitb import text
from tkinter import *
from tkinter.tix import COLUMN

root = Tk()
root.title('Return of investment')

'''ข้อความแสดงผล'''
mylabel1 = Label(text='Return of investment',fg='white',bg='black',font=20).grid(row=0, column=1)
mylabel14 = Label(text='Number of project that you want to compare').grid(row=2, column=0)
mylabel2 = Label(text='Project Name:',justify='left').grid(row=3, column=0)
mylabel3 = Label(text='Initial investment cost:',justify='left').grid(row=4, column=0)
mylabel4 = Label(text='Tax rate:',justify='left').grid(row=5, column=0)
mylabel5 = Label(text='Discount rate:',justify='left').grid(row=6, column=0)
mylabel6 = Label(text='No. of project years:',justify='left').grid(row=7, column=0)
blank1 = Label(text='').grid(row=1)
blank3 = Label(text='').grid(row=15)
'''กล่องข้อความ'''
txt = StringVar()
Tb1 = Entry()
Tb1.grid(row=2,column=1)
Tb2 = Entry()
Tb2.grid(row=3,column=1)
Tb3 = Entry()
Tb3.grid(row=4,column=1)
Tb4 = Entry()
Tb4.grid(row=5,column=1)
Tb5 = Entry()
Tb5.grid(row=6,column=1)
Tb12 = Entry(textvariable=txt)
Tb12.grid(row=7,column=1)

'''function เก็บข้อมูล'''
def getData():
    m1 = int(txt.get())
    Label(text='Cash flows projection',justify='left').grid(row=9, column=0)
    Label(text='Revenue',justify='left').grid(row=11, column=1)
    Label(text='Expense',justify='left').grid(row=11, column=2)
    Label(text='Revenue',justify='left').grid(row=11, column=1)
    Label(text='Expense',justify='left').grid(row=11, column=2)
    for i in range(1,m1+1):
        Label(text='Year'+ str(i),justify='left').grid(row=(11+i), column=0)
        Entry().grid(row=11+i,column=2)
        Entry().grid(row=11+i,column=1)




'''ปุ่มกด'''
b1 = Button(text='Enter',command=getData).grid(row=8,column=1)


root.geometry('600x500')
root.mainloop()
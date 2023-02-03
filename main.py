from tkinter import *
import math
screen = Tk()
screen.geometry("400x500")
screen.title("Epic Table Calculator")

## clear def
def clear():
   entry.delete("1.0","end")
##

## Addition def
def AddCalc():
        num = int(CalcDis.get())
        ans1=num+1
        entry.insert(END,str(num)+" + 1"+"= "+str(ans1))
        for n in range(2,13):
                ans= n+num
                entry.insert(END,'\n'+str(num)+" + "+str(n)+"= "+str(ans))
##

## Subtraction def
def SubCalc():
        num = int(CalcDis.get())
        ans1=num-1
        entry.insert(END,str(num)+" - 1"+"= "+str(ans1))
        for n in range(2,13):
                ans= num-n
                entry.insert(END,'\n'+str(num)+" - "+str(n)+"= "+str(ans))
##

## Multiplication def
def MultiCalc():
        num = int(CalcDis.get())
        ans1=num*1
        entry.insert(END,str(num)+" * 1"+"= "+str(ans1))
        for n in range(2,13):
                ans= n*num
                entry.insert(END,'\n'+str(num)+" * "+str(n)+"= "+str(ans))
##

## Division def
def DivCalc():
        num = int(CalcDis.get())
        ans1=round(num/1,3)
        entry.insert(END,str(num)+" / 1"+"= "+str(ans1))
        for n in range(2,13):
                ans= round(num/n,3)
                entry.insert(END,'\n'+str(num)+" / "+str(n)+"= "+str(ans))
##

## button setup
EnterNum = Label(screen,text="Enter your number here: ")
entry = Text(screen,height=15,width=15)
AddButton = Button(screen, text="Addition",command=AddCalc)
SubButton = Button(screen, text="Subtraction",command=SubCalc)
MulButton = Button(screen, text="Multiplication",command=MultiCalc)
DivButton = Button(screen, text="Division",command=DivCalc)
CalcDis = Entry(screen)
Clear = Button(screen,text="Clear",command=clear)
##

## screen initialization
EnterNum.grid(row=0, column=0)
entry.grid(row=1, column=1,rowspan=15) 
AddButton.grid(row=0, column=2)  
SubButton.grid(row=1, column=2) 
MulButton.grid(row=2, column=2) 
DivButton.grid(row=3, column=2) 
CalcDis.grid(row=0,column=1)
Clear.grid(row=4,column=2)
screen.mainloop()
##
from tkinter import *
import math

## clear def
def clear():
   entry.delete("1.0","end")
##

## Addition def
def AddCalc():
        Rangeinp = RangeInput.get()
        rangelist = list(Rangeinp.split(" "))
        range1 = int(rangelist[0])
        range2 = int(rangelist[1])+1
        num = int(CalcDis.get())
        ans1=num+range1
        entry.insert(END,str(num)+" + "+str(range1)+"= "+str(ans1))
        for n in range(range1+1,range2):
                ans= n+num
                entry.insert(END,'\n'+str(num)+" + "+str(n)+"= "+str(ans))
##

## Subtraction def
def SubCalc():
        Rangeinp = RangeInput.get()
        rangelist = list(Rangeinp.split(" "))
        range1 = int(rangelist[0])
        range2 = int(rangelist[1])+1
        num = int(CalcDis.get())
        ans1=num-range1
        entry.insert(END,str(num)+" - "+str(range1)+"= "+str(ans1))
        for n in range(range1+1,range2):
                ans= num-n
                entry.insert(END,'\n'+str(num)+" - "+str(n)+"= "+str(ans))
##

## Multiplication def
def MultiCalc():
        Rangeinp = RangeInput.get()
        rangelist = list(Rangeinp.split(" "))
        range1 = int(rangelist[0])
        range2 = int(rangelist[1])+1
        num = int(CalcDis.get())
        ans1=num*range1
        entry.insert(END,str(num)+" * "+str(range1)+"= "+str(ans1))
        for n in range(range1+1,range2):
                ans= n*num
                entry.insert(END,'\n'+str(num)+" * "+str(n)+"= "+str(ans))
##

## Division def
def DivCalc():
        Rangeinp = RangeInput.get()
        rangelist = list(Rangeinp.split(" "))
        range1 = int(rangelist[0])
        range2 = int(rangelist[1])+1
        num = int(CalcDis.get())
        ans1=round(num/range1,3)
        entry.insert(END,str(num)+" / "+str(range1)+"= "+str(ans1))
        for n in range(range1+1,range2):
                ans= round(num/n,3)
                entry.insert(END,'\n'+str(num)+" / "+str(n)+"= "+str(ans))
##

## setup
screen = Tk()
screen.geometry("400x500")
screen.title("Epic Table Calculator")
EnterNum = Label(screen,text="Enter your number here: ")
entry = Text(screen,height=15,width=15)
AddButton = Button(screen, text="Addition",command=AddCalc)
SubButton = Button(screen, text="Subtraction",command=SubCalc)
MulButton = Button(screen, text="Multiplication",command=MultiCalc)
DivButton = Button(screen, text="Division",command=DivCalc)
CalcDis = Entry(screen)
Clear = Button(screen,text="Clear",command=clear)
RangeNums = Label(screen,text="Enter range (ex. '12 20'): ")
RangeInput = Entry(screen)
##

## screen initialization
EnterNum.grid(row=0, column=0)
entry.grid(row=2, column=1,rowspan=15) 
AddButton.grid(row=0, column=2)  
SubButton.grid(row=1, column=2) 
MulButton.grid(row=2, column=2) 
DivButton.grid(row=3, column=2) 
CalcDis.grid(row=0,column=1)
Clear.grid(row=4,column=2)
RangeNums.grid(row=1,column=0)
RangeInput.grid(row=1,column=1)
screen.mainloop()
##
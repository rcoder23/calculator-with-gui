from tkinter import *
from tkinter import messagebox
class cal:

    def __init__(self,root):
        self.root=root
        self.root.geometry("500x500")

        self.c_out=StringVar()
        F1 = LabelFrame(self.root, text="Calculator", font=("time new roman", 15, "bold"), fg="gold", bg="red",
                        bd=8, relief=GROOVE)
        F1.place(x=50, y=0,height=70,width=400)
        # fr=Frame(self.root,width=500,height=500,bg="red").grid(row=0,column=0)
        # self.out=Entry(self.fr,command=self.output).grid(row=0,column=0)
        self.cust_name_txt = Entry(F1, width=50, textvariable=self.c_out, font=("arial", 13), bd=2, relief=SUNKEN).grid(
            row=0, column=0)
        F2 = Frame(self.root, bg="red",
                        bd=8, relief=GROOVE)
        F2.place(x=50, y=70, height=225, width=295)
        self.b1=Button(F2,text=1,command=self.one,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=1,column=1)
        self.b2=Button(F2,text=2,command=self.two,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=1,column=2)
        self.b3=Button(F2,text=3,command=self.three,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=1,column=3)
        self.b4=Button(F2,text=4,command=self.four,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=2,column=1)
        self.b5=Button(F2,text=5,command=self.five,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=2,column=2)
        self.b6=Button(F2,text=6,command=self.six,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=2,column=3)
        self.b7=Button(F2,text=7,command=self.seven,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=3,column=1)
        self.b8=Button(F2,text=8,command=self.eight,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=3,column=2)
        self.b9=Button(F2,text=9,command=self.nine,height=1,width=5,font=("time new roman", 15, "bold")).grid(row=3,column=3)
        self.bplus=Button(F2,text='+',height=1,command=self.plus,width=5,font=("time new roman", 15, "bold")).grid(row=1,column=4)
        self.bminus=Button(F2,text='-',height=1,command=self.minus,width=5,font=("time new roman", 15, "bold")).grid(row=2,column=4)
        self.bdiv=Button(F2,text='/',height=1,width=5,command=self.div,font=("time new roman", 15, "bold")).grid(row=3,column=4)
        self.bequal=Button(F2,text='=',height=1,width=5,command=self.equal,font=("time new roman", 15, "bold")).grid(row=4,column=1)
        self.clear=Button(F2,text='clear',height=1,width=5,command=self.clear,font=("time new roman", 15, "bold")).grid(row=4,column=2)
        self.exit=Button(F2,text='exit',height=1,width=5,command=self.exit,font=("time new roman", 15, "bold")).grid(row=4,column=3)
        self.zeor=Button(F2,text=0,height=1,width=5,command=self.zero,font=("time new roman", 15, "bold")).grid(row=4,column=4)
        self.mul=Button(F2,text='*',height=1,width=5,command=self.mul,font=("time new roman", 15, "bold")).grid(row=5,column=1)
        self.cr=Button(F2,text='creator',height=1,width=5,command=self.cr,font=("time new roman", 14, "bold")).grid(row=5,column=2)
    def one(self):
        self.eval=self.c_out.get()
        self.c_out.set(self.c_out.get()+"1")

    def two(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "2")
    def three(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "3")
    def four(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "4")
    def five(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "5")
    def six(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "6")
    def seven(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "7")
    def eight(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "8")
    def nine(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "9")
    def zero(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "0")
    def plus(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "+")
    def minus(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "-")
    def div(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "/")
    def equal(self):
        self.eval = self.c_out.get()
        # print(eval(self.eval))
        try:

            self.c_out.set(eval(self.eval))
        except:
            messagebox.showerror("error","INVALID OPERATION")

    def mul(self):
        self.eval = self.c_out.get()
        self.c_out.set(self.c_out.get() + "*")
    def clear(self):
        self.eval = self.c_out.get()
        self.c_out.set("")
    def exit(self):
        self.root.destroy()
    def cr(self):
        messagebox.showinfo("info","Rohit is creator")

root=Tk()
cal(root)
root.mainloop()

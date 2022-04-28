from tkinter import*
from tkinter import ttk
from ftplib import FTP
import tkinter as tk
import tkinter.messagebox
import os
import json
import time, threading
import codecs
from datetime import datetime
import itertools

class POS:

    def __init__(self,root):
        self.root = root
        self.root.title("Point of Sale")
        self.root.geometry("1380x680+0+0")
        self.root.configure(background='#003366')

        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        SubTotal_Input = StringVar()
        Total_Input = StringVar()
        Car_Registration = StringVar()
        Total_Cost = StringVar()
        choice = StringVar()

        self.P1 = PhotoImage(file = "pic/p1.png")
        self.P2 = PhotoImage(file = "pic/p2.png")
        self.P3 = PhotoImage(file = "pic/p3.png")
        self.P4 = PhotoImage(file = "pic/p4.png")
        self.P5 = PhotoImage(file = "pic/p5.png")
        self.P6 = PhotoImage(file = "pic/p6.png")
        self.P7 = PhotoImage(file = "pic/p7.png")
        self.P8 = PhotoImage(file = "pic/p8.png")

        self.PP = PhotoImage(file = "pic/pp.png")

        MainFrame = Frame(self.root, bg = '#FF9933')
        MainFrame.grid(padx=8, pady=5)

        ButtonFrame = Frame(MainFrame, bg='#003366', bd=5, width=1348, height=160, padx=4, pady=4, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bg='#FF9933', bd=5, width=800, height=300, padx=4, pady=4, relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFTCOVER = LabelFrame(DataFrame, bg='#003366', bd=5, width=800, height=300, padx=4, pady=4,
                                        font=('arial',12,'bold'), text="   Brand   ",fg="White" ,relief=RIDGE)
        DataFrameLEFTCOVER.pack(side=LEFT)

        ChangeButtonFrame = Frame(DataFrameLEFTCOVER, bd=5, width=300, height=460, pady=4, relief=RIDGE)
        ChangeButtonFrame.pack(side=LEFT,padx=4)

        ReceiptFrame = Frame(DataFrameLEFTCOVER, bd=5, width=200, height=400, pady=5, padx=1, relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT,padx=4)

        FoodItemFrame = LabelFrame(DataFrame, bd=5, width=450, height=300, padx=5, pady=2, relief=RIDGE,
                                   bg='#003366', font=('arial', 12, 'bold'), text='   Icon SLam   ',fg="White")
        FoodItemFrame.pack(side=RIGHT)

        CalFrame = Frame(ButtonFrame, bd=5, width=432, height=140, relief=RIDGE)
        CalFrame.grid(row=0, column=1, padx=5)
        #Create clock Frame
        ClockFrame = Frame(ButtonFrame, bd=5, width=500, height=140, pady=2, relief=RIDGE)
        ClockFrame.grid(row=0, column=0, padx=5)
        '''
        ChangeFrame = Frame(ButtonFrame, bd=5, width=500, height=140, pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0, column=1, padx=5)'''

        RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row=0, column=2, padx=5)
#========================================= Clock ================================================================
        lb_clock = Label(ClockFrame,font=('times',20),bg="#13293d",fg="white")
        lb_clock.grid(row=0,column=0,sticky=W,padx=5,pady=8)

        def Tick():
            global curtime,ftime
            curtime = datetime.now().time()
            ftime = curtime.strftime('%H:%M:%S')
            lb_clock.config(text=ftime)
            lb_clock.after(100,Tick)
        Tick()
#========================================= Entry =================================================================
        self.lblSubTotal = Label(CalFrame,font=('arial',14,'bold'),text="Car Registration",bd=5)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=8)
        self.txtSubTotal = Entry(CalFrame,font=('arial',14,'bold'),bd=2 ,width=24)
        self.txtSubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        self.lblTotal = Label(CalFrame,font=('arial',14,'bold'),text="Total Cost",bd=5)
        self.lblTotal.grid(row=2,column=0,sticky=W,padx=5,pady=7)
        self.txtTotal = Entry(CalFrame,font=('arial',14,'bold'),bd=2 ,width=24)
        self.txtTotal.grid(row=2,column=1,sticky=W,padx=5,pady=5)

#=======================================Function==============================================
        def car():
            if self.txtSubTotal.get() == "" or self.txtTotal.get() == "":
                tkinter.messagebox.showwarning(title=Warning, message="Please fill out all information!")
            else:
                input = open("checkin.txt")
                cc = []
                for line in input:
                    regis , cost , timein = line.split()
                    cc.append((regis, cost, timein))

                Output = list(filter(lambda x:self.txtSubTotal.get() in x, cc))
                    
                if len(Output)==0:
                    self.POS_records.insert("",tk.END, values=(self.txtSubTotal.get(),self.txtTotal.get(),ftime))
                    out = open("checkin.txt","a")
                    out.write(str(self.txtSubTotal.get())+"\t"+str(self.txtTotal.get())+"\t"+str(ftime)+"\n")
                    out.close()
                else:
                    tkinter.messagebox.showwarning(title=Warning, message="The car has already been checked in. Can't check in again")
        '''
        def downloadFile():
            filename = 'checkin.txt'
            localfile = open(filename,'wb')

            ftp.retrbinary('RETR '+filename,localfile.write,1024)
            localfile.close()
            

        def uploadFile():
            ftp.encoding = "utf-8"
            filename = 'checkin.txt'
            ftp.storbinary('STOR '+filename,open(filename,'rb'))
            
        FTPServer = '158.108.97.18'
        Username  = 'ST03603423' 
        Password = '03603423'

        ftp = FTP(FTPServer)
        ftp.login(user = Username, passwd = Password)
        print('login success')
        try:
            ftp.mkd('test1')
            ftp.cwd('test1')
        except:
            ftp.cwd('test1')
        try:
            uploadFile()
        except FileNotFoundError:
            print("No such file or directory")
        try:
            downloadFile()
        except:
            print("File not found")'''

        #======================================= Def =================================================
        
        
        def delete():#REmove unwant items
            nn = ['1','2','3','4','5','6','7','8','9','0']
            nn2 = []
            aa = self.POS_records.selection()[0]
            for a2 in aa:
                if a2 in nn:
                    a2 = int(a2)
                    nn2.append(a2)
            fn = nn2[-1]

            lines = []
            with open(r"checkin.txt", 'r') as fp:
                lines = fp.readlines()

            with open(r"checkin.txt", 'w') as fp:
                for number, line in enumerate(lines):
                    if number not in [fn-1]:
                        fp.write(line)
            self.POS_records.delete(self.POS_records.selection()[0])

        def iExit():
            iExit = tkinter.messagebox.askyesno("Point of Sale","Do you want to quit?")
            if iExit > 0:
                root.destroy()
                return
        
#========================================= Button ================================================================
        self.btnPay = Button(RemoveFrame,padx=2, font=('arial',15,'bold'),text="Check In",width=10,height=1,bd=2,command=car)
        self.btnPay.grid(row=0,column=0,pady=2,padx=4)

        self.btnExit = Button(RemoveFrame,padx=2, font=('arial',15,'bold'),text="Exit",width=10,height=1,bd=2,command=iExit)
        self.btnExit.grid(row=1,column=1,pady=2,padx=4)

        self.btnSdata = Button (RemoveFrame,padx=2, font=('arial',15,'bold'),text="Send Data",width=10,height=1,bd=2)
        self.btnSdata.grid(row=0,column=1,pady=2,padx=4)

        self.btnRemoveItem = Button (RemoveFrame,padx=2, font=('arial',15,'bold'),text="Remove",width=10,height=1,bd=2 ,command=delete)
        self.btnRemoveItem.grid(row=1,column=0,pady=2,padx=4)
#====================================================Img========================================================
        self.btnP1 = Button (ChangeButtonFrame,padx=2, image=self.P1,width=104,height=104,bd=2)
        self.btnP1.grid(row=0,column=0,pady=2,padx=4)
        self.btnP2 = Button (ChangeButtonFrame,padx=2, image=self.P2,width=104,height=104,bd=2)
        self.btnP2.grid(row=0,column=1,pady=2,padx=4)
        
        self.btnP3 = Button (ChangeButtonFrame,padx=2, image=self.P3,width=104,height=104,bd=2)
        self.btnP3.grid(row=1,column=0,pady=2,padx=4)
        self.btnP4 = Button (ChangeButtonFrame,padx=2, image=self.P4,width=104,height=104,bd=2)
        self.btnP4.grid(row=1,column=1,pady=2,padx=4)
        
        self.btnP5 = Button (ChangeButtonFrame,padx=2, image=self.P5,width=104,height=104,bd=2)
        self.btnP5.grid(row=2,column=0,pady=2,padx=4)
        self.btnP6 = Button (ChangeButtonFrame,padx=2, image=self.P6,width=104,height=104,bd=2)
        self.btnP6.grid(row=2,column=1,pady=2,padx=4)

        self.btnP7 = Button (ChangeButtonFrame,padx=2, image=self.P7,width=104,height=104,bd=2)
        self.btnP7.grid(row=3,column=0,pady=2,padx=4)
        self.btnP8 = Button (ChangeButtonFrame,padx=2, image=self.P8,width=104,height=104,bd=2)
        self.btnP8.grid(row=3,column=1,pady=2,padx=4)

        self.btnPP = Button (FoodItemFrame,padx=2, image=self.PP,width=620,height=400,bd=2)
        self.btnPP.grid(row=0,column=0,pady=2,padx=4)
#====================================================text========================================================
        scroll_x = Scrollbar(ReceiptFrame,orient=HORIZONTAL)
        scroll_y = Scrollbar(ReceiptFrame,orient=VERTICAL)

        self.POS_records=ttk.Treeview(ReceiptFrame,height=20,columns=("Car_Registration","Total_Cost","Time_CheckIn"),
                                      xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.POS_records.heading("Car_Registration",text="Car Registration")
        self.POS_records.heading("Total_Cost",text="Total Cost")
        self.POS_records.heading("Time_CheckIn",text="Time CheckIn")

        self.POS_records['show']='headings'
        
        self.POS_records.column("Car_Registration",width=120)
        self.POS_records.column("Total_Cost",width=120)
        self.POS_records.column("Time_CheckIn",width=120)

        input = open("checkin.txt")
        contacts = []
        for line in input:
            regis , cost , timein  = line.split()
            contacts.append((regis, cost, timein ))

        for contact in contacts:
            self.POS_records.insert('', tk.END, values=contact)

            
        self.POS_records.pack(fill=BOTH,expand=1)
        self.POS_records.bind("<ButtonRelease-1>")
        

                

if __name__=='__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()

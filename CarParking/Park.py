from datetime import datetime
from tkinter import *
from tkinter import ttk
import tkinter
import os
from tkinter import messagebox
from smtplib import *
from multiprocessing import Process,Value
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time, threading


p=''
ss = Value('i',0 )
uploading = Value('i',0)
#Set Tk. ======================================== 
root = tkinter.Tk()
root.geometry("1350x750+0+0")
#ชื่อโปรแกรม
root.title("PARK")
#สีBG
root.configure(bg='#003366')


SubTotal_Input = StringVar()
Total_Input = StringVar()
Car_Registration = StringVar()
Total_Cost = StringVar()
choice = StringVar()

#=============================================================Set Tk. ======================================== 

#HEADER
Tops = Label(root,font=('TH Sarabun New',35,'bold'),text="PARK",relief=GROOVE,bd=10,anchor='n',fg="#FF9933", bg="#003366")
#Tops.pack(side=TOP)
# relx=เลื่อนขวา/ซ้าย rely=เลื่อนขึ้น/ลง relwidth=ขนาดแกนx relheight=ขนาดแกนy
Tops.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.1, anchor='n')

#BOX MAIN
fMainB = Frame(root,width= 1600,height = 2200, bd=8, relief="raise", bg="#003366")
fMainB.place(x=675, y=73, width=1350, height=750, anchor='n')

# HEAD SHOP
fTL = Label(fMainB,font=('TH Sarabun New',30,'bold'),text="Data",relief=GROOVE,bd=5,anchor='n',fg="white" , bg="#FF9933")
fTL.place(relx=0.5, rely=0.01, relwidth=1, relheight=0.09, anchor='n')


# FLOOR SHOP
fMLT = Listbox(fMainB,width= 200,height = 200, bd=2, relief="raise")
fMLT.place(relx=0.5, rely=0.16, relwidth=1, relheight=0.9, anchor='n')




'''Collumn title store 
lbl1 = Label(fMainB,font=('TH Sarabun New',14,'bold'),text="Car registration",relief=GROOVE,anchor='n',fg="white",bd=3, bg="green")
lbl1.place(relx=0.125, rely=0.115, relwidth=0.25, relheight=0.045, anchor='n')
lbl2 = Label(fMainB,font=('TH Sarabun New',14,'bold'),text="Shop",relief=GROOVE,anchor='n',fg="white",bd=3, bg="green")
lbl2.place(relx=0.37, rely=0.115, relwidth=0.25, relheight=0.045, anchor='n')
lbl3 = Label(fMainB,font=('TH Sarabun New',14,'bold'),text="Total",relief=GROOVE,anchor='n',fg="white",bd=3, bg="green")
lbl3.place(relx=0.62, rely=0.115, relwidth=0.25, relheight=0.045, anchor='n')
lbl4 = Label(fMainB,font=('TH Sarabun New',14,'bold'),text="Date and time",relief=GROOVE,anchor='n',fg="white",bd=3, bg="green")
lbl4.place(relx=0.868, rely=0.115, relwidth=0.25, relheight=0.045, anchor='n')'''


#====================================================== BOX TIME (contrap update) ==========================================================

contrap = TRUE
ft = Label(root,font=('TH Sarabun New',40,'bold'),relief=GROOVE,bd=10,anchor='n',fg="black", bg="#003366")
ft.place(relx=0.9, rely=0, relwidth=0.2, relheight=0.1, anchor='n')

#===================================================== Clock ========================================================================  
lb_clock = Label(font=('times',20),bg="#13293d",fg="white")
lb_clock.place(relx=0.9, rely=0.03, relwidth=0.07, relheight=0.03, anchor='n' )


def tick():
    global curtime,ftime
    curtime = datetime.now().time()
    ftime = curtime.strftime('%H:%M:%S')
    lb_clock.config(text=ftime)
    lb_clock.after(100, tick)

tick()


# ===============================================================  def Button   ===============================================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Point of Sale","Do you want to quit?")
    if iExit > 0:
        root.destroy()
        return
    
def checkfile():
    global outtime
    if len(POS_records.selection()) != 0:
        #tkinter.messagebox.showwarning(title=Warning, message='Check')
        outtime=ftime
        popup()
    else:
        tkinter.messagebox.showwarning(title=Warning, message='กรุณาเลือกข้อมูลก่อน')



# ===============================================================  popUp   ===============================================================
def popup():
    pop = Tk()
    pop.title("คำนวณค่าจอดรถ")
    pop.geometry("320x260")
    pop.configure(bg='#003366')
    input = open("checkin.txt")
    con = []
    for line in input:
        regis , cost, time = line.split()
        con.append((regis, cost, time))
    nn = ['1','2','3','4','5','6','7','8','9','0']
    nn2 = []
    tin = []
    tout = []
    t1 = ""
    t2 = ""
    aa = POS_records.selection()[0]
    for a2 in aa:
        if a2 in nn:
            a2 = int(a2)
            nn2.append(a2)
    fn = nn2[-1]
    ff = con[fn-1]
    for i in ff[2]:
        if i in nn:
            t1+=i
        else:
            tin.append(t1)
            t1=""
    tin.append(t1)
    t1=""
    for j in outtime:
        if j in nn:
            t2+=j
        else:
            tout.append(t2)
            t2=""
    tout.append(t2)
    t2=""
    h = int(tout[0])-int(tin[0])
    m = int(tout[1])-int(tin[1])
    if m < 0 and h > 0:
        m += 60
        h -=1
    if m >= 30:
        h+=1
    parkfee = 0
    if int(ff[1])>=1000:
        parkfee = 0
    elif int(ff[1])>=100 and int(ff[1])<1000:
        if h <=1:
            parkfee = 0
        elif h>1:
            parkfee = 30*(h-1)
    elif int(ff[1])<=100:
        if h == 0:
            parkfee = 0
        else:
            parkfee = 30*h
    print(outtime,h,m,int(ff[1]))
    #======================================== popup DEF =================================
    def ipopExit():
        ipopExit = tkinter.messagebox.askyesno("Point of Sale","Do you want to quit?")
        if ipopExit > 0:
            pop.destroy()
            return
    def Culpark ():
        nn = ['1','2','3','4','5','6','7','8','9','0']
        nn2 = []
        aa = POS_records.selection()[0]
        for a2 in aa:
            if a2 in nn:
                a2 = int(a2)
                nn2.append(a2)
        fn = nn2[-1]
        ff = con[fn-1]
        input = open("checkin.txt")
        cc = []
        for line in input:
            regis , cost , timein = line.split()
            cc.append((regis, cost, timein))
        lines = []
        with open(r"checkin.txt", 'r') as fp:
            lines = fp.readlines()

        with open(r"checkin.txt", 'w') as fp:
            for number, line in enumerate(lines):
                if number not in [fn-1]:
                    fp.write(line)
        POS_records.delete(POS_records.selection()[0])

        out = open("checkout.txt","a")
        out.write(str(ff[0])+"\t"+str(ff[1])+"\t"+str(ff[2])+"\t"+str(outtime)+"\t"+str(parkfee)+"\n")
        out.close()
        tkinter.messagebox.showwarning(title=Warning, message='Check Out Success')
        pop.destroy()

        print(cc,ff)

    #======================================== Label ================================
    #======= ทะเบียน =========
    carre1 = Label(pop,font=('times',20),text="ทะเบียนรถ",bg="#003366",fg="white")
    carre1.grid(row=0, column=0, padx=5)
    carre2 = Label(pop,font=('times',20),text=ff[0],bg="#003366",fg="white")
    carre2.grid(row=0, column=1, padx=5)
    #======= เวลาเข้า =========
    lbintime1 = Label(pop,font=('times',20),text="inTime",bg="#003366",fg="white")
    lbintime1.grid(row=1, column=0, padx=5)
    lbintime2 = Label(pop,font=('times',20),text=ff[2],bg="#003366",fg="white")
    lbintime2.grid(row=1, column=1, padx=5)
    #======= เวลาออก =========
    lbouttime1 = Label(pop,font=('times',20),text="OutTime",bg="#003366",fg="white")
    lbouttime1.grid(row=2, column=0, padx=5)
    lbouttime2 = Label(pop,font=('times',20),text=outtime,bg="#003366",fg="white")
    lbouttime2.grid(row=2, column=1, padx=5)
    #======= ราคาshop =========
    shopprice1 = Label(pop,font=('times',20),text="Shoping Price",bg="#003366",fg="white")
    shopprice1.grid(row=3, column=0, padx=5)
    shopprice2 = Label(pop,font=('times',20),text=ff[1],bg="#003366",fg="white")
    shopprice2.grid(row=3, column=1, padx=5)
    #======= ราคาshop =========
    carprice1 = Label(pop,font=('times',20),text="Price",bg="#003366",fg="white")
    carprice1.grid(row=4, column=0, padx=5)
    carprice2 = Label(pop,font=('times',20),text=parkfee,bg="#003366",fg="white")
    carprice2.grid(row=4, column=1, padx=5)
    #======================================== Button ================================
    #====== iExit ==========
    button = tkinter.Button(pop,font=('TH Sarabun New',14,'bold'), text="EXIT",width=10,height=1,command=ipopExit ,bg="firebrick",fg="white")
    button.grid(row=6, column=0, padx=5)
    #======  Pay  ==========
    button = tkinter.Button(pop,font=('TH Sarabun New',14,'bold'), text="CHECK OUT",width=10,height=1,command=Culpark ,bg="#458414",fg="white")
    button.grid(row=6, column=1, padx=5)
# ==============================================================================================================================







# ===============================================================  popUp Send Mail   ===============================================================
def popupsendmail():
    PSM = Tk()
    PSM.title("ปิดรอบ")
    PSM.geometry("600x400")
    PSM.configure(bg='#003366')
    HBF = Frame(PSM,width= 300,height = 200, bd=8, relief="raise", bg="#FF9933")
    HBF.place(x=300, y=0, width=600, height=60, anchor='n')
    HEADL= Label(HBF,font=('TH Sarabun New',24,'bold'), text="Data",fg="white", bg="#FF9933")
    HEADL.place(x=300, y=1, width=80, height=40, anchor='n')
    TVF = Frame(PSM,width= 300,height = 220, bd=8, relief="raise", bg="#FF9933")
    TVF.place(x=300, y=65, width=600, height=270, anchor='n')
    
    def iPSMExit():
        iPSMExit=tkinter.messagebox.askyesno("Point of Sale","Do you want to quit?")
        if iPSMExit > 0:
            PSM.destroy()
    def sendmail():
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        time = datetime.fromtimestamp(timestamp)
        time = str(time)
        day = int(time[8] + time[9])
        month = int(time[5] + time[6])
        year = int(time[0] + time[1] + time[2] + time[3])
        receiver_email = "thiwat.su@ku.th"
        msg = MIMEMultipart()
        msg['Subject'] = "ปิดยอดประจำวันที่ "+ str(day) +"/"+str(month)+"/"+str(year)

        try:
            server = SMTP("smtp.gmail.com","587")
            server.starttls()
        except:
            print("Erroe: unable to connect SMTP server,please try again")
              
        try:
            server.login("thiwat.su@ku.th","Aum@2544")
        except:
            print("Error: invalid address or password,please try again")
                    
        msg['From'] = "thiwat.su@ku.th"
        msg['To'] = receiver_email
        filename = "checkout.txt"
        attachment = open(filename,"rb")
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename=%s"%filename)
        msg.attach(part)
        text = msg.as_string()
        server.sendmail("thiwat.su@ku.th",receiver_email,text)
        server.quit()
        tkinter.messagebox.showwarning(title=Warning, message='Send Mail Success')
        PSM.destroy()

 #===================== Create ====================== 
    # FLOOR SHOP
    FPSM = Listbox(TVF,width=96 ,height = 1, bd=2, relief="raise")
    FPSM.grid(row=1, column=0, padx=5)
    #=========== Frame=======
    BF = Frame(PSM,width= 300,height = 200, bd=8, relief="raise", bg="#FF9933")
    BF.place(x=300, y=350, width=600, height=60, anchor='n')
    #====== iExit ==========
    buttonexit = tkinter.Button(BF,font=('TH Sarabun New',14,'bold'), text="EXIT",width=10,height=1,command=iPSMExit ,bg="firebrick",fg="white")
    buttonexit.grid(row=0, column=1, padx=5)
    #======  Pay  ==========
    buttonsend = tkinter.Button(BF,font=('TH Sarabun New',14,'bold'), text="SEND MAIL",width=10,height=1,command=sendmail ,bg="#458414",fg="white")
    buttonsend.grid(row=0, column=5, padx=5)

#====================================================text========================================================
    scroll_x = Scrollbar(FPSM,orient=HORIZONTAL)
    scroll_y = Scrollbar(FPSM,orient=VERTICAL)

    POS_records=ttk.Treeview(FPSM,height=10,columns=("Car_Registration","Total_Cost","Timein","Timeout","Price"),
                                      xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    POS_records.heading("Car_Registration",text="Car Registration")
    POS_records.heading("Total_Cost",text="Total Cost")
    POS_records.heading("Timein",text="Timein")
    POS_records.heading("Timeout",text="Timeout")
    POS_records.heading("Price",text="Price")
    POS_records['show']='headings'
    POS_records.column("Car_Registration",width=110)
    POS_records.column("Total_Cost",width=110)
    POS_records.column("Timein",width=110)
    POS_records.column("Timeout",width=110)
    POS_records.column("Price",width=110)
    input = open("checkout.txt")
    contacts = []
    for line in input:
        regis , cost, timein,timeout,price = line.split()
        contacts.append((regis, cost, timein, timeout, price))
    
    for contact in contacts:
        POS_records.insert('', tkinter.END, values=contact)

        POS_records.pack(fill=BOTH,expand=1)
        POS_records.bind("<ButtonRelease-1>")
     
# ==============================================================================================================================







            
#===================================================  Create Button ===========================================================

#====== Button Work =========         
fbb = Frame(root,width= 1600,height = 2000, bd=8, relief="raise", bg="#003366")
fbb.place(x=675, y=675, width=1350, height=74, anchor='n')

#command=กดแล้วเรียกใช้def
#button = tkinter.Button(fbb,font=('TH Sarabun New',14,'bold'), text=" ชื้อปุ่ม", command= ชื่อdef ,bd=5,bg="sea green",fg="white")

######CulCar button #########
button = tkinter.Button(fbb,font=('TH Sarabun New',14,'bold'), text="คำนวณราคาที่จอด", command=checkfile,bg="#458414",fg="white")
button.place(relx=0.5, rely=0.1, relwidth=0.28, relheight=0.8, anchor='n')

###### edit button #########
#button = tkinter.Button(fbb,font=('TH Sarabun New',14,'bold'), text="ใส่ราคาสินค้า", command=editItem,bd=5,bg="sea green",fg="white")
'''button = tkinter.Button(fbb,font=('TH Sarabun New',14,'bold'), text="แก้ไขข้อมูล" , bd=5,bg="sea green",fg="white")
button.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.8, anchor='n')'''
            
######Exit button #########
button = tkinter.Button(fbb,font=('TH Sarabun New',14,'bold'), text="EXIT",command=iExit ,bg="firebrick",fg="white")
button.place(relx=0.94, rely=0.1, relwidth=0.1, relheight=0.8, anchor='n')


#====== Button Send ========= 
fb = Label(root,font=('TH Sarabun New',40,'bold'),relief=GROOVE,bd=10,anchor='n',fg="black", bg="#003366")
#Tops.pack(side=TOP)
fb.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.1, anchor='n')

button=tkinter.Button(fb,font=('TH Sarabun New',14,'bold'),width=5,text="ปิดรอบวัน",command=popupsendmail,bg="sky blue",fg="black")
button.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.8, anchor='n')

#====================================================text========================================================
scroll_x = Scrollbar(fMLT,orient=HORIZONTAL)
scroll_y = Scrollbar(fMLT,orient=VERTICAL)

POS_records=ttk.Treeview(fMLT,height=20,columns=("Car_Registration","Total_Cost","Time"),
                                      xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

POS_records.heading("Car_Registration",text="Car Registration")
POS_records.heading("Total_Cost",text="Total Cost")
POS_records.heading("Time",text="Time")
POS_records['show']='headings'
POS_records.column("Car_Registration",width=120)
POS_records.column("Total_Cost",width=120)
POS_records.column("Time",width=120)
input = open("checkin.txt")
contacts = []
for line in input:
    regis , cost, time = line.split()
    contacts.append((regis, cost, time))
    
for contact in contacts:
    POS_records.insert('', tkinter.END, values=contact)

    POS_records.pack(fill=BOTH,expand=1)
    POS_records.bind("<ButtonRelease-1>")

#========================================== RUN =================================================================================


if __name__=='__main__':
    root.resizable(width=False, height=False)
    root.mainloop()

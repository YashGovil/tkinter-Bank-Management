from tkinter import *
import tkinter as tk
import os
import mysql.connector
from tkinter import messagebox as ms
from PIL import Image,ImageTk
db=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="admin")
a=db.cursor()
import time

a.execute("CREATE DATABASE IF NOT EXISTS project")
a.execute("use project")
a.execute("CREATE TABLE IF NOT EXISTS pythons(username VARCHAR(20),password VARCHAR(20));")
a.execute("CREATE TABLE IF NOT EXISTS account(acc VARCHAR(20),type VARCHAR(20),name VARCHAR(20),amt VARCHAR(20),user VARCHAR(20));")

def main_screen1():
    global window
    window = Tk()
    window.title("NetBanking")
    window.geometry("1920x1080")
    window.configure(width=200,height=72,bg="salmon2")
    canvas1=Canvas(window,width=400,height=900,bg="salmon2")
    canvas2=Canvas(window,width=1040,height=900,bg="salmon2")
    line=canvas1.create_line(370,0,370,900,fill="lightblue2",width=50)
    line=canvas1.create_line(390,0,390,900,fill="white",width=30)
    line=canvas2.create_line(0,180,1440,180,fill="lightblue2",width=50)
    line=canvas2.create_line(0,200,1440,200,fill="white",width=30)
    line=canvas2.create_line(215,130,865,130,fill="#00008B",width=5)
    canvas1.place(x=0,y=0)
    canvas2.place(x=401,y=0)
    window1_label2=Label(window,text="Youth Bank Limited",font=("ALGERIAN",50),bg="salmon2",fg="#00008B").place(x=600,y=40)
    Button1 = Button(window, text='Create Account', bg='lightblue2',height=2, width=25,font=("Calibri", 18), command=CreateAccount.create_account)
    img=ImageTk.PhotoImage(Image.open("Untitled-8.png"))
    canvas2.create_image(120, 270, image=img, anchor=NW)
    img1=ImageTk.PhotoImage(Image.open("Untitled-9.png"))
    canvas2.create_image(560, 270, image=img1, anchor=NW)
    Button1.place(x=170, y=80, anchor="center")
    Button2 = Button(window, text='Edit Account', bg='lightblue2',font=("Calibri", 18), height=2, width=25,
                     command=EditAccount.edit_account)
    Button2.place(x=170, y=180, anchor="center")
    Button3 = Button(window, text='Deposit', bg='lightblue2', font=("Calibri", 18),height=2, width=25,
                     command=DepositCash.cash_deposit)
    Button3.place(x=170, y=280, anchor="center")
    Button4 = Button(window, text='Withdraw', bg='lightblue2',font=("Calibri", 18),height=2, width=25,
                     command=WithdrawCash.cash_withdraw)
    Button4.place(x=170, y=380, anchor="center")
    Button7 = Button(window, text='Balance Enquiry',bg='lightblue2', height=2, width=25,
                     font=("Calibri", 18), command=BalanceEnquiry.enquire_balance)
    Button7.place(x=170, y=480, anchor="center")
    Button8 = Button(window, text='Delete Account', bg='lightblue2',  font=("Calibri", 18),height=2, width=25,
                     command=DeleteAccount.account_delete)
    Button8.place(x=170, y=680, anchor="center")
    Button9 = Button(window, text='Logout', bg='lightblue2', font=("Calibri", 18),height=2, width=25,
                     command=AppSupport.support)
    Button9.place(x=170, y=780, anchor="center")
    Button10 = Button(window, text='Money Transfer', bg='lightblue2',   font=("Calibri", 18),height=2, width=25,
                     command=Transfer.MoneyTransfer)
    Button10.place(x=170, y=580, anchor="center")
    Close = Button(window, text='Close', background='lightblue2', height=2, width=10,font=("TIMES NEW ROMAN", 15), command=close)
    Close.place(x=910, y=800, anchor="center")
    window.mainloop()

def destroyy():
    
    bark.destroy()
    window.destroy()
def destroyy1():
    
    bark.destroy()
    main_screen.destroy()
    
def close():
    global bark
    bark = Toplevel(window)
    bark.configure(background='salmon2')
    bark.geometry("1920x1080+0+0")
    msg = Label(bark, text="Thank You For Visiting", bg='black', fg="white", font=("Copperplate Gothic Bold", 42))
    msg.place(x=730, y=300, anchor="center")
    k = Button(bark, text='Close',background='black',height='1',fg='white', width='7',font=("Copperplate Gothic Bold", 20), command=destroyy)
    k.place(x=725, y=500, anchor="center")

def close1():
    global bark
    bark = Toplevel(main_screen)
    bark.geometry("1920x1080+0+0")
    bark.configure(background='salmon2')
    msg = Label(bark, text="Thank You For Visiting", bg='black', fg="white", font=("Copperplate Gothic Bold", 42))
    msg.place(x=730, y=300, anchor="center")
    k = Button(bark, text='Close',background='black',height='1',fg='white', width='7',font=("Copperplate Gothic Bold", 20), command=destroyy1)
    k.place(x=725, y=500, anchor="center")
    
    
def account_screen():
   
    global main_screen
    main_screen = Tk()
    main_screen.title("NetBanking")
    #time_label=Label(main_screen,text="Local Time",font=("Verdana Bold",20),bg="#C0C0C0").place(x=900,y=2)
    main_screen.geometry("1920x1080+0+0")
    clock = Label(main_screen, font=('Times New Roman', 20, 'bold'), bg="salmon2",fg='blue')
    clock.pack(padx=30,pady=30,anchor=E)
    main_screen.configure(width=200,height=72,bg="salmon2")
    canvas1=Canvas(main_screen,width=400,height=900,bg="white")
    line=canvas1.create_line(370,0,370,900,fill="cyan2",width=50)
    line=canvas1.create_line(390,0,390,900,fill="white",width=30)
    canvas1.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open("logo (2).png"))
    label=Label(main_screen,image=img)
    label.place(x=7,y=300)
    label.img=img
    window1_label1=Label(main_screen,text="Welcome to ",font=("ALGERIAN",50),bg="salmon2",fg="#00008B").place(x=700,y=200)
    window1_label2=Label(main_screen,text="Youth Bank Limited",font=("ALGERIAN",50),bg="salmon2",fg="#00008B").place(x=580,y=265)
    window1_label2=Label(main_screen,text="Bangalore",font=("ALGERIAN",30),bg="salmon2",fg="firebrick4").place(x=780,y=338)
    def tick():
        global time1
        time1 = ''
        # get the current local time from the PC
        time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)
    tick()

    #window1_form_userinfo=Label(main_screen,text="Choose from the following",font=("Calibri Bold",18),bg="#C0C0C0",fg="midnight blue").place(x=500,y=400)
    window1_form_but1=Button(main_screen,text="Register",font=("Calibri Bold",20),width=10,command=register,bg="light blue").place(x=1050,y=500)
    #window_form_entry1=Entry(register_screen,font=("Verdana",12),textvariable=username,width=30).place(x=700,y=450)
    window1_form_but2=Button(main_screen,text="Login",font=("Calibri Bold",20),width=10,command=login,bg="light blue").place(x=550,y=500)
    #window1_form_entry2=Entry(register_screen,font=("Verdana",12),textvariable=password,width=30,show="*").place(x=700,y=500)
    #window1_button1=Button(register_screen,text="  Register  ",fg="red",bg="yellow",font=("Calibri Bold",14),command= register_user ).place(x=770,y=560)
    Close = Button(main_screen, text='Close', background='lightblue2', height=1, width=10,font=("Calibri Bold", 15), command=close1)
    Close.place(x=865, y=650, anchor="center")

    
def register():

    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    #time_label=Label(main_screen,text="Local Time",font=("Verdana Bold",20),bg="#C0C0C0").place(x=900,y=2)
    register_screen.geometry("1920x1080+0+0")
    clock = Label(register_screen, font=('Times New Roman', 20, 'bold'), bg="salmon2",fg='blue')
    clock.pack(padx=30,pady=30,anchor=E)
    register_screen.configure(width=200,height=72,bg="salmon2")
    canvas1=Canvas(register_screen,width=400,height=900,bg="white")
    line=canvas1.create_line(370,0,370,900,fill="cyan2",width=50)
    line=canvas1.create_line(390,0,390,900,fill="white",width=30)
    canvas1.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open("logo (2).png"))
    label=Label(register_screen,image=img)
    label.place(x=7,y=300)
    label.img=img
    window1_label1=Label(register_screen,text="Welcome to ",font=("ALGERIAN",50),bg="salmon2",fg="#00008B").place(x=700,y=200)
    window1_label2=Label(register_screen,text="Youth Bank Limited",font=("ALGERIAN",50),bg="salmon2",fg="#00008B").place(x=580,y=265)
    window1_label2=Label(register_screen,text="Bangalore",font=("ALGERIAN",30),bg="salmon2",fg="firebrick4").place(x=780,y=338)
    def tick():
        global time1
        time1 = ''
        # get the current local time from the PC
        time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)
    tick()

    global username
    global password

    username = StringVar()
    password = StringVar()

    global username_entry
    global password_entry

    window1_form_userinfo=Label(register_screen,text="Enter the following details appropriately in order to perform banking operation",font=("Calibri Bold",18),bg="salmon2",fg="midnight blue").place(x=500,y=430)
    window1_form_labe1=Label(register_screen,text="Username:",font=("TIMES NEW ROMAN",20),bg="salmon2").place(x=570,y=480)
    window_form_entry1=Entry(register_screen,font=("Verdana",16),textvariable=username,width=30).place(x=760,y=485)
    window1_form_labe2=Label(register_screen,text="Password:",font=("TIMES NEW ROMAN",20),bg="salmon2").place(x=570,y=550)
    window1_form_entry2=Entry(register_screen,font=("Verdana",16),textvariable=password,width=30,show="*").place(x=760,y=555)
    window1_button1=Button(register_screen,text="  Register  ",fg="red",bg="yellow",font=("Calibri Bold",22),command= register_user ).place(x=770,y=650)

def register_user():
    if username.get()=='' or password.get()=='':
        l=Label(register_screen,text='Fill all details',font=(15)).place(x=800,y=600)
    else:
        
        a.execute("select username from pythons where username = '%s'"%username.get())
        b=a.fetchall()
        for x in b:
            (y,) = x
            if username.get()==y:
                ms.showerror("Register","Account already exists")
                break
        else:
            
            username_info = username.get()
            password_info = password.get()

            a.execute("INSERT INTO pythons(username,password) VALUES('%s','%s')" %(username_info,password_info))
            db.commit()
            ms.showinfo("Succesful","Registered")


def login():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1920x1080+0+0")
    clock = Label(login_screen, font=('Times New Roman', 20, 'bold'), bg="salmon2",fg='blue')
    clock.pack(padx=30,pady=30,anchor=E)
    login_screen.configure(width=200,height=72,bg="salmon2")
    canvas1=Canvas(login_screen,width=400,height=900,bg="white")
    line=canvas1.create_line(370,0,370,900,fill="cyan2",width=50)
    line=canvas1.create_line(390,0,390,900,fill="white",width=30)
    canvas1.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open("logo (2).png"))
    label=Label(login_screen,image=img)
    label.place(x=7,y=300)
    label.img=img
    window1_label1=Label(login_screen,text="Welcome to ",font=("ALGERIAN",50),bg="salmon2",fg="#00008B").place(x=700,y=200)
    window1_label2=Label(login_screen,text="Youth Bank Limited",font=("ALGERIAN",50),bg="salmon2",fg="#00008B").place(x=580,y=265)
    window1_label2=Label(login_screen,text="Bangalore",font=("ALGERIAN",30),bg="salmon2",fg="firebrick4").place(x=780,y=338)
    def tick():
        global time1
        time1 = ''
        # get the current local time from the PC
        time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)
    tick()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    window1_form_userinfo=Label(login_screen,text="Enter the following details appropriately in order to perform banking operation",font=("Calibri Bold",18),bg="salmon2",fg="midnight blue").place(x=500,y=430)
    window1_form_labe1=Label(login_screen,text="Username:",font=("TIMES NEW ROMAN",20),bg="salmon2").place(x=570,y=480)
    window_form_entry1=Entry(login_screen,font=("Verdana",16),textvariable=username_verify,width=30).place(x=760,y=485)
    window1_form_labe2=Label(login_screen,text="Password:",font=("TIMES NEW ROMAN",20),bg="salmon2").place(x=570,y=550)
    window1_form_entry2=Entry(login_screen,font=("Verdana",16),textvariable=password_verify,width=30,show="*").place(x=760,y=555)
    window1_button1=Button(login_screen,text="  Login  ",fg="red",bg="yellow",font=("Calibri Bold",22),command= login_verify ).place(x=770,y=620)



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    # username_login_entry.delete(0, END)
    # password_login_entry.delete(0, END)
    a.execute("select * from pythons")
    b=a.fetchall()
    for x in b:
        (y,z) = x
  #   if username1 in temp:
        if username1 == y and password1==z:
            msg = Label(login_screen, text="Successful Login", fg="green", font=("calibri", 13))
            msg.place(x=150, y=230, anchor="center")
            account_screen_destory()
            main_screen1()
            break
    else:
        ms.showerror("Error","User Not Found")
   
def account_screen_destory():
    main_screen.destroy()


class CreateAccount:

    def create_account():
        global create_account_screen
        create_account_screen = Toplevel(window)
        global name
        global acc_no
        global amount
        global acc_type
        acc_no=StringVar()
        name = StringVar()
        acc_no.set("(6_Digit)")
        acc_type = StringVar()
        acc_type.set("Choose Account Type")
        amount = StringVar()
        create_account_screen.title("Create Account")
        create_account_screen.geometry("1035x646+404+216")
        create_account_screen.resizable(0,0)
        create_account_screen.configure(background='lightblue2')
        img=ImageTk.PhotoImage(Image.open("Untitled-2.png"))
        label=Label(create_account_screen,image=img)
        label.place(x=600,y=150)
        label.img=img
        img1=ImageTk.PhotoImage(Image.open("Untitled-3.png"))
        label1=Label(create_account_screen,image=img1)
        label1.place(x=335,y=10)
        label1.img=img1
        w = Label(create_account_screen, text="Name:", bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=190)
        w = Entry(create_account_screen, textvariable=name, width=40)
        w.place(x=295, y=200)
        w = Label(create_account_screen, text="Account No:",  bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=240)
        w = Entry(create_account_screen, textvariable=acc_no, width=40)
        w.place(x=295, y=250)
        w = Label(create_account_screen, text="Account Type:", bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=295)
        w = OptionMenu(create_account_screen, acc_type, "Savings Account", "Current Account",
                       command=CreateAccount.selected_value)
        w.place(x=295, y=300)
        w = Label(create_account_screen, text="Initial Amt:",  bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=350)
        w = Entry(create_account_screen, textvariable=amount, width=40)
        w.place(x=295, y=360)
        Save = Button(create_account_screen, text='Create', highlightbackground='grey', height=1, width=10,
                      font=("TIMES NEW ROMAN", 20), command=CreateAccount.save_action)
        Save.place(x=420, y=450, anchor="center")


    def selected_value(value):
        global dropdown_value
        dropdown_value = value
        print("######" + value)
        
        return dropdown_value
    
    def save_action():
        if name.get() == '' or acc_no.get() == '' or acc_type.get() == '' or amount.get() == '':
            w = Label(create_account_screen,text = 'Fill all details')
            w.place(x=420, y=400, anchor="center")
        else:
            if (acc_no.get().isdigit())==True and len(acc_no.get())==6 and (name.get().isalpha()) and (amount.get().isdigit()):
                 a.execute("select acc from account")            
                 b = a.fetchall()
                 for x in b:
                     (y,) = x                
                
                     if acc_no.get() == y:
                         ms.showerror("Error","The Account Already Exists")
                         break
                 else:                     
                     ms.showinfo("Succesful","Account Created")
                     a.execute("INSERT INTO account(acc,type,name,amt,user) VALUES('%s','%s','%s','%s','%s')" %(acc_no.get(),acc_type.get(),name.get(),amount.get(),username_verify.get()))
                     db.commit()
            else:
               ms.showerror("Failed","Wrong Input")
class EditAccount:

    def edit_account():        
       
        a.execute("select acc from account where user = '%s'"%(username_verify.get()))
        temp=[]

        b = a.fetchall()
        if b == []:
            ms.showerror("Error",'User Not Found')
            
        else:
            
            global edit_account_screen
            edit_account_screen = Toplevel(window)
            edit_account_screen.title("Edit Account")
            edit_account_screen.geometry("1035x646+404+216")
            edit_account_screen.resizable(0,0)
            edit_account_screen.configure(width=200,height=72,bg="salmon2")
            img=ImageTk.PhotoImage(Image.open("Untitled-4.png"))
            label=Label(edit_account_screen,image=img)
            label.place(x=570,y=150)
            label.img=img
            img1=ImageTk.PhotoImage(Image.open("Untitled-3.png"))
            label1=Label(edit_account_screen,image=img1)
            label1.place(x=340,y=10)
            label1.img=img1
            global edit_name
            global edit_acc_no
            global edit_amount
            edit_name = StringVar()
            edit_acc_no = StringVar()
            edit_acc_no.set("Select the Account No")
            edit_acc_type = StringVar()
            # edit_acc_type.set("Savings Account")
            edit_account_screen.title("Edit Account")
            edit_account_screen.geometry("1035x646+404+216")
            edit_account_screen.configure(background='lightblue2')
       
      
    
            for x in b:
                
                (y,) = x
                temp.append(y)
            options = temp
        
        
            w = Label(edit_account_screen, text="Account No:", bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
            w.place(x=105, y=190)
            w = OptionMenu(edit_account_screen, edit_acc_no, *options, command=EditAccount.on_option_change)
            w.place(x=300, y=195)
            
    @staticmethod
    def on_option_change(self):
        global acc_no_up
        global acc_no_ty
        global update_acc
        global updated_name
        global update_type
        global edit_acc_type
        edit_acc_type = StringVar()
        acc_no_up = edit_acc_no.get()
         
    
       
        w = Label(edit_account_screen, text="Name:", bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=240)
        updated_name = Entry(edit_account_screen, width=40)
        #(akk,) = acc_no_up
        a.execute("select name from account where acc = '%s' and user = '%s'"%(acc_no_up,username_verify.get()))
        for x in a:
            (y,)= x
            updated_name.insert(END,y)
        updated_name.place(x=300,y=250)
        edit_acc_type.set("Change account type")
        w = Label(edit_account_screen, text="Account Type:", bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=290)
        update_type = OptionMenu(edit_account_screen, edit_acc_type, 'Savings Account', 'Current Account')
        update_type.place(x=295, y=295)
        
        #update_acc = document.get("Account No")
        update = Button(edit_account_screen, text='Update', highlightbackground='grey', height=1, width=10,
                        font=("TIMES NEW ROMAN", 20), command=EditAccount.update_account)
        update.place(x=400, y=430, anchor="center")
        
    def selected_value(value):
        global dropdown_value
        dropdown_value = value
        return dropdown_value

    def update_account():
        ms.showinfo("Succesful","Account Updated")

        
        global typeess
        
        typeess = edit_acc_type.get()
        a.execute("update account set name = '%s' where acc = '%s'"%(updated_name.get(),acc_no_up))
        a.execute("update account set type = '%s' where acc = '%s'"%(typeess,acc_no_up))
        db.commit()
           
class Transfer:
    
    def MoneyTransfer():
        a.execute("select acc from account where user = '%s'"%(username_verify.get()))
        temp=[]
        b = a.fetchall()
        if b == []:
            ms.showerror("Error","User Not Found")
            
        else:
            global money_transfer_screen
            money_transfer_screen = Toplevel(window)
            money_transfer_screen.title("Transfer Window")
            money_transfer_screen.geometry("1035x646+404+216")
            money_transfer_screen.resizable(0,0)
            
            img=ImageTk.PhotoImage(Image.open("mti.png"))
            label=Label(money_transfer_screen,image=img)
            label.place(x=630,y=170)
            label.img=img
            img1=ImageTk.PhotoImage(Image.open("Untitled-3.png"))
            label1=Label(money_transfer_screen,image=img1)
            label1.place(x=390,y=10)
            label1.img=img1
            global edit_name
            global edit_acc_no
            global edit_amount
            edit_name = StringVar()
            edit_acc_no = StringVar()
            edit_acc_no.set("Select the Account No")
            edit_acc_type = StringVar()
            # edit_acc_type.set("Savings Account")
            money_transfer_screen.title("Transfer")

            money_transfer_screen.geometry("1035x646+404+216")
            money_transfer_screen.configure(background='lightblue2')
            a.execute("select acc from account where user = '%s'"%(username_verify.get()))
            temp=[]

            b = a.fetchall()

            for x in b:
                
                (y,) = x
                temp.append(y)
            options = temp
            
            w = Label(money_transfer_screen, text="Account No:", bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
            w.place(x=105, y=190)
            w = OptionMenu(money_transfer_screen, edit_acc_no, *options, command=Transfer.on_option_change)
            w.place(x=350, y=195)
    @staticmethod
    def on_option_change(self):
        global update_acc
        global acc_no_up
        global orig_amt
        global edit_acc_no
        global updated_name
        global transfer_amount
        global transfer_account
        transfer_account = StringVar()
        acc_no_up = edit_acc_no.get()
        global edit_acc_type
        transfer_account.set("Select the Account No")
        edit_acc_type = StringVar()
        orig_amt=StringVar()
        transfer_amount = StringVar()
     
        w = Label(money_transfer_screen, text="Name:",bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=240)
        updated_name = Entry(money_transfer_screen,width=40)
        a.execute("select name from account where acc = '%s'"%acc_no_up)
        for x in a:
            (y,)= x
            updated_name.insert(END,y)
        updated_name.place(x=350,y=250)
        a.execute("select acc from account")
        tempo=[]

        b = a.fetchall()

        for x in b:
                
            (y,) = x
            tempo.append(y)
        option = tempo
        w = Label(money_transfer_screen, text="Account to transfer:", bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=290)
        w = OptionMenu(money_transfer_screen, transfer_account, *option)
        w.place(x=350, y=295)
        w = Label(money_transfer_screen, text="Transfer Amount:",  bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=105, y=340)
        w = Entry(money_transfer_screen, textvariable=transfer_amount, width=40)
        w.place(x=350, y=350)
        update = Button(money_transfer_screen, text='Transfer', highlightbackground='grey', height=1, width=10,
                        font=("TIMES NEW ROMAN", 20), command=Transfer.update_account)
        update.place(x=470, y=450, anchor="center")
        
    def update_account():
        if transfer_amount.get() == '':
           
            w = Label(money_transfer_screen,text = 'Fill all details')
            w.place(x=460, y=390, anchor="center")
        else:
            global old_list
            global final_amount
            global typeess
            typeess = edit_acc_type.get()
            
            
            if (transfer_amount.get().isdigit())==True:
                a.execute("select amt from account where acc = '%s'"%acc_no_up)
                
                b = a.fetchall()
                
                for x in b:
                    (y,)= x
                
                if int(transfer_amount.get())<=int(y):              
                    a.execute("select amt from account where acc = '%s'"%transfer_account.get())
                    b = a.fetchall()
                    for x in b:
                        (y,)= x
                    a.execute("update account set amt = '%s' where acc = '%s'"%((int(y)+int(transfer_amount.get()),transfer_account.get())))
                    db.commit()
                    a.execute("select amt from account where acc = '%s'"%acc_no_up)
                    b = a.fetchall()
                    for x in b:
                        (y,)= x
                    a.execute("update account set amt = '%s' where acc = '%s'"%((int(y)-int(transfer_amount.get()),acc_no_up)))
                    db.commit()
                    ms.showinfo("Successful","Rs."+transfer_amount.get()+" Transfered")
                    
                    
                else:
                    ms.showerror("Failed","Insufficient Funds")
            else:
                ms.showerror("Failed","Wrong Input")
                    
class DepositCash:

    def cash_deposit():
        
        a.execute("select acc from account where user = '%s'"%(username_verify.get()))
        temp=[]
        b = a.fetchall()
        if b == []:
     
            ms.showerror("Error",'User Not Found')
            
        else:
            global cash_deposit_screen
            cash_deposit_screen = Toplevel(window)
            cash_deposit_screen.title("Cash Deposit")
            cash_deposit_screen.geometry("1035x646+404+216")
            cash_deposit_screen.resizable(0,0)
            
            img=ImageTk.PhotoImage(Image.open("Untitled-5.png"))
            label=Label(cash_deposit_screen,image=img)
            label.place(x=570,y=150)
            label.img=img
            img1=ImageTk.PhotoImage(Image.open("Untitled-3.png"))
            label1=Label(cash_deposit_screen,image=img1)
            label1.place(x=340,y=10)
            label1.img=img1
                
            global edit_name
            global edit_acc_no
            global edit_amount
            edit_name = StringVar()
            edit_acc_no = StringVar()
            edit_acc_no.set("Select the Account No")
            edit_acc_type = StringVar()
       
            cash_deposit_screen.title("Deposit Cash")
            cash_deposit_screen.geometry("1035x646+404+216")
            cash_deposit_screen.configure(background='lightblue2')
            a.execute("select acc from account where user = '%s'"%(username_verify.get()))
            
            temp=[]

            b = a.fetchall()

            for x in b:
                
                (y,) = x
                temp.append(y)
            options = temp
            
            w = Label(cash_deposit_screen, text="Account No:", bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
            w.place(x=120, y=190)
            w = OptionMenu(cash_deposit_screen, edit_acc_no, *options, command=DepositCash.on_option_change)
            w.place(x=315, y=195)

    @staticmethod
    def on_option_change(self):
        global update_acc
        global acc_no_up
        global orig_amt
        global edit_acc_no
        global updated_name
        global deposit_amount
        acc_no_up = edit_acc_no.get()
        global edit_acc_type
        edit_acc_type = StringVar()
        orig_amt=StringVar()
        deposit_amount = StringVar()
     
        w = Label(cash_deposit_screen,text="Name:", bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=120, y=240)
        updated_name = Entry(cash_deposit_screen,width=40)
        a.execute("select name from account where acc = '%s'"%acc_no_up)
        for x in a:
            
            (y,)= x
            updated_name.insert(END,y)
        updated_name.place(x=315,y=250)
        w = Label(cash_deposit_screen, text="Deposit Amount:", bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=120, y=290)
        w = Entry(cash_deposit_screen, textvariable=deposit_amount, width=40)
        w.place(x=315, y=300)
        update = Button(cash_deposit_screen, text='Deposit',  highlightbackground='grey', height=1, width=10,
                        font=("TIMES NEW ROMAN", 20), command=DepositCash.update_account)
        update.place(x=440, y=410, anchor="center")

    def update_account():
        if deposit_amount.get() == '':
            w = Label(cash_deposit_screen,text = 'Fill all details')
            w.place(x=430, y=350, anchor="center")
           
            
        else:
            global old_list
            global final_amount
            global typeess
            global bark
            typeess = edit_acc_type.get()

            if (deposit_amount.get().isdigit())==True:
                ms.showinfo("Succesful","Amount " + deposit_amount.get() + " Has Been Deposited")
                
                a.execute("select amt from account where acc = '%s'"%acc_no_up)
                for x in a:
                    print(x)
                    (y,)= x
                
                a.execute("update account set amt = '%s' where acc = '%s'"%(int(y)+int(deposit_amount.get()),acc_no_up))
                db.commit()
              
                
            else:
                ms.showerror("Failed","Wrong Input")

class WithdrawCash:

    def cash_withdraw():
        
        a.execute("select acc from account where user = '%s'"%(username_verify.get()))
        temp=[]
        b = a.fetchall()
        if b == []:
            ms.showerror("Error",'User Not Found')
        else:
            global cash_withdraw_screen
            cash_withdraw_screen = Toplevel(window)
            cash_withdraw_screen.geometry("1035x646+404+216")
            cash_withdraw_screen.title("Cash Withdraw")
            cash_withdraw_screen.resizable(0,0)
            
            img=ImageTk.PhotoImage(Image.open("images (1).png"))
            label=Label(cash_withdraw_screen,image=img)
            label.place(x=630,y=150)
            label.img=img
            img1=ImageTk.PhotoImage(Image.open("Untitled-3.png"))
            label1=Label(cash_withdraw_screen,image=img1)
            label1.place(x=340,y=10)
            label1.img=img1
            global edit_name
            global edit_acc_no
            global edit_amount
            edit_name = StringVar()
            edit_acc_no = StringVar()
            edit_acc_no.set("Select the Account No")
            edit_acc_type = StringVar()
            # edit_acc_type.set("Savings Account")
            cash_withdraw_screen.title("Withdraw Cash")
            cash_withdraw_screen.geometry("1035x646+404+216")
            cash_withdraw_screen.configure(background='lightblue2')
            a.execute("select acc from account where user = '%s'"%(username_verify.get()))
            temp=[]

            b = a.fetchall()

            for x in b:
                
                (y,) = x
                temp.append(y)
            options = temp
            
            w = Label(cash_withdraw_screen, text="Account No:", bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
            w.place(x=120, y=190)
            w = OptionMenu(cash_withdraw_screen, edit_acc_no, *options, command=WithdrawCash.on_option_change)
            w.place(x=340, y=195)

    @staticmethod
    def on_option_change(self):
        global update_acc
        global acc_no_up
        global orig_amt
        global edit_acc_no
        global updated_name
        global withdraw_amount
        acc_no_up = edit_acc_no.get()
        global edit_acc_type
        edit_acc_type = StringVar()
        orig_amt=StringVar()
        withdraw_amount = StringVar()
        

        w = Label(cash_withdraw_screen, text="Name:", bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=120, y=240)
        updated_name = Entry(cash_withdraw_screen, width=40)
        a.execute("select name from account where acc = '%s'"%acc_no_up)
        for x in a:
            (y,)= x
            updated_name.insert(END,y)
        updated_name.place(x=340,y=250)
        w = Label(cash_withdraw_screen, text="Withdraw Amount:",  bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=120, y=290)
        w = Entry(cash_withdraw_screen, textvariable=withdraw_amount, width=40)
        w.place(x=340, y=300)
        update = Button(cash_withdraw_screen, text='Update', highlightbackground='grey', height=1, width=10,
                        font=("TIMES NEW ROMAN", 20),command=WithdrawCash.update_account)
        update.place(x=470, y=400, anchor="center")

    def update_account():
        if withdraw_amount.get() == '':
            w = Label(cash_withdraw_screen,text = 'Fill all details')
            w.place(x=460, y=350, anchor="center")
           
            
        else:
            global bark
            global old_list
            global final_amount
            global typeess
            
            typeess = edit_acc_type.get()
            if (withdraw_amount.get().isdigit())==True:
                a.execute("select amt from account where acc = '%s'"%acc_no_up)
                for x in a:
                    print(x)
                    (y,)= x
                if (int(y)-int(withdraw_amount.get()))>=0:
                    ms.showinfo("Succesful","Amount " + withdraw_amount.get() + " Has Been Withdrawn")
                    
                    a.execute("update account set amt = '%s' where acc = '%s'"%(int(y)-int(withdraw_amount.get()),acc_no_up))
                    db.commit()
                  
                else:
                    ms.showinfo("Failed","Insufficient Funds")
                  
            else:
                 ms.showinfo("Failed","Wrong Input")

class BalanceEnquiry:
    
    def enquire_balance():
        a.execute("select acc from account where user = '%s'"%(username_verify.get()))
        temp=[]
        b = a.fetchall()
        if b == []:
            ms.showerror("Error","User Not Found")
            
        else:
            global enquire_balance_screen
            enquire_balance_screen = Toplevel(window)
            enquire_balance_screen.geometry("1035x646+404+216")
            enquire_balance_screen.title("Balance Enquiry")
            enquire_balance_screen.resizable(0,0)
            
            img=ImageTk.PhotoImage(Image.open("Untitled-6.png"))
            label=Label(enquire_balance_screen,image=img)
            label.place(x=570,y=170)
            label.img=img
            img1=ImageTk.PhotoImage(Image.open("Untitled-3.png"))
            label1=Label(enquire_balance_screen,image=img1)
            label1.place(x=340,y=10)
            label1.img=img1
            global edit_name
            global edit_acc_no
            global edit_amount
            edit_name = StringVar()
            edit_acc_no = StringVar()
            edit_acc_no.set("Select the Account No")
            edit_acc_type = StringVar()
            enquire_balance_screen.title("Cash Balance")
            enquire_balance_screen.geometry("1035x646+404+216")
            enquire_balance_screen.configure(background='lightblue2')
            a.execute("select acc from account where user = '%s'"%(username_verify.get()))
            temp=[]

            b = a.fetchall()

            for x in b:
                
                (y,) = x
                temp.append(y)
            options = temp
            
            w = Label(enquire_balance_screen,text="Account No:",  bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
            w.place(x=120, y=200)
            w = OptionMenu(enquire_balance_screen, edit_acc_no, *options, command=BalanceEnquiry.on_option_change)
            w.place(x=300, y=205)

    @staticmethod
    def on_option_change(self):
        global update_acc
        global acc_no_up
        global orig_amt
        global edit_acc_no
        global updated_name
        global withdraw_amount
        acc_no_up = edit_acc_no.get()
        global edit_acc_type
        edit_acc_type = StringVar()
        orig_amt=StringVar()
        withdraw_amount = StringVar()

        w = Label(enquire_balance_screen, text="Name:",  bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=120, y=250)
        updated_name = Entry(enquire_balance_screen, width=40)
        a.execute("select name from account where acc = '%s'"%acc_no_up)
        for x in a:
            (y,)= x
            updated_name.insert(END,y)
        updated_name.place(x=300,y=260)
        update = Button(enquire_balance_screen, text='Show Balance',  highlightbackground='grey', height=1, width=12,
                        font=("TIMES NEW ROMAN", 18), command=BalanceEnquiry.update_account)
        update.place(x=400, y=360, anchor="center")

    def update_account():
        a.execute("select amt from account where acc = '%s'"%acc_no_up)
        for x in a:
            print(x)
            (y,)= x
        ms.showinfo("Succesful","Your account balance is " + y)
            
class DeleteAccount:
    
    def account_delete():
        
        a.execute("select acc from account where user = '%s'"%(username_verify.get()))
        temp=[]
        b = a.fetchall()
        if b == []:
            ms.showerror("Error","User Not Found")
        else:
            global delete_account_screen
            delete_account_screen = Toplevel(window)
            delete_account_screen.geometry("1035x646+404+216")
            delete_account_screen.resizable(0,0)
            delete_account_screen.title("Delete Account")
            delete_account_screen.configure(background='salmon2')
            
            img=ImageTk.PhotoImage(Image.open("business-banking.png"))
            label=Label(delete_account_screen,image=img)
            label.place(x=570,y=170)
            label.img=img
            img1=ImageTk.PhotoImage(Image.open("Untitled-3.png"))
            label1=Label(delete_account_screen,image=img1)
            label1.place(x=340,y=10)
            label1.img=img1
            global edit_name
            global edit_acc_no
            global edit_amount
            edit_name = StringVar()
            edit_acc_no = StringVar()
            edit_acc_no.set("Select the Account No")
            edit_acc_type = StringVar()
            
            delete_account_screen.title("Deposit Cash")
            delete_account_screen.geometry("1035x646+404+216")
            delete_account_screen.configure(background='lightblue2')
            a.execute("select acc from account where user = '%s'"%(username_verify.get()))
            temp=[]
            b = a.fetchall()

            for x in b:  
                (y,) = x
                temp.append(y)
            options = temp
            w = Label(delete_account_screen, text="Account No:",bg='lightblue2',relief='flat',font=("TIMES NEW ROMAN", 20))
            w.place(x=120, y=200)
            w = OptionMenu(delete_account_screen, edit_acc_no, *options, command=DeleteAccount.on_option_change)
            w.place(x=300, y=205)

    @staticmethod
    def on_option_change(self):
        global update_acc
        global acc_no_up
        global orig_amt
        global edit_acc_no
        global updated_name
        global withdraw_amount
        acc_no_up = edit_acc_no.get()
        global edit_acc_type
        edit_acc_type = StringVar()
        orig_amt=StringVar()
        withdraw_amount = StringVar()
        w = Label(delete_account_screen, text="Name:",bg='lightblue2', font=("TIMES NEW ROMAN", 20))
        w.place(x=120, y=240)
        updated_name = Entry(delete_account_screen, width=40)
        a.execute("select name from account where acc = '%s'"%acc_no_up)
        for x in a:
            (y,)= x
            updated_name.insert(END,y)
        updated_name.place(x=300,y=250)
        update = Button(delete_account_screen, text='Delete', highlightbackground='grey', height=1, width=10,
                        font=("TIMES NEW ROMAN", 18), command=DeleteAccount.update_account)
        update.place(x=400, y=330, anchor="center")

    def update_account():
         ms.showinfo("Succesful","Your account is deleted")
         a.execute("delete from account where acc = '%s'"%acc_no_up)
         db.commit()

class AppSupport:
    def support():
       window.destroy()   
       account_screen()
account_screen()

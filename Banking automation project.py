from tkinter import *
from tkinter import messagebox
import time
import sqlite3

try:
    conobj=sqlite3.connect(database='sqlite')
    curobj=conobj.cursor()
    curobj.execute('create table acn(acn_acno integer primary key autoincrement, acn_name text, acn_pass text, acn_email text, acn_mob text, acn_bal float, acn_opendate text)')
    print('table created')
except:
    print('table already created or something else')
curobj.close()

win=Tk()
win.configure(bg='powder blue')
win.state('zoomed')
win.resizable(width=False,height=False)

lbl_title=Label(win,text='Banking Automation',font=('',25,'bold','underline'),bg='powder blue')
lbl_title.pack()

date=time.strftime('%d-%m-%Y')
lbl_date=Label(win,text=date,font=('',20,'bold'),bg='powder blue')
lbl_date.place(relx=.89,rely=.08)

def main_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)

    def newuser():
        frm.destroy()
        newuser_screen()

    def forgot():
        frm.destroy()
        forgot_screen()

    def login():
        global acn
        acn=e_acn.get()
        pwd=e_pass.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showwarning('validation','Empty fields are not allowed')
        else:
            conobj=sqlite3.connect(database='sqlite')
            curobj=conobj.cursor()
            curobj.execute('select * from acn where acn_acno=? and acn_pass=?',(acn,pwd))
            tup=curobj.fetchone()
            conobj.close
            if tup==None:
                messagebox.showerror('login','invalid acn/pass')
            else:
                frm.destroy()
                welcome_screen()

    def reset():
        e_acn.delete(0,'end')
        e_pass.delete(0,'end')
        e_acn.focus()

    lbl_acn=Label(frm,text='ACN',font=('',20,'bold'),bg='pink')
    lbl_acn.place(relx=.35,rely=.1)

    e_acn=Entry(frm,font=('',15),bd=5)
    e_acn.place(relx=.45,rely=.1)

    lbl_pass=Label(frm,text='Pass',font=('',20,'bold'),bg='pink')
    lbl_pass.place(relx=.35,rely=.2)

    e_pass=Entry(frm,font=('',15),bd=5)
    e_pass.place(relx=.45,rely=.2)

    btn_login=Button(frm,command=login,text='login',font=('',15,'bold'),bd=5)
    btn_login.place(relx=.478,rely=.3)

    btn_reset=Button(frm,command=reset,text='reset',font=('',15,'bold'),bd=5)
    btn_reset.place(relx=.55,rely=.3)

    btn_newuser=Button(frm,command=newuser,text='new_users',font=('',15,'bold'),bd=5)
    btn_newuser.place(relx=.41,rely=.45)

    btn_frgtpwd=Button(frm,command=forgot,text='forgot_password',font=('',15,'bold'),bd=5)
    btn_frgtpwd.place(relx=.51,rely=.45)

def newuser_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)

    def newacn():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        bal=0
        date=time.strftime("%d-%m-%Y")

        conobj=sqlite3.connect(database='sqlite')
        curobj=conobj.cursor()
        curobj.execute('insert into acn (acn_name, acn_pass, acn_email,acn_mob,acn_bal,acn_opendate) values(?,?,?,?,?,?)',(name,pwd,email,mob,bal,date))
        conobj.commit()
        conobj.close()

        conobj=sqlite3.connect(database='sqlite')
        curobj=conobj.cursor()
        curobj.execute('select max(acn_acno) from acn')
        tup=curobj.fetchone()
        conobj.close()

        messagebox.showinfo('New account',f'account created, acn:{tup[0]}')

    def back():
        frm.destroy()
        main_screen()

    btn_back=Button(frm,command=back,text='back',font=('',15,'bold'),bd=5)
    btn_back.place(relx=0,rely=0)

    lbl_name=Label(frm,text='Name',font=('',20,'bold'),bg='pink')
    lbl_name.place(relx=.35,rely=.1)

    e_name=Entry(frm,font=('',15),bd=5)
    e_name.place(relx=.45,rely=.1)

    lbl_pass=Label(frm,text='Pass',font=('',20,'bold'),bg='pink')
    lbl_pass.place(relx=.35,rely=.2)

    e_pass=Entry(frm,font=('',15),bd=5)
    e_pass.place(relx=.45,rely=.2)

    lbl_email=Label(frm,text='E-mail',font=('',20,'bold'),bg='pink')
    lbl_email.place(relx=.35,rely=.3)

    e_email=Entry(frm,font=('',15),bd=5)
    e_email.place(relx=.45,rely=.3)

    lbl_mob=Label(frm,text='Mob',font=('',20,'bold'),bg='pink')
    lbl_mob.place(relx=.35,rely=.4)

    e_mob=Entry(frm,font=('',15),bd=5)
    e_mob.place(relx=.45,rely=.4)

    btn_submit=Button(frm,command=newacn,text='Submit',font=('',15,'bold'),bd=5)
    btn_submit.place(relx=.5,rely=.6)

def forgot_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)
    
    def back():
        frm.destroy()
        main_screen()

    def forgot():
        email=e_email.get()
        mob=e_mob.get()
        acn=e_acn.get()
        
        conobj=sqlite3.connect(database='sqlite')
        curobj=conobj.cursor()
        curobj.execute('select acn_pass from acn where acn_acno=? and acn_email=? and acn_mob=?',(acn,email,mob))
        tup=curobj.fetchone()
        conobj.close()

        messagebox.showinfo('Password',f'Pass: {tup[0]}')
        
        
    btn_back=Button(frm,command=back,text='back',font=('',15,'bold'),bd=5)
    btn_back.place(relx=0,rely=0)
    
    lbl_email=Label(frm,text='E-mail',font=('',20,'bold'),bg='pink')
    lbl_email.place(relx=.35,rely=.1)

    e_email=Entry(frm,font=('',15),bd=5)
    e_email.place(relx=.45,rely=.1)

    lbl_mob=Label(frm,text='Mob',font=('',20,'bold'),bg='pink')
    lbl_mob.place(relx=.35,rely=.2)

    e_mob=Entry(frm,font=('',15),bd=5)
    e_mob.place(relx=.45,rely=.2)

    lbl_acn=Label(frm,text='ACN',font=('',20,'bold'),bg='pink')
    lbl_acn.place(relx=.35,rely=.3)

    e_acn=Entry(frm,font=('',15),bd=5)
    e_acn.place(relx=.45,rely=.3)

    btn_submit=Button(frm,command=forgot,text='Submit',font=('',15,'bold'),bd=5)
    btn_submit.place(relx=.5,rely=.5)

def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.87)
    
    conobj=sqlite3.connect(database='sqlite')
    curobj=conobj.cursor()
    curobj.execute('select * from acn where acn_acno=?',(acn,))
    tup=curobj.fetchone()
    conobj.close()
    
    def logout():
        frm.destroy()
        main_screen()
    
    def details():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.6,relheight=.7)

        conobj=sqlite3.connect(database='sqlite')
        curobj=conobj.cursor()
        curobj.execute('select * from acn where acn_acno=?',(acn,))
        tup=curobj.fetchone()
        conobj.close()

        lbl_acn=Label(ifrm,text=f'Account NO= {tup[0]}',font=('',20,'bold'),bg='white')
        lbl_acn.place(relx=.2,rely=.15)

        lbl_bal=Label(ifrm,text=f'Your ACN Bal= {tup[5]}',font=('',20,'bold'),bg='white')
        lbl_bal.place(relx=.2,rely=.25)

        lbl_date=Label(ifrm,text=f'Account opendate= {tup[6]}',font=('',20,'bold'),bg='white')
        lbl_date.place(relx=.2,rely=.35)

        lbl_screen=Label(ifrm,text='This is details screen',font=('',20,'bold'),bg='white')
        lbl_screen.pack()

    def deposite():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.6,relheight=.7)

        def depacn():
            conobj=sqlite3.connect(database='sqlite')
            curobj=conobj.cursor()
            amnt=float(e_amnt.get())
            curobj.execute('update acn set acn_bal=acn_bal+? where acn_acno=?',(amnt,acn))
            conobj.commit()
            conobj.close()

            messagebox.showinfo('deposite',f'{amnt} deposited')

        lbl_screen=Label(ifrm,text='This is deposite screen',font=('',20,'bold'),bg='white')
        lbl_screen.pack()

        lbl_amnt=Label(ifrm,text='Amount',font=('',20,'bold'),bg='white')
        lbl_amnt.place(relx=.3,rely=.15)

        e_amnt=Entry(ifrm,font=('',15),bd=5)
        e_amnt.place(relx=.45,rely=.15)

        btn_submit=Button(ifrm,command=depacn,text='Submit',font=('',15,'bold'),bd=5)
        btn_submit.place(relx=.5,rely=.3)

    def withdraw():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.6,relheight=.7)

        def withdrawacn():
            conobj=sqlite3.connect(database='sqlite')
            curobj=conobj.cursor()
            amnt=float(e_amnt.get())
            curobj.execute('update acn set acn_bal=acn_bal-? where acn_acno=?',(amnt,acn))
            conobj.commit()
            conobj.close()

            messagebox.showinfo('withdraw',f'{amnt} withdrawl')

        lbl_screen=Label(ifrm,text='This is withdraw screen',font=('',20,'bold'),bg='white')
        lbl_screen.pack()

        lbl_amnt=Label(ifrm,text='Amount',font=('',20,'bold'),bg='white')
        lbl_amnt.place(relx=.3,rely=.15)

        e_amnt=Entry(ifrm,font=('',15),bd=5)
        e_amnt.place(relx=.45,rely=.15)

        btn_submit=Button(ifrm,command=withdrawacn,text='Submit',font=('',15,'bold'),bd=5)
        btn_submit.place(relx=.5,rely=.3)
        
    def update():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.6,relheight=.7)

        def updateacn():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()

            conobj=sqlite3.connect(database='sqlite')
            curobj=conobj.cursor()
            curobj.execute('update acn set acn_name=?,acn_pass=?,acn_email=?,acn_mob=?',(name,pwd,email,mob))
            conobj.commit()
            conobj.close()
            frm.destroy()
            welcome_screen()

            messagebox.showinfo('Update','Update Successfully')

        lbl_name=Label(ifrm,text='Name',font=('',20,'bold'),bg='white')
        lbl_name.place(relx=.15,rely=.15)

        e_name=Entry(ifrm,font=('',15),bd=5)
        e_name.place(relx=.15,rely=.23)

        lbl_pass=Label(ifrm,text='Pass',font=('',20,'bold'),bg='white')
        lbl_pass.place(relx=.55,rely=.15)

        e_pass=Entry(ifrm,font=('',15),bd=5)
        e_pass.place(relx=.55,rely=.23)

        lbl_email=Label(ifrm,text='E-mail',font=('',20,'bold'),bg='white')
        lbl_email.place(relx=.15,rely=.43)

        e_email=Entry(ifrm,font=('',15),bd=5)
        e_email.place(relx=.15,rely=.51)

        lbl_mob=Label(ifrm,text='Mob',font=('',20,'bold'),bg='white')
        lbl_mob.place(relx=.55,rely=.43)

        e_mob=Entry(ifrm,font=('',15),bd=5)
        e_mob.place(relx=.55,rely=.51)

        btn_update=Button(ifrm,command=updateacn,text='Update',font=('',15,'bold'),bd=5)
        btn_update.place(relx=.43,rely=.7)
            
        lbl_screen=Label(ifrm,text='This is update screen',font=('',20,'bold'),bg='white')
        lbl_screen.pack()

        conobj=sqlite3.connect(database='sqlite')
        curobj=conobj.cursor()
        curobj.execute('select * from acn where acn_acno=?',(acn))
        tup=curobj.fetchone()
        conobj.close()

        e_name.insert(0,tup[1])
        e_pass.insert(0,tup[2])
        e_email.insert(0,tup[3])
        e_mob.insert(0,tup[4])
        e_name.focus()

    def admin():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.6,relheight=.7)

        def dltacn():
            acno=e_acno.get()
            pwd=e_pass.get()

            conobj=sqlite3.connect(database='sqlite')
            curobj=conobj.cursor()
            curobj.execute('delete from acn where acn_acno=? and acn_pass=?',(acno,pwd))
            conobj.commit()
            conobj.close()
            frm.destroy()
            main_screen()

            messagebox.showinfo('Delete','Delete Successfully')

        lbl_screen=Label(ifrm,text='This is Admin screen',font=('',20,'bold'),bg='white')
        lbl_screen.pack()

        btn_dlt=Button(ifrm,command=dltacn,text='Delete',font=('',15,'bold'),bd=5)
        btn_dlt.place(relx=.43,rely=.5)

        lbl_acno=Label(ifrm,text='Account No',font=('',20,'bold'),bg='white')
        lbl_acno.place(relx=.15,rely=.15)

        e_acno=Entry(ifrm,font=('',15),bd=5)
        e_acno.place(relx=.15,rely=.23)

        lbl_pass=Label(ifrm,text='Pass',font=('',20,'bold'),bg='white')
        lbl_pass.place(relx=.55,rely=.15)

        e_pass=Entry(ifrm,font=('',15),bd=5)
        e_pass.place(relx=.55,rely=.23)

        conobj=sqlite3.connect(database='sqlite')
        curobj=conobj.cursor()
        curobj.execute('select * from acn where acn_acno=?',(acn))
        tup=curobj.fetchone()
        conobj.close()

        e_acno.delete(0,tup[0])
        e_pass.delete(0,tup[2])
    
    btn_logout=Button(frm,command=logout,text='logout',font=('',15,'bold'),bd=5)
    btn_logout.place(relx=.94,rely=0)

    lbl_wlcm=Label(frm,text=f'Welcome, {tup[1]} ',font=('',20,'bold'),bg='pink')
    lbl_wlcm.place(relx=0,rely=0)

    btn_details=Button(frm,command=details,text='Check Details',width=12,font=('',15,'bold'),bd=5)
    btn_details.place(relx=0,rely=.2)

    btn_deposite=Button(frm,command=deposite,text='Deposite amnt',width=12,font=('',15,'bold'),bd=5)
    btn_deposite.place(relx=0,rely=.3)

    btn_withdraw=Button(frm,command=withdraw,text='Withdraw amnt',width=12,font=('',15,'bold'),bd=5)
    btn_withdraw.place(relx=0,rely=.4)

    btn_update=Button(frm,command=update,text='Update Details',width=12,font=('',15,'bold'),bd=5)
    btn_update.place(relx=0,rely=.5)

    btn_admin=Button(frm,command=admin,text='Admin acnt',width=12,font=('',15,'bold'),bd=5)
    btn_admin.place(relx=0,rely=.6)
        

main_screen()
win.mainloop()


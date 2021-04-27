from tkinter import *
from ministatement import Ms
import time
from os import system
from tkinter import messagebox
import sqlite3 as db


class ATM:
    def __init__(self):
        self.balance = 1000
        self.win = Tk()
        self.win.title("ATM")
        self.win.iconbitmap('atm.ico')

        # for database connectivity
        self.con = db.connect("atm.db")
        self.cur = self.con.cursor()
# --------------------------------------------------------------------------------
        # code to position the window at the centre of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        centre_x = int(width/2)
        centre_y = int(height/2)
        window_width = 800
        window_height = 400
        x = int(centre_x-window_width/2)
        y = int(centre_y-window_height/2)
        self.win.geometry(f'{window_width}x{window_height}+{x}+{y}')
# ---------------------------------------------------------------------------------
        self.win.config(bg="black")
        self.win.resizable(0, 0)

        # Frame 'f0' for main parent frame of a whole window
        self.f0 = Frame(self.win, bg="black")
        self.f0.pack(fill=BOTH, expand=1)

        # label 'l3' for displaying time and date
        self.l3 = Label(self.f0, text='', bg='black',
                        fg='violet', font=('Georgia 18 bold'))
        self.l3.place(x=500, y=320)

    def welcome_window(self):

        self.f1 = Frame(self.f0, bg="Purple", height=150)
        self.f1.pack(fill=BOTH)

        self.l1 = Label(self.f1, text="Welcome to ATM", bg="purple",
                        fg="black", font=("Georgia 32 bold"))
        self.l1.pack(pady=20)

        self.l2 = Label(self.f0, text="Enter your PIN:", bg="purple",
                        fg="black", font=("Georgia 25 bold"))
        self.l2.pack(pady=40)

        self.e1 = Entry(self.f0, bg="violet", fg="black",
                        font=("Helvetica 15 bold"))
        self.e1.pack()

        self.b1 = Button(self.f0, text="Continue", bg="purple",
                         fg="black", font=("Helvetica 15 bold"), command=self.validate)
        self.b1.pack(pady=20)

        self.b1.bind("<Enter>", machine1.button1_hover)
        self.b1.bind("<Leave>", machine1.button1_hover_reverse)

        self.b0 = Button(self.f0, text="Create Account?", bg="black", fg="violet", font=(
            "Helvetica 15 bold"), bd=0, command=self.create_account)
        self.b0.place(x=10, y=340)
        
        self.b0.bind("<Enter>", machine1.button0_hover)
        self.b0.bind("<Leave>", machine1.button0_hover_reverse)


    def time_and_date(self):
        day = time.strftime('%A')
        hour = time.strftime('%I')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')
        day = time.strftime('%A')
        meridian = time.strftime('%p')
        date = time.strftime('%d-%b-%Y')

        self.l3.config(text=hour+':'+minutes+':'+seconds +
                       ' '+meridian+'\n'+date+', '+day)
        self.l3.after(1000, self.time_and_date)

    def button0_hover(self, e):
        self.b0.config(fg="white")

    def button0_hover_reverse(self, e):
        self.b0.config(fg="violet")

    def button1_hover(self, e):
        self.b1.config(fg="white")

    def button1_hover_reverse(self, e):
        self.b1.config(fg="black")

    def button2_hover(self, e):
        self.b2.config(fg="white")

    def button2_hover_reverse(self, e):
        self.b2.config(fg="black")

    def button3_hover(self, e):
        self.b3.config(fg="white")

    def button3_hover_reverse(self, e):
        self.b3.config(fg="black")

    def button4_hover(self, e):
        self.b4.config(fg="white")

    def button4_hover_reverse(self, e):
        self.b4.config(fg="black")

    def button5_hover(self, e):
        self.b5.config(fg="white")

    def button5_hover_reverse(self, e):
        self.b5.config(fg="black")

    def button6_hover(self, e):
        self.b6.config(fg="white")

    def button6_hover_reverse(self, e):
        self.b6.config(fg="violet")

    def validate(self):
        try:
            query = "select * from user where Pin={}".format(int(self.e1.get()))
            self.cur.execute(query)
            result = self.cur.fetchall()

            if result:
                self.current_user=result[0][0]
                response = messagebox.showinfo("PIN Status", "Your have logged in successfully! Press OK to continue!")
                self.home_window(self.current_user)
            
            else:
                messagebox.showerror("PIN Status", "Your PIN is incorrect! Please try again...!")

        except:
            pass

        
    def home_window(self,current_user):
        self.f0.pack_forget()

        self.f2 = Frame(self.win, bg="black")
        self.f2.pack(fill=BOTH, expand=1)

        self.f3 = Frame(self.f2, bg="Purple", height=150)
        self.f3.pack(fill=BOTH)

        self.f4 = Frame(self.f2, bg="Purple", width=550, height=220)
        self.f4.place(x=220, y=150)

        self.l4 = Label(self.f3, text="Welcome to ATM", bg="purple",
                        fg="black", font=("Georgia 32 bold"))
        self.l4.pack(pady=20)

        self.l0 = Label(self.f3, text=current_user, bg="purple",
                        fg="violet", font=("Georgia 20 bold"))
        self.l0.pack()

        self.b2 = Button(self.f2, text="Balance", bg="purple", width=10,
                         fg="black", font=("Helvetica 15 bold"), command=lambda:self.balance_btn(current_user))
        self.b2.place(x=50, y=150)

        self.b3 = Button(self.f2, text="Withdraw", bg="purple", width=10,
                         fg="black", font=("Helvetica 15 bold"), command=lambda:self.withdraw_btn(current_user))
        self.b3.place(x=50, y=210)

        self.b4 = Button(self.f2, text="Deposit", bg="purple", width=10,
                         fg="black", font=("Helvetica 15 bold"), command=lambda:self.deposit_btn(current_user))
        self.b4.place(x=50, y=270)

        self.b5 = Button(self.f2, text="Statement", bg="purple", width=10,
                         fg="black", font=("Helvetica 15 bold"), command=lambda:self.get_statement(current_user))
        self.b5.place(x=50, y=330)

        self.b6 = Button(self.f3, text="Exit", bg="black", width=5,
                         fg="white", font=("Helvetica 12 bold"), command=self.exit)
        self.b6.place(x=720, y=90)

        self.b2.bind("<Enter>", machine1.button2_hover)
        self.b2.bind("<Leave>", machine1.button2_hover_reverse)

        self.b3.bind("<Enter>", machine1.button3_hover)
        self.b3.bind("<Leave>", machine1.button3_hover_reverse)

        self.b4.bind("<Enter>", machine1.button4_hover)
        self.b4.bind("<Leave>", machine1.button4_hover_reverse)

        self.b5.bind("<Enter>", machine1.button5_hover)
        self.b5.bind("<Leave>", machine1.button5_hover_reverse)

    def exit(self):
        self.f2.pack_forget()
        self.e1.delete(0, END)
        self.f0.pack(fill=BOTH, expand=1)

    def balance_btn(self,current_user):
        query=f"select balance from user where Username='{current_user}'"
        self.cur.execute(query)
        result=self.cur.fetchone()
        if result[0]==None:
            balance=0
        else:
            balance=result[0]

        self.f4 = Frame(self.f2, bg="Purple", width=550, height=220)
        self.f4.place(x=220, y=150)
        
        self.l5 = Label(self.f4, text="Your current balance is: {}".format(balance), bg="purple", fg="white", font=("Georgia 20 bold"))

        self.l5.place(x=80, y=100)

    def withdraw_btn(self,current_user):
        query=f"select balance from user where Username='{current_user}'"
        self.cur.execute(query)
        result=self.cur.fetchone()
        if result[0]==None:
            balance=0
        else:
            balance = result[0]

        self.f4 = Frame(self.f2, bg="Purple", width=550, height=220)
        self.f4.place(x=220, y=150)

        self.l5 = Label(self.f4, text="Enter the amount to withdraw:",
                        bg="purple", fg="white", font=("Georgia 20 bold"))
        self.l5.place(x=80, y=50)

        self.e2 = Entry(self.f4, bg="violet", fg="black",
                        font=("Helvetica 15 bold"))
        self.e2.place(x=85, y=100)

        self.b6 = Button(self.f4, text="Continue", bg="black", width=10,
                         fg="violet", font=("Helvetica 12 bold"), command=lambda:self.withdraw_amount(balance,current_user))
        self.b6.place(x=350, y=100)

        self.b6.bind("<Enter>", machine1.button6_hover)
        self.b6.bind("<Leave>", machine1.button6_hover_reverse)

    def deposit_btn(self,current_user):
        query = f"select balance from user where Username='{current_user}'"
        self.cur.execute(query)
        result = self.cur.fetchone()
        if result[0] == None:
            balance = 0
        else:
            balance = result[0]

        self.f4 = Frame(self.f2, bg="Purple", width=550, height=220)
        self.f4.place(x=220, y=150)

        self.l5 = Label(self.f4, text="Enter the amount to deposit:",
                        bg="purple", fg="white", font=("Georgia 20 bold"))
        self.l5.place(x=80, y=50)

        self.e2 = Entry(self.f4, bg="violet", fg="black",
                        font=("Helvetica 15 bold"))
        self.e2.place(x=85, y=100)

        self.b6 = Button(self.f4, text="Continue", bg="black", width=10,
                         fg="violet", font=("Helvetica 12 bold"), command=lambda:self.deposit_amount(balance,current_user))
        self.b6.place(x=350, y=100)

        self.b6.bind("<Enter>", machine1.button6_hover)
        self.b6.bind("<Leave>", machine1.button6_hover_reverse)

    def withdraw_amount(self,balance,current_user):
        self.l6 = Label(self.f4, text="",
                        bg="purple", fg="white", font=("Georgia 20 bold"))
        self.l6.place(x=60, y=160)
        try:
            amount = self.e2.get()
            if balance >= int(amount):
                balance -= int(amount)
                query="update user set balance=:balance where Username=:username"
                insert_data={'balance':balance,'username':current_user}
                self.cur.execute(query,insert_data)
                self.con.commit()
                message=f"Your account is debited by {amount}!"
                rem_amt=f" Remaining balance is: {balance}."
                self.l6.config(text=message)
                with open(f"{current_user}.txt",'a') as file:
                    timestamp = time.strftime("On %d-%b-%Y at %T ")
                    data=timestamp+message+rem_amt
                    file.write(data+"\n")
                    file.close()
                    
            else:
                message = "Balance is insufficient!"
                rem_amt=f" Remaining balance is: {balance}."
                self.l6.config(text=message)
                with open(f"{current_user}.txt", 'a') as file:
                    timestamp = time.strftime("On %d-%b-%Y at %T ")
                    data = timestamp+message+rem_amt
                    file.write(data+"\n")
                    file.close()
        except:
            pass

    def deposit_amount(self,balance,current_user):
        self.l6 = Label(self.f4, text="",
                        bg="purple", fg="white", font=("Georgia 20 bold"))
        self.l6.place(x=60, y=160)
        try:
            amount = self.e2.get()
            balance += int(amount)
            query="update user set balance=:balance where Username=:username"
            insert_data={'balance':balance,'username':current_user}
            self.cur.execute(query,insert_data)
            self.con.commit()
            if query:
                message = f"Your account is credited by {amount}!"
                total_amt=f" Total balance is: {balance}."
                self.l6.config(text=message)
                with open(f"{current_user}.txt", 'a') as file:
                    timestamp = time.strftime("On %d-%b-%Y at %T ")
                    data = timestamp+message+total_amt
                    file.write(data+"\n")
                    file.close()
            else:
                message="Amount can't be credited...!"
                total_amt=f" Total balance is: {balance}."
                self.l6.config(text=message)
                with open(f"{current_user}.txt", 'a') as file:
                    timestamp = time.strftime("On %d-%b-%Y at %T ")
                    data = timestamp+message+total_amt
                    file.write(data+"\n")
                    file.close()
        except:
            pass

    def create_account(self):
        self.f0.pack_forget()

        self.f5 = Frame(self.win, bg="black")
        self.f5.pack(fill=BOTH, expand=1)

        self.f6 = Frame(self.f5, bg="Purple", height=150)
        self.f6.pack(fill=BOTH)

        self.l0 = Label(self.f6, text="Welcome to ATM", bg="purple",
                        fg="black", font=("Georgia 32 bold"))
        self.l0.pack(pady=20)

        self.l7 = Label(self.f5, text="Enter your name:", bg="black",
                        fg="purple", font=("Georgia 25 bold"))
        self.l7.place(x=20, y=150)

        self.e3 = Entry(self.f5, bg="violet", fg="black",
                        font=("Helvetica 20 bold"))
        self.e3.place(x=350, y=155)

        self.l8 = Label(self.f5, text="Enter your PIN:", bg="black",
                        fg="purple", font=("Georgia 25 bold"))
        self.l8.place(x=20, y=210)

        self.e4 = Entry(self.f5, bg="violet", fg="black",
                        font=("Helvetica 20 bold"))
        self.e4.place(x=350, y=215)

        self.b7 = Button(self.f5, text="Create", bg="purple", width=10,
                         fg="violet", font=("Helvetica 19 bold"), command=self.creation)
        self.b7.place(x=350, y=300)

        self.b8 = Button(self.f5, text="Back to Login", bg="purple", width=12,
                         fg="violet", font=("Helvetica 19 bold"), command=self.back_to_home)
        self.b8.place(x=550, y=300)

    def creation(self):
        self.name = self.e3.get()
        self.pin = int(self.e4.get())
        query = "insert into user (Username,Pin)values (:name, :pin)"
        insert_data = {"name": self.name, "pin": self.pin}
        self.cur.execute(query, insert_data)
        self.con.commit()
        if query:
            messagebox.showinfo(
                "Account Status", "Account created successfully!")
        else:
            messagebox.showerror("Account Status", "Operation Failed!")

    def back_to_home(self):
        self.f5.pack_forget()
        self.f0.pack(fill=BOTH,expand=1)

    def get_statement(self,current_user):
        mini=Ms()
        mini.get_mini(current_user)
        
machine1 = ATM()
machine1.welcome_window()
machine1.time_and_date()
machine1.win.mainloop()

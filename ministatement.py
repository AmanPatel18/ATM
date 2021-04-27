from tkinter import *
from tkinter import Listbox
class Ms:

    def __init__(self):
        self.win=Tk()
        self.win.title('Account Statement')
        self.win.geometry("500x250")
        self.win.config(bg="purple")
        self.win.iconbitmap('atm.ico')
        self.win.resizable(0,0)
        # declare frame and scrollbar

        self.my_frame = Frame(self.win,bg="violet")
        self.my_scrollbar=Scrollbar(self.my_frame,orient=VERTICAL)

        # declraing Listbox

        self.list_box=Listbox(self.my_frame,width=100,yscrollcommand=self.my_scrollbar.set,bg="black",fg="white")

        #config scroll bar
        self.my_scrollbar.config(command=self.list_box.yview)
        self.my_scrollbar.pack(side=RIGHT,fill=Y)
        self.my_frame.pack(pady=15)
        self.list_box.pack(pady=15)

    def get_mini(self,user):
        # adding items in Listbox
        with open(f"{user}.txt") as file:
            mylist=file.readlines()
            for item in mylist:
                self.list_box.insert(END,item)
                self.list_box.itemconfigure(END, selectbackground="violet",selectforeground="black",activestyle=None)
            file.close()

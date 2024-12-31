from tkinter import*
from tkinter import messagebox
from subprocess import call



class Login:
    #Login system...
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")
        
        #Login Frame...
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400) 

        title= Label(Frame_login, text="Login", font=("impact", 35, "bold"), fg="teal", bg="white").place(x=90,y=30)   
        subtittle= Label(Frame_login, text="User Login", font=("times new roman", 15, "bold"), fg="black", bg="white").place(x=90,y=100) 

        #Username
        lbl_user= Label(Frame_login, text="Username", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(x=90,y=140) 
        self.username = Entry(Frame_login, font=("times new roman", 15, "bold"), fg="gray", bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320,height=35)

        #Password
        lbl_password= Label(Frame_login, text="Password", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(x=90,y=210) 
        self.password = Entry(Frame_login, font=("times new roman", 15, "bold"), fg="gray", bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320,height=35)

        #Button
        submit = Button(Frame_login,command=self.check_function,cursor="hand2", text="Login",bd=0, font=("times new roman", 15, "bold"), bg="teal", fg="white").place(x=90,y=280, width=180, height=40)

    def check_function(self):
            if self.username.get()==""or self.password.get()=="":
                messagebox.showerror("Error","Check again...", parent=self.root)
            elif self.username.get()!="library1"or self.password.get()!="1234":
                messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            else:
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")
                call (["python","library.py"])
                root.destroy()
                
                   
root= Tk()
obj = Login(root)
root.mainloop()




from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Login_Window:
    def __init__(self,root):
      self.root=root
      self.root.title("Login")
      self.root.geometry("1550x800+0+0")

      self.bg=ImageTk.PhotoImage(file=r"D:\Photgraphs and Videos\Family Members Photographs\SAMARTH\20211015_183020.jpg")
      lbl_bg=Label(self.root,image=self.bg)
      lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

      frame=Frame(self.root,bg="skyblue")
      frame.place(x=610,y=170,width=340,height=450)

      img1=Image.open(r"D:\Photgraphs and Videos\Family Members Photographs\SAMARTH\20211015_183020.jpg")
      img1=img1.resize((100,100),Image.ANTIALIAS)  
      self.photoimage1=ImageTk.PhotoImage(img1)
      lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
      lblimg1.place(x=730,y=175,width=100,height=90)
      
      get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="skyblue")
      get_str.place(x=95,y=100)

      #UserName
      username=lbl=Label(frame,text="Username: ",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
      username.place(x=70,y=155)

      self.txtuser =ttk.Entry(frame,font=("times new roman",15,"bold"))
      self.txtuser.place(x=40,y=180,width=270)

      #Password
      password=lbl=Label(frame,text="Password: ",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
      password.place(x=70,y=225)

      self.txtpass =ttk.Entry(frame,font=("times new roman",15,"bold"))
      self.txtpass.place(x=40,y=250,width=270)

      #IconImages
      img2=Image.open(r"D:\Photgraphs and Videos\Family Members Photographs\SAMARTH\20211015_183020.jpg")
      img2=img2.resize((25,25),Image.ANTIALIAS)  
      self.photoimage2=ImageTk.PhotoImage(img2)
      lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
      lblimg1.place(x=650,y=323,width=25,height=25)

      img3=Image.open(r"D:\Photgraphs and Videos\Family Members Photographs\SAMARTH\20211015_183020.jpg")
      img3=img3.resize((25,25),Image.ANTIALIAS)  
      self.photoimage3=ImageTk.PhotoImage(img3)
      lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
      lblimg1.place(x=650,y=393,width=25,height=25)

      #loginbtn
      loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
      loginbtn.place(x=110,y=300,width=120,height=35)

      #registerbtn
      registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="skyblue",activebackground="skyblue",activeforeground="white")
      registerbtn.place(x=15,y=350,width=160)

      #forgotpassbtn
      forgotbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="skyblue",activebackground="skyblue",activeforeground="white")
      forgotbtn.place(x=10,y=370,width=160)

    def login(self):
         if self.txtuser.get()=="" or self.txtpass.get()=="":
             messagebox.showerror("Error","Enter All Credentials Required")
         elif self.txtuser.get()=="Admin" and self.txtpass.get()=="Admin":
             messagebox.showinfo("Success","Login SucccessFully")
         else:
             messagebox.showerror("Invalid","Enter Correct Credentials")    


if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()   
    
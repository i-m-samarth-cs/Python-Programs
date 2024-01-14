#==============Attendance Sheet===============

# 1) Need Student ID Copy => my_cursor.execute("Select Dep form student_id="+str(id))
#                            d = my_cursor.fetchone()
#                            d="+"join(d)

# 2) Paste below the same statement
# 3) Change    my_cursor.execute("Select Student_id  form Student_id="+str(id))
#                            i = my_cursor.fetchone()
#                            i="+"join(i)

# 4) Add new statement above cv2.putText() in the if confidence>77 block
#    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

# 5)Create new method above face_recog(self) and below b1_1.place()

#=============attendance==============
def mark_attendance(self,i,r,n,d):          #i,r,n,d are arguments of cv2.putText(img,f"ID:{i},{r},{n},{d}
    with open("kiran.csv","r+",newline="\n") as f:
        myDataList=f.readlines()
        name_list=[]
        for line in myDataList:
            entry==line.split((","))
            name_list.append(entry[0])
        if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
            
            
        # used for non repetative attendance
        # from Data and time use => from time import strftime
        # from datetime import datetime
            now=datetime.now()
            d1=now.strftime("%d/%m/%Y")   # used for date month and Year     
            dtString=now.strftime("%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")
            
            
# 6) Call the function at if confidence>77 block before else
        self.mark_attendance(i,r,n,d)

# 7)Create new file with name kiran.csv in the folder part same name as argument
# 8)Error when camera is not opening (i)Open mysql (ii)Open student table click on setting 2nd Icon (iii)Change the datatype of student_id from INT to varchar(45)
#   (iv)Apply then Finish   Attendance would be saved in .csv file and stored in the excel file

#================CREATE FILE attendance.py================
from tkinter import*
from tkinter import ttk   # Contains Scrollbar
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata[] # Global Variable
class Attendance :
    def__init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #================Variables=================#
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
#--Code for Images
        # first imag

        img=Image.open(r"college_images\smart-attendance.jpg")  #URL for Image
        img=img.resize((800,200), Image.ANTIALIAS) 
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # second image
        img1=Image.open(r"college_images\clg.jpg")              #URL for Image
        img1=img1.resize((800,200), Image. ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)   
        
        # background image
        img3-Image.open(r" college_images\bgimg.jpg")
        img3-img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3-ImageTk. PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200, width=1530, height=710)
        
        title_lbl=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",3)
        title_lbl.place (x=0,y=0, width=1530,height=45) 
        
        main_frame=Frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        
        # Left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",3))
        Left_frame.place(x=10,y=10,width=720,height=500)
        
        # Paste Image in Left label Frame
        img_left=Image.open(r"college_images\AdobeStock_8932892894.jpeg") # IMG URL
        img_left=img_left.resize(720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        # Create Frame
        left_inside_frame=Frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        # Label Entries
        #Attendance Id
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(rows=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Roll No
        rollLabel=Label(left_inside_frame,text="Roll: ",bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)
        
        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        # Name
        nameLabel=Label(left_inside_frame, text="Name:",bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)
        
        atten_name=ttk. Entry (left_inside_frame, width=22,textvariable=self.var_atten_name, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1,pady=8)

        # Department
        depLabel=Label(left_inside_frame, text="Department:",bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)
        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # time
        timeLabel=Label(left_inside_frame,text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_time, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel=Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)
        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        # attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)
        self.atten_status=ttk.Combobox (left_inside_frame, width=20,textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1,pady=8)
        self.atten_status.current(0)
        
        # Removed the function which is not created 
        # buttons frame
        btn_frame=Frame (left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place (x=0,y=300, width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv", width=17,command=self.importCsv, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn=Button(btn_frame,text="Export csv",width=17,command=self.exportCsv, font=("times new roman",13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn=Button(btn_frame, text="Update", width=17, font=("times new roman",13, "bold"), bg="blue",fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn=Button (btn_frame, text="Reset", width=17,command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
        # Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",3))
        Right_frame.place(x=750,y=10,width=720,height=500)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        
        #========Scrollbar and Table=======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","data","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonReleased>",self.get_cursor)
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()

# 9)Import the File Attendance.py into main file
# Below the from face_recognition import Face_Recognition
from attendance import Attendance # Attendance is class

# 10)Go at last in main file below function face_data(self):
def attendance_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Attendance(self.new_window)

# 11)Go to Attendance Button and call the Function at b1_1=Button(bg_img,image=self.photoimg6,cursor="hand2",)
b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
b1.place(x=800,y=100,width=220,height=220)

b1_1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data,font=("times new roman",13,"bold"),bg="white")
b1_1.place(x=800,y=300,width=220,height=40)

# 12)Import the data from .csv to table
# Create method in the attendance.py file below self.AttendanceReportTable.pack(fill=BOTH,expand=1)

def fetchData(self,rows):  # To fetch and display data
    self.AttendanceReportTable.delete(*self.AttendanceReportTable.getchildren())
    for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)
        

# 13)Function to bring data from .csv file
# Create below fetchData() function

def importCsv(self):
    #Create a Global variable above class Attendance @Line no 52
    global mydata
    mydata.clear()
    #import os
    #import csv
    #from tkinter import filedialog                                                 # *csv extension of CSV
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
    with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")    #Delimiter is used as separator
        for i in csvread:
            mydata.append(i)
        self.fetchData()
    
# 14) Call the Method at Import CSV Button below btn_frame.place()
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv, width=17, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0)
        
# 15) While we clicked on Import CSV FileDialog will be opened
# 16) Method to export csv folder create method below the importCsv method
# Export CSV
def exportCsv(self):
    try:
        if len(mydata)<1:
            messagebox.showerror("No Data","No Data Found for Exporting",parent=self.root)
        return False
    fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
    with open(fln,mode="w",newline="") as myfile:
        exp_write=csv.writerow(myfile,delimeter=",")
        for i in mydata:
            exp_write.writerow(i)
        messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
    except Exception as e:
        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

# 17) Call the Method at Export CSV Button below save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,text="Export csv",width=17,command=self.exportCsv, font=("times new roman",13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=1) 
        
# 18) Create Variables in Attendance Class below self.root.title("Face Recognition System") Line no 62
#     Add variables at buttons to show data using textvariable=self.var_atten_id

# 19) Create Function to show Data

def get_cursor(self,event=""):
    cursor_row=self.AttendanceReportTable.focus()
    content=self.AttendanceReportTable(cursor_row)
    rows=content['values']
    self.var_atten_id.set(rows[0])
    self.var_atten_roll.set(rows[1])
    self.var_atten_name.set(rows[2])
    self.var_atten_dep.set(rows[3])
    self.var_atten_time.set(rows[4])
    self.var_atten_date.set(rows[5])
    self.var_atten_attendance.set(rows[6])

# 20) Bind the method below self.AttendanceReportTable.pack()  Line No = 226

# 21) Function of Reset Data

def reset_data(self):
    self.var_atten_id.set("")
    self.var_atten_roll.set("")
    self.var_atten_name.set("")
    self.var_atten_dep.set("")
    self.var_atten_time.set("")
    self.var_atten_date.set("")
    self.var_atten_attendance.set("")
    
# 22)Call reset_data method at reset button
    reset_btn=Button (btn_frame, text="Reset", width=17,command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
    reset_btn.grid(row=0, column=3)

#=============DEVELOPER SECTION=============#
# 23)Create new page developer.py

from tkinter import*
from tkinter import ttk   # Contains Scrollbar
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def__init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
    
    title_lbl=label=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
    title_lbl.place(x=0,y=0,width=1530,height=45)
    
    img_top=Image.open(r"college_images\AdobeStock_8932892894.jpeg") # IMG URL
    img_top=img_top.resize(720,130),Image.ANTIALIAS)
    self.photoimg_top=ImageTk.PhotoImage(img_top)   
    
    f_lbl=label(self.root,image=self.photoimg_top)
    f_lbl.place(x=0,y=1530,height=720)
    
    #====Frame=====#
    main_frame=Frame(f_lbl,bd=2,bg="white")
    main_frame.place(x=1000,y=0,width=500,height=600)
    
    #=IMG=
    img_top1=Image.open(r"college_images\AdobeStock_8932892894.jpeg") # IMG URL
    img_top1=img_top1.resize(200,200),Image.ANTIALIAS)
    self.photoimg_top1=ImageTk.PhotoImage(img_top1)   
    
    f_lbl=label(main_frame,image=self.photoimg_top1)
    f_lbl.place(x=300,y=0,width=200,height=200)
        
    #==Developer Info==#
    dev_label=Label(current_cource_frame,text="Hello My Name is XYZ",font=("times new roman",20,"bold"),bg="white")
    dev_label.place(x=0,y=5)
    
    img2=image.open(r"college_images\AdobeStock_8932892894.jpeg")
    img2=img2.resize((500,390),Image.ANTIALIAS)
    self.photoimg2=ImageTk.PhotoImage(img2)
    
    f_lbl=Label(main_frame,images=self.photoimg2)
    f_lbl.place(x=0,y=210,width=500,height=390)
    
    # Import class Developer into main file
    from developer import Developer
    
    #Create new method for developer below the method attendance_data(self)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    # Call Developer pafe from main page in developer_face_button below self.photoimg10
    
    b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
    b1.place(x=800,y=380,width=220,height=40)
    
    b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white")
    b1_1.place(x=800,y=500,width=220,height=40)
    
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
    

#=====EXIT Button====#
# Code for exit button create function below open_img(self) function

def iExit(self):
    self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you Sure?",parent=self.root)
    if self.iExit >0:
        self.root.destroy()
    else:
        return 
    
# Call the Function of the Exit Button of the main page
    b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
    b1.place(x=1100,y=380,width=220,height=220)
    
    b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white")
    b1_1.place(x=1100,y=580,width=220,height=40)

# Import package tkinter in main page for exit
import tkinter

# Timer Code
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lb1.after (1000, time)
        lbl = Label(title_lbl, font= ('times new roman', 14, 'bold'), background='white',foreground='blue')
        lbl.place(x=0,y=0, width=110,height=50)
        time()
        
# Import package below import os 
#from time import strftime
#from datetime import datetime

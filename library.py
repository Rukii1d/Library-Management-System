from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")
        
        #..............................Variable..................#
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.nic_var=StringVar()
        self.firstname_var=StringVar()
        self.middlename_var=StringVar()
        self.lastname_var=StringVar()
        self.adress_var=StringVar()
        self.postcode_var=StringVar()
        self.contact_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.datoveredue_var=StringVar()
        self.bookprice_var=StringVar()
        
        
               
              
        


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="teal",fg="black",bd=30,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="teal")
        frame.place(x=0,y=130,width=1570,height=400)
        
    
        #.....................DataFrameleft.......................
    
        DataFrameLeft=LabelFrame(frame,text="Library Membership Details",bg="teal",bd=10,relief=RIDGE,font=("times new roman",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        lblmember=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Member Type:",padx=2,pady=6,background="teal")
        lblmember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",
                               font=("times new roman",13,"bold"),width=27)
        comMember["value"]=("Admin Staf","Lecturer","Student")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_No=Label(DataFrameLeft,bg="teal",text="PRN No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.prn_var ,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lbltitle=Label(DataFrameLeft,bg="teal",text="NIC No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbltitle.grid(row=2,column=0,sticky=W)
        txttitle=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.nic_var,width=29)
        txttitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="teal",text="First Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblMiddle=Label(DataFrameLeft,bg="teal",text="Middle Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMiddle.grid(row=4,column=0,sticky=W)
        txtMiddle=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.middlename_var,width=29)
        txtMiddle.grid(row=4,column=1)

        lblLastName=Label(DataFrameLeft,bg="teal",text="Last Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=5,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=5,column=1)

        lblAddress=Label(DataFrameLeft,bg="teal",text="Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=6,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.adress_var,width=29)
        txtAddress.grid(row=6,column=1)

        lblContact=Label(DataFrameLeft,bg="teal",text="Post Code:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblContact.grid(row=7,column=0,sticky=W)
        txtContact=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.postcode_var,width=29)
        txtContact.grid(row=7,column=1)

        lblBookN=Label(DataFrameLeft,bg="teal",text="Contact No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookN.grid(row=8,column=0,sticky=W)
        txtBookN=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.contact_var,width=29)
        txtBookN.grid(row=8,column=1)

        lblBookTi=Label(DataFrameLeft,bg="teal",text="Book ID:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookTi.grid(row=0,column=2,sticky=W)
        txtBookTi=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookTi.grid(row=0,column=3)

        lblAuth=Label(DataFrameLeft,bg="teal",text="Book Tittle:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAuth.grid(row=1,column=2,sticky=W)
        txtAuth=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtAuth.grid(row=1,column=3)

        lblDateb=Label(DataFrameLeft,bg="teal",text="Auther Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateb.grid(row=2,column=2,sticky=W)
        txtDateb=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.auther_var,width=29)
        txtDateb.grid(row=2,column=3)

        lblDatedu=Label(DataFrameLeft,bg="teal",text="Date Borrowed:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDatedu.grid(row=3,column=2,sticky=W)
        txtDatedu=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDatedu.grid(row=3,column=3)
        
        lblDaysOn=Label(DataFrameLeft,bg="teal",text="Date Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOn.grid(row=4,column=2,sticky=W)
        txtDatysOn=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDatysOn.grid(row=4,column=3)
        
        lblLateReturn=Label(DataFrameLeft,bg="teal",text="Days on Book:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLateReturn.grid(row=5,column=2,sticky=W)
        txtLateReturn=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtLateReturn.grid(row=5,column=3)

        lblLateOver=Label(DataFrameLeft,bg="teal",text="Late Return Fine:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLateOver.grid(row=6,column=2,sticky=W)
        txtLateOver=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateOver.grid(row=6,column=3)

        lblPrice=Label(DataFrameLeft,bg="teal",text="Date Over Due:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPrice.grid(row=7,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.datoveredue_var,width=29)
        txtPrice.grid(row=7,column=3)

        lblBookid=Label(DataFrameLeft,bg="teal",text="Book Price:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookid.grid(row=8,column=2,sticky=W)
        txtBookid=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.bookprice_var,width=29)
        txtBookid.grid(row=8,column=3)
     
        #................DataFrameRight...........


        DataFrameRight=LabelFrame(frame,bd=10,padx=10,relief=RIDGE,text="Book Details",
                                bg="teal",font=("times new roman",14,"bold"))
        DataFrameRight.place(x=870,y=5,width=490,height=350)
        self.textbox=Text(DataFrameRight, font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.textbox.grid(row=0,column=2)
        
        
        #Add.........Books.....................
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        listbooks=['Sherlock Holms','Harry Potter','Lily','How to Learn HTML','Jungle Book','Adventure of TinTin','Cronical of Narnia',
                                                     'Pirates of the Carribean','Halloween Party','Wild Cookbook','AI Technology','NANO Technology','24 Hours',
                                                     'Night at the Museum','Litriture for Psycology','Litriture for Biology','Economics','Parliment Jokes',
                                                     'Mahinda Rajapakshe and theves','Ghost Town Stories','Sanath Nishantha Donkey',
                                                                                         ]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Sherlock Holms"):
                self.bookid_var.set("BKID0001")
                self.booktitle_var.set("Novel")
                self.auther_var.set("Arthur Conan Doyle")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.455")
                
                
            elif(x=="Harry Potter"):
                self.bookid_var.set("BKID0002")
                self.booktitle_var.set("Novel")
                self.auther_var.set("J.K. Rowling")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.550")
                
               
            elif(x=="Lily"):
                self.bookid_var.set("BKID0003")
                self.booktitle_var.set("Novel")
                self.auther_var.set("J.K. Rowling")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.450")
                
            
            elif(x=="How to Learn HTML"):
                self.bookid_var.set("BKID0004")
                self.booktitle_var.set("Education")
                self.auther_var.set("J.O. Foster")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.50")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.650")     
                
            elif(x=="Jungle Book"):
                self.bookid_var.set("BKID0005")
                self.booktitle_var.set("Novel")
                self.auther_var.set("Rudyard Kipling")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.550")    
                
            elif(x=="Adventure of TinTin"):
                self.bookid_var.set("BKID0006")
                self.booktitle_var.set("Novel")
                self.auther_var.set("Herg`e")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.750") 
                
            elif(x=="Cronical of Narnia"):
                self.bookid_var.set("BKID0007")
                self.booktitle_var.set("Novel")
                self.auther_var.set("C.S. Lewis")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.750") 
                
            elif(x=="Pirates of the Carribean"):
                self.bookid_var.set("BKID0008")
                self.booktitle_var.set("Novel")
                self.auther_var.set("Liz Braswell")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.450")
                
                
            elif(x=="Halloween Party"):
                self.bookid_var.set("BKID0009")
                self.booktitle_var.set("Novel")
                self.auther_var.set("sean cruz")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.450")     
            
            
            elif(x=="Wild Cookbook"):
                self.bookid_var.set("BKID0010")
                self.booktitle_var.set("Life Style")
                self.auther_var.set("sean cruz")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.450")    
            
            elif(x=="AI Technology"):
                self.bookid_var.set("BKID0011")
                self.booktitle_var.set("Education")
                self.auther_var.set("Sean Paul")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.750")    
            
            elif(x=="NANO Technology"):
                self.bookid_var.set("BKID0012")
                self.booktitle_var.set("Education")
                self.auther_var.set("Sean Paul")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.850")     
        
            elif(x=="24 Hours"):
                self.bookid_var.set("BKID0014")
                self.booktitle_var.set("Education")
                self.auther_var.set("Paul Jackson")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("LKR.25")
                self.datoveredue_var.set("No")
                self.bookprice_var.set("LKR.450") 
        
        
        listBox=Listbox(DataFrameRight,font=("arial",11,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listbooks:
            listBox.insert(END,item)


        #.................BUTTONS frame................
        Framebutton=Frame(self.root,bd=5,relief=RIDGE,padx=0,bg="teal")
        Framebutton.place(x=0,y=500,width=1370,height=60)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times new roman",11,"bold"),width=25,background="black",foreground="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("times new roman",11,"bold"),width=25,background="blue",foreground="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("times new roman",11,"bold"),width=25,background="black",foreground="white")
        btnAddData.grid(row=0,column=2) 
        
        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("times new roman",11,"bold"),width=25,background="blue",foreground="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("times new roman",11,"bold"),width=25,background="black",foreground="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("times new roman",11,"bold"),width=20,background="Blue",foreground="white")
        btnAddData.grid(row=0,column=5)



        #.................information frame................
        FrameDetails=Frame(self.root,bd=10,relief=RIDGE,padx=15,bg="teal")
        FrameDetails.place(x=0,y=530,width=1370,height=180)

        Table_frame=Frame(FrameDetails,bd=10,relief=RIDGE,bg="teal")
        Table_frame.place(x=0,y=2,width=1320,height=150)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","nicno","firstname","middlename","lastname",
                                     "adress","postcode","contactno","bookid","booktitle","auther","dateborrowed",
                                     "datedue","days","latereturnfine","dateoverdue","bookprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)




        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("nicno",text="NIC No")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("middlename",text="Middle Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress",text="Adress")
        self.library_table.heading("postcode",text="Post Code")
        self.library_table.heading("contactno",text="Contact No")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("bookprice",text="Final Price")
        

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        
        self.library_table.column("membertype",width="100")
        self.library_table.column("prnno",width="100")
        self.library_table.column("nicno",width="100")
        self.library_table.column("firstname",width="100")
        self.library_table.column("middlename",width="100")
        self.library_table.column("lastname",width="100")
        self.library_table.column("adress",width="100")
        self.library_table.column("postcode",width="100")
        self.library_table.column("contactno",width="100")
        self.library_table.column("bookid",width="100")
        self.library_table.column("booktitle",width="100")
        self.library_table.column("auther",width="100")
        self.library_table.column("dateborrowed",width="100")
        self.library_table.column("datedue",width="100")
        self.library_table.column("days",width="100")
        self.library_table.column("latereturnfine",width="100")
        self.library_table.column("dateoverdue",width="100")
        self.library_table.column("bookprice",width="100")
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
        

    def add_data(self):
        cnx=mysql.connector.connect(host="localhost",username="root",password="",database="sys")
        my_cursor=cnx.cursor()
        
        my_cursor.execute("insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                 self.member_var.get(),
                                                                                                                 self.prn_var.get(),
                                                                                                                 self.nic_var.get(),
                                                                                                                 self.firstname_var.get(),
                                                                                                                 self.middlename_var.get(),
                                                                                                                 self.lastname_var.get(),
                                                                                                                 self.adress_var.get(),
                                                                                                                 self.postcode_var.get(),
                                                                                                                 self.contact_var.get(),
                                                                                                                 self.bookid_var.get(),
                                                                                                                 self.booktitle_var.get(),
                                                                                                                 self.auther_var.get(),
                                                                                                                 self.dateborrowed_var.get(),
                                                                                                                 self.datedue_var.get(),
                                                                                                                 self.daysonbook_var.get(),
                                                                                                                 self.latereturnfine_var.get(),
                                                                                                                 self.datoveredue_var.get(),
                                                                                                                 self.bookprice_var.get(),      
                                                                                                              ))                                                                      
        cnx.commit()
        self.fatch_data()
        cnx.close()
        
        messagebox.showinfo("Success","Member Has been inserted successfully")
        
    #Update Button    
    def update(self):
        cnx=mysql.connector.connect(host="localhost",username="root",password="",database="sys")
        my_cursor=cnx.cursor()
        
        my_cursor.execute("update library set Member=%s,NIC_NO=%s,FirstName=%s,MiddleName=%s,LastName=%s,Address=%s,Postcode=%s,Contact_No=%s,Bookid=%s,Booktitle=%s,Auther=%s,Dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,Dateoverdue=%s,Bookprice=%s,PRN_NO=%s"(
                                                                                                                 self.member_var.get(),
                                                                                                                 self.nic_var.get(),
                                                                                                                 self.firstname_var.get(),
                                                                                                                 self.middlename_var.get(),
                                                                                                                 self.lastname_var.get(),
                                                                                                                 self.adress_var.get(),
                                                                                                                 self.postcode_var.get(),
                                                                                                                 self.contact_var.get(),
                                                                                                                 self.bookid_var.get(),
                                                                                                                 self.booktitle_var.get(),
                                                                                                                 self.auther_var.get(),
                                                                                                                 self.dateborrowed_var.get(),
                                                                                                                 self.datedue_var.get(),
                                                                                                                 self.daysonbook_var.get(),
                                                                                                                 self.latereturnfine_var.get(),
                                                                                                                 self.datoveredue_var.get(),
                                                                                                                 self.bookprice_var.get(), 
                                                                                                                 self.prn_var.get(),
           
                                                                                                 ))
        cnx.commit()
        self.fatch_data()
        self.reset()
        cnx.close()  
           
        messagebox.showinfo("Success","Member has been Updated")    
           
           
        
    def fatch_data(self): 
        cnx=mysql.connector.connect(host="localhost",username="root",password="",database="sys")
        my_cursor=cnx.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
         
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            cnx.commit()
        cnx.close()
        
        
     #..........show Data Button............    
     
     
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.nic_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.middlename_var.set(row[4]),
        self.lastname_var.set(row[5]),
        self.adress_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.contact_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.get(row[15]),
        self.datoveredue_var.get(row[16]),
        self.bookprice_var.get(row[17])
  
    def showData(self):   
        self.textbox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")    
        self.textbox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n") 
        self.textbox.insert(END,"NIC No:\t\t"+ self.nic_var.get() + "\n") 
        self.textbox.insert(END,"First Name:\t\t"+ self.firstname_var.get() + "\n") 
        self.textbox.insert(END,"Middle Name:\t\t"+ self.middlename_var.get() + "\n") 
        self.textbox.insert(END,"Last Name:\t\t"+ self.lastname_var.get() + "\n") 
        self.textbox.insert(END,"Address:\t\t"+ self.adress_var.get() + "\n") 
        self.textbox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n") 
        self.textbox.insert(END,"Contact No:\t\t"+ self.contact_var.get() + "\n") 
        self.textbox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n") 
        self.textbox.insert(END,"Book Tittle:\t\t"+ self.booktitle_var.get() + "\n") 
        self.textbox.insert(END,"Auther Name:\t\t"+ self.auther_var.get() + "\n") 
        self.textbox.insert(END,"Date Borrowed:\t\t"+ self.dateborrowed_var.get() + "\n") 
        self.textbox.insert(END,"Date Due:\t\t"+ self.datedue_var.get() + "\n") 
        self.textbox.insert(END,"Days on Book:\t\t"+ self.daysonbook_var.get() + "\n") 
        self.textbox.insert(END,"Late Return Fine:\t\t"+ self.latereturnfine_var.get() + "\n") 
        self.textbox.insert(END,"Date Over Due:\t\t"+ self.datoveredue_var.get() + "\n")      
        self.textbox.insert(END,"Book Price:\t\t"+ self.bookprice_var.get() + "\n") 
     
     
      #Reset Button
      
         
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.nic_var.set(""),
        self.firstname_var.set(""),
        self.middlename_var.set(""),
        self.lastname_var.set(""),
        self.adress_var.set(""),
        self.postcode_var.set(""),
        self.contact_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.datoveredue_var.set(""),
        self.bookprice_var.set("")
        self.textbox.delete("1.0",END)
        
    #Exit Button
    
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
             self.root.destroy()
             return
         
    
    
    #Delete Button     
    def delete(self):
        if self.prn_var.get()==""or self.nic_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            cnx=mysql.connector.connect(host="localhost",username="root",password="",database="sys")
            my_cursor=cnx.cursor() 
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            
            cnx.commit()
            self.fatch_data()
            self.reset()
            cnx.close()
            
            messagebox.showinfo("Success","Member has been Deleted!!")
            
         
         
         

if __name__=="__main__":
    root=Tk()
    object=LibraryManagementSystem(root)
    root.mainloop()
    
    
    

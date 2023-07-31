
#------------------------------------------------------------------------------------------------------------------------------------------------

#IMPORTING LIBRARIES.

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from cs50 import SQL
import tkinter.messagebox as tmsg
#------------------------------------------------------------------------------------------------------------------------------------------------

# USING SQL
db = SQL("sqlite:///school.db")
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR EDITING FEES IN DATABASE

def editfeeDB():
    try:
     if entered_fee.get().lower() in ['pending','paid']:
        db.execute("update students set fee_status=? where name=?;",entered_fee.get().lower(),namePost.get())
        tmsg.showinfo("UPDATE FEE","Sucesfully updated!")
     else:
        tmsg.showinfo("UPDATE FEE","Invalid Fee!\nFee can be either \'pending\' or \'paid\'")
    except:
        tmsg.showinfo("UPDATE FEE","Invalid Fee!")


#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR FEE EDITING (EVENT)

def editfee(event):
    # Get the index of the selected item
    index = event.widget.curselection()[0]
    # Get the value of the selected item
    value = event.widget.get(index)
    name=value.split()[0];percentage=value.split()[-1]
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    global entered_fee,namePost
    entered_fee=StringVar();namePost=StringVar()
    namePost.set(name[:-1])
    entered_fee.set(percentage)
    Label(text=f"ENTER fee of {name}", font=" Calibiri 20", bg="#90AEB2").place(x=800, y=200)
    Entry(root,textvariable=entered_fee, width=20, font=20).place(x=800, y=250)
    Entry(root,textvariable=namePost, width=20, font=20).place(x=550, y=250)
    Button(text="EDIT", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=editfeeDB).place(x=760, y=300)    
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR FEES FOR ALL

def goforfeeAll():
    for i in range(1, feedata.size()):
        feedata.delete(1)
    for student in db.execute("SELECT * FROM students;"):
        feedata.insert(END, f"{student['name']}:          {student['cms_id']}                {student['fee_status']}")
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR FEES OF INDIVISUAL

def goforfeeIndivisual():
    for _ in range(1, feedata.size()):
        feedata.delete(1)
    allstudents=[i['name'] for i in db.execute("SELECT * FROM students;")]
    for student in db.execute("SELECT * FROM students;"):
     if student['name']==indivisual.get().strip():   
        feedata.insert(END, f"{student['name']}:          {student['cms_id']}                {student['fee_status']}")
    if  indivisual.get().strip() not in allstudents:
        tmsg.showinfo("FEE SECTION", "NAME not exists")
#------------------------------------------------------------------------------------------------------------------------------------------------

#DEFINING A FUNCTION OF FEE SECTION

def FeeSection():
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    global indivisual
    global feedata,all
    indivisual=StringVar();all=StringVar()
    Label(text="ENTER STUDENT NAME: ", font=" Calibiri 20", bg="#90AEB2").place(x=750, y=200)
    Entry(root, textvariable=indivisual, width=20, font=20).place(x=800, y=250)
    Button(text="SEARCH", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=goforfeeIndivisual).place(x=700, y=300)
    all=Button(text="ALL STUDENTS", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=goforfeeAll).place(x=950, y=300)

    # CREATING A LISTBOX
    feedata = Listbox(rectangle2, height=15, width=70, font="calibri 15")
    feedata.insert(END, '''NAME            CMS ID               FEE STATUS\n''')
    feedata.place(x=600, y=400)
    feedata.bind("<<ListboxSelect>>", editfee)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------

# CREATING A FUNCTION FOR EDITING STUDENTS FEE IN DATABASE

def editpercentageDB():
    try:
     if 0.0<=float(entered_percentage.get())<=100.0:
        db.execute("update students set percentage=? where name=?;",entered_percentage.get(),namePost.get())
        tmsg.showinfo("UPDATE PERCENTAGE","Sucesfully updated!")
     else:
        tmsg.showinfo("UPDATE PERCENTAGE","Invalid percentage!")
    except:
        tmsg.showinfo("UPDATE PERCENTAGE","Invalid percentage!")
#------------------------------------------------------------------------------------------------------------------------------------------------

# CREATING A FUNCTION TO EDIT PERCENTAGE 

def editpercentagepage(event):
    # Get the index of the selected item
    item = event.widget.selection()[0]
    name = marksdata.item(item, "values")[0]
    percentage = marksdata.item(item, "values")[2]
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    global entered_percentage,namePost
    entered_percentage=StringVar();namePost=StringVar()
    namePost.set(name)
    entered_percentage.set(percentage)
    Label(text=f"ENTER Percentage of {name}", font=" Calibiri 20", bg="#90AEB2").place(x=800, y=200)
    Entry(root,textvariable=entered_percentage, width=20, font=20).place(x=800, y=250)
    Entry(root,textvariable=namePost, width=20, font=20).place(x=550, y=250)
    Button(text="EDIT", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=editpercentageDB).place(x=760, y=300)    
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR GETTING MARKS OF STUDENTS 

def goformarksAll():
    marksdata.delete(*marksdata.get_children())
    cursor.execute(f'SELECT name,cms_id,percentage FROM students')
    rows = cursor.fetchall()
    for column in columns:
        marksdata.heading(column, text=column)
    for row in rows:
        marksdata.insert('', tk.END, values=row)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR GETTING MARKS OF A SINGLE STUDENT

def goformarksIndivisual():
    if indivisual.get() not in [i["name"] for i in db.execute("select name from students;")]:
        tmsg.showinfo("ERROR","Name not found!")
        return marks()
    marksdata.delete(*marksdata.get_children())
    cursor.execute(f'SELECT name,cms_id,percentage FROM students where name=\'{indivisual.get().strip()}\'')
    rows = cursor.fetchall()
    for column in columns:
        marksdata.heading(column, text=column)
    for row in rows:
        marksdata.insert('', tk.END, values=row)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR MARKS

def marks():
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    global indivisual
    global marksdata,columns
    indivisual=StringVar()
    Label(text="ENTER STUDENT NAME: ", font=" Calibiri 20", bg="#90AEB2").place(x=750, y=200)
    Entry(root, textvariable=indivisual, width=20, font=20).place(x=800, y=250)
    Button(text="SEARCH", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=goformarksIndivisual).place(x=700, y=300)
    Button(text="ALL STUDENTS", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=goformarksAll).place(x=950, y=300)
    columns=['name',"cms id","percentage"]
    marksdata = ttk.Treeview(root, columns=columns, show='headings')
    marksdata.place(x=600, y=400,width=700,height=400)
    marksdata.bind("<<TreeviewSelect>>", editpercentagepage)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR EDITTING ATTENDENCE OF STUDENTS

def editattandance(event):
    if datee.get()!=datetime.now().strftime("%d/%m/%y"):
        tmsg.showinfo("Attandence","Cant modify Past Attandences!!")
        return particularDate()
    
    item = event.widget.selection()[0]
    if Adata.item(item, "values")[2]=='present':
        db.execute("update Attandence set status='absent' where name=? and date=?;",
                   Adata.item(item, "values")[0],datetime.now().strftime("%d/%m/%y"))
    else:
        db.execute("update Attandence set status='present' where name=? and date=?;",
                   Adata.item(item, "values")[0],datetime.now().strftime("%d/%m/%y"))
    return AttandenceStart()
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR STUDENT ATTENDENCES

def AllAttandence():
    Adata.delete(*Adata.get_children())
    cursor.execute(f'SELECT name,cms_id,status FROM Attandence where date=\'{datetime.now().strftime("%d/%m/%y")}\';')
    rows = cursor.fetchall()
    for column in columns:
        Adata.heading(column, text=column)
    for row in rows:
        Adata.insert('', tk.END, values=row) 
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR INDIVIDUAL STUDENT ATTENDENCE

def IndivisualAttandence():
    if one.get() not in [i["name"] for i in db.execute("select name from students;")]:
            tmsg.showinfo("ERROR","Name not found!")
            return marks()
    Adata.delete(*Adata.get_children())
    cursor.execute(f'SELECT name,cms_id,status FROM Attandence where name=\'{one.get().strip()}\' and date=\'{datetime.now().strftime("%d/%m/%y")}\'')
    rows = cursor.fetchall()
    for column in columns:
        Adata.heading(column, text=column)
    for row in rows:
        Adata.insert('', tk.END, values=row)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR ATTENDENCE OF A DATE

def particularDate():
    if datee.get() not in [i["date"] for i in db.execute("select date from Attandence;")]:
        tmsg.showinfo("ATTANDENCE","Date not Found!!")
        return AttandenceStart()
    Adata.delete(*Adata.get_children())
    cursor.execute(f'SELECT name,cms_id,status FROM Attandence where date=\'{datee.get()}\';')
    rows = cursor.fetchall()
    for column in columns:
        Adata.heading(column, text=column)
    for row in rows:
        Adata.insert('', tk.END, values=row) 
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR SAVING ATTENDENCE 

def saveattandence():
    tmsg.showinfo("ATTANDENCE","Saved Todays SUCESSFULLY!")
#------------------------------------------------------------------------------------------------------------------------------------------------
    
# DEFINING A FUNCTION FOR STARTING ATTENDENCE

def AttandenceStart():
    if datetime.now().strftime("%d/%m/%y") not in [i["date"] for i in db.execute("select date from Attandence;")]:
        for i in db.execute("select name,cms_id from students;"): 
            db.execute("insert into Attandence(name,cms_id,status,date) values(?,?,'present',?);",i['name'],i['cms_id'],datetime.now().strftime("%d/%m/%y") )    
    for k in [i for i in db.execute("select name,cms_id from students") if i['name'] not in ([j['name'] for j in db.execute("select name from Attandence where date=?",datetime.now().strftime("%d/%m/%y"))])]:
        db.execute("insert into Attandence(name,cms_id,status,date) values(?,?,'present',?);", k['name'], k['cms_id'],datetime.now().strftime("%d/%m/%y"))
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    global Adata,columns,one,datee
    one=StringVar();datee=StringVar()
    datee.set(datetime.now().strftime("%d/%m/%y"))
    Label(text=f"TODAY'S DATE: {datee.get()}", font=" Calibiri 20", bg="#90AEB2").place(x=370, y=200)
    Entry(root,textvariable=datee, width=20, font=20).place(x=400, y=250)
    Button(text="SEARCH DATE", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=particularDate).place(x=400, y=300)
    Label(text="ENTER STUDENT NAME: ", font=" Calibiri 20", bg="#90AEB2").place(x=750, y=200)
    Entry(root, textvariable=one, width=20, font=20).place(x=800, y=250)
    Button(text="SEARCH", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=IndivisualAttandence).place(x=700, y=300)
    Button(text="ALL STUDENTS", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=AllAttandence).place(x=950, y=300)
    Button(text="SAVE", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=saveattandence).place(x=820, y=350)
    columns=['name',"cms id","attandence"]
    Adata = ttk.Treeview(root, columns=columns, show='headings')
    Adata.place(x=600, y=400,width=700,height=400)
    cursor.execute(f'SELECT name,cms_id,status FROM Attandence where date=\'{datetime.now().strftime("%d/%m/%y")}\';')
    rows = cursor.fetchall()
    for column in columns:
        Adata.heading(column, text=column)
    for row in rows:
        Adata.insert('', tk.END, values=row)
        
    Adata.bind("<<TreeviewSelect>>", editattandance)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR ALL STUDENT ATTENDENCES

def goforstudentAll():
    Tree.delete(*Tree.get_children())
   # cursor.execute(f'SELECT name,cms_id,father_name,pwd FROM students')
    rows = cursor.fetchall()
    for column in columns:
        Tree.heading(column, text=column)
    for row in rows:
        Tree.insert('', tk.END, values=row)
#------------------------------------------------------------------------------------------------------------------------------------------------

# CREATING A FUNCTION FOR INDIVISUAL STUDENT ATTENDENCE

def goforstudentIndivisual():
    if namesearch.get() not in [i["name"] for i in db.execute("select name from students;")]:
        tmsg.showinfo("ERROR","Name not found!")
        return marks()
    
    Tree.delete(*Tree.get_children())
    cursor.execute(f'SELECT name,cms_id,father_name,pwd FROM students where name=\'{namesearch.get().strip()}\'')
    rows = cursor.fetchall()
    for column in columns:
        Tree.heading(column, text=column)
    for row in rows:
        Tree.insert('', tk.END, values=row)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR SEARCHING A STUDENT

def searchstudent():
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    global namesearch,Tree,columns
    namesearch= StringVar()
    Label(text="ENTER STUDENT NAME: ", font=" Calibiri 20", bg="#90AEB2").place(x=500, y=200)
    Entry(root, textvariable=namesearch, width=20, font=20).place(x=850, y=200)
    Button(text="SEARCH", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=goforstudentIndivisual).place(x=1100, y=196)
    Button(text="ALL STUDENTS", font=" Calibiri 17", height=1, width=29, bg="#90AEB2",command=goforstudentAll).place(x=780, y=250)
    columns = ["NAME",'CMS ID',"FATHER NAME",'PASSWORD']
    Tree = ttk.Treeview(root, columns=columns, show='headings')
    Tree.place(x=600, y=350,width=600,height=400)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR STUDENT DATA

def studentdata():
        if str(cnicnumber.get().strip()).isnumeric() and len(str(cnicnumber.get())) == 13:
            name=studentname.get();father=fathername.get();cnic=cnicnumber.get();cms=cmsno.get();pwd=password.get()
            db.execute("INSERT INTO students(cms_id,pwd,name,father_name,cnic) VALUES(?,?,?,?,?);",cms,pwd,name,father,cnic)
            tmsg.showinfo("DATA", "Data Entered successfully!")
            studentname.set('')
            fathername.set('')
            cnicnumber.set('')
            cmsno.set('')
            password.set('')
            contact.set('')
        else:
            tmsg.showinfo("Error", "Invalid Entries!")
        return
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR ADDING A STUDENT

def addstudent():
    root.title("ADMIN BLOCK-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    global studentname
    global fathername
    global cnicnumber
    global cmsno
    global password
    global contact
        #GET THESE FOLLOWING INFO

    studentname = StringVar()
    fathername = StringVar()
    cnicnumber = StringVar()
    contact = StringVar()
    cmsno = StringVar()
    password = StringVar()
    Label(text="ENTER STUDENT NAME", font=" Calibiri 20", bg="#90AEB2").place(x=224, y=200)
    Entry(root, textvariable=studentname, width=30, font=20).place(x=610, y=202)
    Label(text="ENTER FATHER NAME", font=" Calibiri 20", bg="#90AEB2").place(x=224, y=270)
    Entry(root, textvariable=fathername, width=30, font=20).place(x=610, y=282)
    Label(text="ENTER CNIC NUMBER", font=" Calibiri 20", bg="#90AEB2").place(x=224, y=340)
    Entry(root, textvariable=cnicnumber, width=30, font=20).place(x=610, y=352)
    Label(text="CONTACT NUMBER", font=" Calibiri 20", bg="#90AEB2").place(x=224, y=430)
    Entry(root, textvariable=contact, width=30, font=20).place(x=610, y=432)
    Label(text="CMS ID", font=" Calibiri 20", bg="#90AEB2").place(x=224, y=500)
    Entry(root, textvariable=cmsno, width=30, font=20).place(x=610, y=502)
    Label(text="PASSWORD", font=" Calibiri 20", bg="#90AEB2").place(x=224, y=570)
    Entry(root, textvariable=password, width=30, font=20).place(x=610, y=582)
    Button(text="ADD STUDENT", font=" Calibiri 17", height=2, width=20, bg="#90AEB2",command=studentdata).place(x=960,y=630)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR SENDING MESSAGE

def sendMsg():
    if msg.get()=='':
        return addAnouncements()
    try:
        db.execute("insert into Announcments(time,msg) values(?,?);",datetime.now(),msg.get())
        tmsg.showinfo("CHATS","Sucesfully sent!")
        addAnouncements()
    except:
        tmsg.showerror("Unable to sent right now!")
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR ADDING ANY ANNOUNCEMENTS

def addAnouncements():
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="ENTER MESSAGE: ", font=" Calibiri 20", bg="#90AEB2").place(x=750, y=200)
    global msg
    msg=StringVar()
    entry=Entry(root, textvariable=msg, width=50, font=20)
    entry.place(x=600, y=250)
    Button(text="SEND", font=" Calibiri 17", height=1, width=20, bg="#90AEB2",command=sendMsg).place(x=760, y=300)
    
    cursor.execute(f'SELECT sender,time,msg FROM Announcments')
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    treeview = ttk.Treeview(root, columns=columns, show='headings')
    treeview.place(x=600, y=400,width=600,height=400)
    for column in columns:
        treeview.heading(column, text=column)
    for row in rows:
        treeview.insert('', tk.END, values=row)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=adminblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# STARTING ADMIN BLOCK
# DEFINING A FUNCTION OF ADMIN BLOCK

def adminblock():                                                          
    root.title("ADMIN BLOCK-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Button(text="SEARCH A STUDENT", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=searchstudent).place(x=600,y=300)
    Button(text="ADD STUDENT ACCOUNT", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=addstudent).place(x=600,y=350)
    Button(text="ATTENDENCE OF STUDENTS", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=AttandenceStart).place(x=600,y=400)
    Button(text="MARKS OF STUDENTS", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=marks).place(x=600, y=450)
    Button(text="ADD ANNOUNCEMENTS AND EVENTS", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=addAnouncements).place(x=600, y=500)
    Button(text="FEE SLIPS OF STUDENTS", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=FeeSection).place(x=600,y=550)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=admin).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR VIEWING STUDENT RESULTS

def viewStudentResult():
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="YOUR PERCENTAGE ", font=" Calibiri 20", bg="#90AEB2").place(rectangle2,x=750, y=200)
    Button(text="RELOAD", font=" Calibiri 17", height=1, width=20, bg="#90AEB2").place(x=760, y=300)
    cursor.execute(f'SELECT name,cms_id,percentage FROM students where cms_id={int(cmsID.get())}')
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    treeview = ttk.Treeview(root, columns=columns, show='headings')
    treeview.place(x=600, y=400,width=600,height=400)
    for column in columns:
        treeview.heading(column, text=column)
    for row in rows:
        treeview.insert('', tk.END, values=row)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=studentblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR STUDENT'S OWN ATTENDENCE

def myAttandence():
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="YOUR ATTENDANCE ", font=" Calibiri 20", bg="#90AEB2").place(x=750, y=200)
    Button(text="RELOAD", font=" Calibiri 17", height=1, width=20, bg="#90AEB2").place(x=760, y=300)
    searchlist = Listbox(rectangle2, height=15, width=70, font="calibri 15")
    searchlist.insert(END, '''DATE                     NAME                 CMS ID\n''')
    name=db.execute("select name from students where cms_id=?",int(cmsID.get()))[0]['name']
    attendences=db.execute("SELECT date from Attandence where name=?",name)
    for attandence in attendences:
        searchlist.insert(END, f'''{attandence['date']}                 {name}                     {int(cmsID.get())}\n''')
    searchlist.place(x=600, y=400)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=studentblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR STUDENT'S OWN FEE STATUS

def myFeeStatus():
    student=db.execute("SELECT * from students where cms_id=?",int(cmsID.get()))[0]    
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="YOUR FEE STATUS", font=" Calibiri 20", bg="#90AEB2").place(x=750, y=200)
    Button(text="RELOAD", font=" Calibiri 17", height=1, width=20, bg="#90AEB2").place(x=760, y=300)
    searchlist = Listbox(rectangle2, height=15, width=70, font="calibri 15")
    searchlist.insert(END, '''NAME                 CMS ID                     FEE STATUS\n''')
    searchlist.insert(END, f'''{student["name"]}                 {student["cms_id"]}                     {student["fee_status"]}\n''')
    searchlist.place(x=600, y=400)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=studentblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR STUDENT'S ANNOUNCMENTS

def myAnnouncments():
    root.title("SEARCH STUDENT-------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="ANOUNCEMENTS", font=" Calibiri 20", bg="#90AEB2").place(rectangle2,x=750, y=200)
    Button(text="RELOAD", font=" Calibiri 17", height=1, width=20, bg="#90AEB2").place(x=760, y=300)
    cursor.execute(f'SELECT sender,time,msg FROM Announcments')
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    treeview = ttk.Treeview(root, columns=columns, show='headings')
    treeview.column('#1', stretch=tk.NO, width=50)
    treeview.place(x=600, y=400,width=600,height=400)
    for column in columns:
        treeview.heading(column, text=column)
    for row in rows:
        treeview.insert('', tk.END, values=row)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=studentblock).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING THE STUDENT BLOCK

def studentblock():                                                
    root.title("STUDENT BLOCK------------------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM",font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Button(text="SEE MY RESULTS", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=viewStudentResult).place(x=600, y=300)
    Button(text="SEE THE ATTENDENCE", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=myAttandence).place(x=600, y=350)
    Button(text="ANNOUNCMENTS", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=myAnnouncments).place(x=600,  y=400)
    Button(text="FEE SLIPS", font=" Calibiri 17", height=1, width=40, bg="#90AEB2",command=myFeeStatus).place( x=600, y=450)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=admin).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR CHECKING STUDENT PASSWORD

def studentpasswordcheck():                                  
    # try:
        if int(cmsvalue.get()) in [i["cms_id"] for i in db.execute("select cms_id from students")]:
            if password_student.get()==db.execute("select pwd from students where cms_id=?",int(cmsvalue.get()))[0]["pwd"]:
                global cmsID;cmsID=IntVar();cmsID.set(int(cmsvalue.get()))
                studentblock()
            else:
                tmsg.showinfo("PASSWORD ERROR","Wrong password!")
        else:
            tmsg.showinfo("ERROR","NO RECORD FOUND")
    # except:
    #         tmsg.showinfo("ERROR","Invalid entries!")
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING A FUNCTION FOR CHECKING ADMIN PASSWORD

def passwordadmincheck():
    if password_admin.get()=='admin':
        adminblock()
    else:
         tmsg.showinfo("WRONG PASSWORD","PASSWORD DIDN'T MATCH")
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR ADMIN

def admin():                                                        
    root.title("ADMIN LOG IN------------------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    global password_admin
    password_admin = StringVar()
    Label(text="ENTER PASSWORD", font=" Calibiri 20",bg="#90AEB2").place(x=750,y=300)  # taking password input from admin
    Entry(root,show="*", textvariable=password_admin, width=20, font=20).place(x=760, y=400)
    Button(text="LOG IN", font=" Calibiri 17", height=1, width=20,bg="#90AEB2",command=passwordadmincheck).place(x=760, y=500,)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=main).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------

# DEFINING A FUNCTION FOR STUDENT LOGIN

def student():                                                  
    root.title("STUDENT LOG IN------------------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    global cmsvalue
    global password_student
    cmsvalue=StringVar()
    password_student=StringVar()
    Label(text="ENTER CMS ID",font=" Calibiri 20",bg="#90AEB2").place(x=750,y=300)     #taking cms and password input from student
    Entry(root,textvariable=cmsvalue,width=20,font=20).place(x=740,y=350)
    Label(text="ENTER PASSWORD", font=" Calibiri 20",bg="#90AEB2").place(x=730, y=500)
    Entry(root,show="*",textvariable=password_student,width=20,font=20).place(x=750,y=550)
    Button(text="LOG IN",font=" Calibiri 17",height=1,width=20,bg="#90AEB2",command=studentpasswordcheck).place(x=730,y=650)
    Button(text="BACK", font=" Calibiri 17", height=1, width=6, bg="#90AEB2", command=main).place(x=0, y=0)
#------------------------------------------------------------------------------------------------------------------------------------------------


# DEFINING THE MAIN FUNCTION

def main():                                    
    root.title("ADMIN OR STUDENT?------------------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    Canvas(root,height=1000,width=220,bg="#017075").place(x=0,y=0)
    rectangle2 = Canvas(root,height=700,width=2000,bg="#90AEB2").place(x=222,y=170)
    #Label(text="SCHOOL MANAGEMENT SYSTEM",font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600,y=100)
    # photo = PhotoImage(file="d.gif")
    # Label(image=photo).place(x=222,y=-58)
    Button(rectangle2,text="LOGIN AS ADMIN",font=" Calibiri 17",height=3,width=20,command=admin,bg="#90AEB2").place(x=750,y=360)
    Button(rectangle2,text="LOGIN AS STUDENT",font=" Calibiri 17",height=3,width=20,command=student,bg="#90AEB2").place(x=750,y=500)
#------------------------------------------------------------------------------------------------------------------------------------------------


#  EXECUTING THE PROGRAM
def start():
    global root
    root = Tk()
    root.geometry("744x444")
    root.title("ADMIN OR STUDENT?------------------------------DEVELOPED BY SARMAD,FAKHIR AND ABDUL MOIZ")
    #photo = PhotoImage(file="fakhirKayLiayPNG.png")
    #Label(image=photo).place(x=0, y=0)
    Canvas(root, height=1000, width=220, bg="#017075").place(x=0, y=0)
    rectangle2 = Canvas(root, height=700, width=2000, bg="#90AEB2").place(x=222, y=170)
    Label(text="SCHOOL MANAGEMENT SYSTEM", font=" Calibiri 30 bold", bg="#EDF6F9").place(x=600, y=100)
    photo = PhotoImage(file="images.png")
    Label(image=photo).place(x=222, y=-58)
    Button(rectangle2, text="LOGIN AS ADMIN", font=" Calibiri 17", height=3, width=20, command=admin, bg="#90AEB2").place(x=750, y=360)
    Button(rectangle2, text="LOGIN AS STUDENT", font=" Calibiri 17", height=3, width=20, command=student,bg="#90AEB2").place(x=750, y=500)
    #main()
    root.mainloop()
start()
conn.commit()
conn.close()


#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------



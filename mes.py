from tkinter import *

avi = Tk()
avi.geometry('1000x1000')
avi.title('vignan registartion')
avi.configure(background='white')
imag=PhotoImage(file="tt.png")
label11=Label(avi,image=imag)
label11.pack()


label_1 = Label(avi, text="FullName : ",width=15,font=("bold", 10),fg='white',bg='green')
label_1.place(x=300,y=130)

entry_1 = Entry(avi)
entry_1.place(x=500,y=130)
entry_1.config(bg='grey',fg='white',font=('bold',10))

label = Label(avi,text="Father name : ",width=15,font=("bold",10),fg='white',bg='green')
label.place(x=300,y=180)

entry = Entry(avi)
entry.place(x=500,y=180)
entry.configure(bg='grey',fg='white',font=('bold',10))


label_2 = Label(avi, text="Email : ",width=15,font=("bold", 10),fg='white',bg='green')
label_2.place(x=300,y=230)

entry_2 = Entry(avi)
entry_2.place(x=500,y=230)
entry_2.config(bg='grey',fg='white',font=('bold',10))

label_3 = Label(avi, text="Gender : ",width=12,font=("bold", 10),fg='white',bg='green')
label_3.place(x=200,y=280)
var = StringVar()

Radiobutton(avi, text="Male",padx = 0, variable=var, value='male',bg='skyblue').place(x=330,y=280)
Radiobutton(avi, text="Female",padx = 20, variable=var, value='female',bg='skyblue').place(x=380,y=280)

labelb = Label(avi,text="DOB : ",width=10,font=('bold',10),fg='white',bg='green')
labelb.place(x=530,y=280)

listd = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
d=StringVar()
droplist=OptionMenu(avi,d, *listd)
droplist.config(width=2,fg='black',bg='skyblue')
d.set('DD')
droplist.place(x=630,y=280)

listm = ['JAN','FEB','MAR','APRIL','MAY','JUNE','JULY','AUG','SEP','OCT','NOV','DEC'];
e=StringVar()
droplist=OptionMenu(avi,e, *listm)
droplist.config(width=2,fg='black',bg='skyblue')
e.set('MM')
droplist.place(x=700,y=280)

listy = ['1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006'];
f=StringVar()
droplist=OptionMenu(avi,f, *listy)
droplist.config(width=4,fg='black',bg='skyblue')
f.set('YYYY')
droplist.place(x=770,y=280)


labela=Label(avi,text="Roll : ",width=10,font=("bold",10),fg='white',bg='green')
labela.place(x=150,y=330)

entrya = Entry(avi)
entrya.place(x=250,y=330)
entrya.config(bg='grey',fg='white',font=('bold',10))

labelar=Label(avi,text="Aadhar : ",width=10,font=("bold",10),fg='white',bg='green')
labelar.place(x=400,y=330)

entryar = Entry(avi)
entryar.place(x=500,y=330)
entryar.config(bg='grey',fg='white',font=('bold',10))

labelp=Label(avi,text="Mobile : ",width=10,font=("bold",10),fg='white',bg='green')
labelp.place(x=650,y=330)

entryp = Entry(avi)
entryp.place(x=750,y=330)
entryp.config(bg='grey',fg='white',font=('bold',10))

label_4 = Label(avi, text="Course : ",width=8,font=("bold", 10),fg='white',bg='green')
label_4.place(x=90,y=380)

list1 = ['B.tech','M.tech','Mca','Bca','Pharmacy','Bba'];
c=StringVar()
droplist=OptionMenu(avi,c, *list1)
droplist.config(width=15,fg='black',bg='skyblue')
c.set('select your course')
droplist.place(x=180,y=380)

label_5 = Label(avi, text="Department : ",width=10,font=("bold", 10),fg='white',bg='green')
label_5.place(x=340,y=380)

list2 = ['IT','CSE','EEE','ECE','MECH','CIVIL','BT','FT','BI','CE','AE'];
b=StringVar()
droplist=OptionMenu(avi,b, *list2)
droplist.config(width=10,fg='black',bg='skyblue')
b.set('Department')
droplist.place(x=440,y=380)

labely=Label(avi,text='Year : ',width=8,font=('bold',10),fg='white',bg='green')
labely.place(x=550,y=380)
list3 = ['1','2','3','4']
a=StringVar()
droplist=OptionMenu(avi,a, *list3)
droplist.config(width=5,fg='black',bg='skyblue')
a.set('Year')
droplist.place(x=630,y=380)

labels = Label(avi,text='Semester : ',width=10,font=('bold',10),fg='white',bg='green')
labels.place(x=730,y=380)

lists = ['1','2']
s=StringVar()
droplist=OptionMenu(avi,s, *lists)
droplist.config(width=5,fg='black',bg='skyblue')
s.set('Sem')
droplist.place(x=830,y=380)


label_4 = Label(avi, text="Address : ",width=15,font=("bold", 10),fg='white',bg='green')
label_4.place(x=85,y=450)

entryarr = Entry(avi,width=40)
entryarr.place(x=230,y=450)
entryarr.config(bg='grey',fg='white',font=('bold',10))

var1 = StringVar()
Radiobutton(avi, text="Hosteler",padx = 0, variable=var1, value = 'hosteler',fg='black',bg='skyblue').place(x=600,y=450)
Radiobutton(avi, text="Day scholar",padx = 10, variable=var1, value = 'dayscholar',fg='black',bg='skyblue').place(x=680,y=450)

labelf = Label(avi,text='Fee : ',width=10,font=('bold',10),bg='green',fg='white')
labelf.place(x=100,y=500)

entryf=Entry(avi)
entryf.place(x=200,y=500)
entryf.config(bg='grey',fg='white',font=('bold',10))

labelaf = Label(avi,text='Hostel Fee : ',width=15,font=('bold',10),bg='green',fg='white')
labelaf.place(x=370,y=500)

entryaf=Entry(avi)
entryaf.place(x=510,y=500)
entryaf.config(bg='grey',fg='white',font=('bold',10))

labelbf = Label(avi,text='Bus Fee : ',width=10,font=('bold',10),bg='green',fg='white')
labelbf.place(x=680,y=500)

entrybf=Entry(avi)
entrybf.place(x=780,y=500)
entrybf.config(bg='grey',fg='white',font=('bold',10))

labelsub = Label(avi,text='subjects : ',width=10,font=('bold',10),bg='green',fg='white')
labelsub.place(x=80,y=550)

entrys1=Entry(avi)
entrys1.place(x=200,y=550)
entrys1.config(bg='grey',fg='white',font=('bold',10),width=15)

entrys2=Entry(avi)
entrys2.place(x=320,y=550)
entrys2.config(bg='grey',fg='white',font=('bold',10),width=15)

entrys3=Entry(avi)
entrys3.place(x=440,y=550)
entrys3.config(bg='grey',fg='white',font=('bold',10),width=15)

entrys4=Entry(avi)
entrys4.place(x=560,y=550)
entrys4.config(bg='grey',fg='white',font=('bold',10),width=15)

entrys5=Entry(avi)
entrys5.place(x=680,y=550)
entrys5.config(bg='grey',fg='white',font=('bold',10),width=15)

entrys6=Entry(avi)
entrys6.place(x=800,y=550)
entrys6.config(bg='grey',fg='white',font=('bold',10),width=15)

def sub():

    if(entry_1.get()!=NONE):


        dab=    d.get() + '/' + e.get() + '/' + f.get()


        import pymysql
        connection = pymysql.connect(host="localhost", user="root", passwd="1234", database="avi", charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:

                sql = "INSERT INTO `regist` (`name`,`fathername`,`email`,`gender`,`dob`,`aadhar`,`roll`,`mobile`,`course`,`department`,`year`,`semester`,`fee`,`hostelfee`,`busfee`,`address`,`stay`,`sub1`,`sub2`,`sub3`,`sub4`,`sub5`,`sub6`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (entry_1.get(), entry.get(),entry_2.get(),var.get(),dab,entryar.get(),entrya.get(),entryp.get(),c.get(),b.get(),a.get(),s.get(),entryf.get(),entryaf.get(),entrybf.get(),entryarr.get(),var1.get(),entrys1.get(),entrys2.get(),entrys3.get(),entrys4.get(),entrys5.get(),entrys6.get()))
            print("affected rows = {}".format(cursor.rowcount))
            connection.commit()


        finally:
            if (cursor.rowcount == 1):
                import tkinter.messagebox
                mes = Tk()
                tkinter.messagebox.showinfo('alert', 'Successfully recorded')
                mes.mainloop()
            else:
                import tkinter.messagebox
                ttt = Tk()
                tkinter.messagebox.showinfo('alert', 'Failed to insert record \ncheck Aadhar or Roll number\ncheck weather you have filled all the data')
                ttt.mainloop()
            connection.close()

def helpi():
    import tkinter.messagebox
    me=Tk()
    tkinter.messagebox.showinfo('help','for further details contact DEO of the department\nitcommonmail@gmail.com')
    me.mainloop()

def searchi():
    import tkinter.messagebox
    me=Tk()
    me.title('Search')
    me.geometry('220x200')
    labelt=Label(me,text='Regd Id: ',fg='white',bg='green',font=('bold',10))
    labelt.place(x=10,y=60)
    entryt=Entry(me)
    entryt.place(x=80,y=60)
    entryt.get()

    def OKi():
        import pymysql
        connection = pymysql.connect(host="localhost", user="root", passwd="1234", database="avi", charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:

                sql = 'SELECT * FROM `REGIST` WHERE roll=(%s);'
                cursor.execute(sql,(entryt.get()))
                data = cursor.fetchone()

            connection.commit()



        finally:

            connection.close()
        if (cursor.rowcount == 1):
            import tkinter.messagebox
            mero = Tk()
            mero.title('Details')
            mero.geometry('280x560')
            ve=data.items()
            ve=list(ve)

            lij=len(ve)
            elk2=Label(mero)
            elk2.pack()
            for i in range(lij):
                elk=Label(mero,text=ve[i],fg='black',font=('bold',10))
                elk.pack()
        else :
            import tkinter.messagebox
            meri = Tk()
            meri.title('Not found')
            meri.geometry('220x130')
            labelde = Label(meri,text='No data found \n student id is not registered',font=('bold',10))
            labelde.place(x=40, y=40)

    Button(me,text='OK',width=8,bg='brown',fg='white',command=OKi).place(x=70,y=100)

def deli():
    import tkinter.messagebox
    mei=Tk()
    mei.geometry('220x130')
    mei.title('password')
    labeld=Label(mei,text='password',fg='white',bg='green')
    labeld.place(x=20,y=40)
    entryd=Entry(mei,show='*')
    entryd.place(x=80,y=40)
    def okie():
        if(entryd.get()=='1234'):
            import tkinter.messagebox
            meri=Tk()
            meri.title('Alert')
            meri.geometry('220x130')
            labelde=Label(meri,text='regd id : ',bg='green',fg='white')
            labelde.place(x=20,y=40)
            entryde=Entry(meri)
            entryde.place(x=80,y=40)

            def delite():
                import pymysql
                connection = pymysql.connect(host="localhost", user="root", passwd="1234", database="avi",
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                try:
                    with connection.cursor() as cursor:

                        sql = 'DELETE  FROM `REGIST` WHERE roll=(%s);'
                        cursor.execute(sql, (entryde.get()))
                        data = cursor.fetchone()

                    connection.commit()



                finally:
                    connection.close()
                    if (cursor.rowcount == 1):
                        import tkinter.messagebox
                        meii = Tk()
                        meii.title('Alert')
                        meii.geometry('220x130')
                        labelde = Label(meii, text='Record deleted successfully')
                        labelde.place(x=40, y=40)
                    else :
                        import tkinter.messagebox
                        meii = Tk()
                        meii.title('Alert')
                        meii.geometry('220x130')
                        labelde = Label(meii, text='Record not deleted \n check the Register id')
                        labelde.place(x=40, y=40)
                meri.mainloop()


            Button(meri,text='submit',bg='brown',fg='white',command=delite).place(x=100,y=80)
        else :
            import tkinter.messagebox
            meri = Tk()
            meri.title('Alert')
            meri.geometry('220x130')
            labelde = Label(meri, text='wrong password \n please enter the correct password')
            labelde.place(x=20, y=40)
            Button(meri, text='ok', bg='brown', fg='white', command=deli).place(x=100, y=80)

    Button(mei,bg='brown',fg='white',text='ok',command=okie).place(x=100,y=80)
    mei.mainloop()




Button(avi, text='Submit',width=20,bg='brown',fg='white',command=sub).place(x=440,y=680)
Button(avi,text='Help',width=20,bg='brown',fg='white',command=helpi).place(x=100,y=750)
Button(avi,text='Search',width=20,bg='brown',fg='white',command=searchi).place(x=750,y=750)
Button(avi,text='Delete',width=20,bg='brown',fg='white',command=deli).place(x=440,y=750)

mainloop()






















#___________________________________________________________________________________________________________________________________________________________________________

                                                                   #JYOTI SINGH[211B157] B5(BY)
#___________________________________________________________________________________________________________________________________________________________________________

try:
    from tkinter import *
except:
    from Tkinter import*
    
from tkinter.messagebox import *

class Test:

    def page9_Add_running(self):
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()
        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date varchar(20) ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number)')


        root=Tk()
        root.title("Add Bus Running Details")
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        fr=Frame(root)
        fr.grid(row=0,column=2,columnspan=100)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//9)
        fr.grid(row=1,column=2,columnspan=10)
        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 
        Label(root,text='Add Bus Running Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=100)
        Label(root,text='').grid(row=3,column=0,padx=60)

        Label(root,text='Bus Id',font="Arial 12 bold").grid(row=3,column=1)
        Bus_Id=Entry(root,font="Arial 12 bold")
        Bus_Id.grid(row=3,column=2)

        Label(root,text='Running Date',font="Arial 12 bold").grid(row=3,column=3)
        Running_Date=Entry(root,font="Arial 12 bold") 
        Running_Date.grid(row=3,column=4)
              
        Label(root,text='Seat Available',font="Arial 12 bold").grid(row=3,column=5)
        Seat_Available=Entry(root,font="Arial 12 bold") 
        Seat_Available.grid(row=3,column=6)

        def Add_Run():
            if len(Bus_Id.get())==0 and len(Running_Date.get())==0 and len(Seat_Available.get())==0:
                showerror('Value Missing','Please Enter The All Values')
            elif len(Bus_Id.get())==0:
                showerror('Value Missing','Please Enter The Bus_Id')
            elif len(Running_Date.get())==0:
                showerror('Value Missing','Please Enter Running_Date')
            elif len(Seat_Available.get())==0:
                showerror('Value Missing','Please Enter Seat_Available')
            elif(Bus_Id.get().isalpha()):
                showerror('Error','Enter Bus Id in numeric')
            
            elif(Seat_Available.get().isalpha()):
                showerror('Error','Enter Seat available in numeric')
            else:
                busID=Bus_Id.get()
                date=Running_Date.get()
                seat=Seat_Available.get()
                y=(busID ,date,seat)
                query='insert into runs(Bus_id ,date,seat_avaiable ) values(?,?,?)'
                cur.execute(query,y)
                con.commit()
                
                Bus_Id.delete(0,END)
                Running_Date.delete(0,END)
                Seat_Available.delete(0,END)
                
                showinfo('Add  runs Entry','Bus runs Record Added')
                quer='select * from runs where bus_id=? and date=?'
                value2=(busID,date)
                cur.execute(quer,value2)
                
                result=cur.fetchall()
                Label(root,text=result,font="arial 10 bold").grid(row=5,column=3,columnspan=50)
            
                
                
        def Delete_Run():
            if len(Bus_Id.get())==0 and len(Running_Date.get())==0 and len(Seat_Available.get())==0:
                showerror('Value Missing','Please Enter The All Values')
            elif(Bus_Id.get())==0:
                showerror('Value Missing','Please Enter The Bus_id')
            elif(len(Running_Date.get())==0 ):
                showerror('Value Missing','Please Enter Running_Date')
            elif len(Seat_Available.get())==0:
                showerror('Value Missing','Please Enter Seat_Available')
            elif(Bus_Id.get().isalpha()):
                showerror('Error','Enter Bus Id in numeric')
            
            elif(Seat_Available.get().isalpha()):
                showerror('Error','Enter Seat available in numeric')
            else:
                y=Bus_Id.get()
                query='select Bus_id from runs where Bus_id=?'
                cur.execute(query,y)
                res=cur.fetchall()
                if(res):
                    showinfo('found','runs Id Exist')
                    x=Bus_Id.get()
                    query='delete from runs where Bus_id=?'
                    cur.execute(query,x)
                    con.commit()
                    Label(root,text='           Deleted         ',font="arial 10 bold",bg='alice blue').grid(row=5,column=3,columnspan=50)
                    Bus_Id.delete(0,END)
                    Running_Date.delete(0,END)
                    Seat_Available.delete(0,END)
                    
                    showinfo('Deleted','Run Detail Deleted Successfully')
                    
                else:
                    Bus_Id.delete(0,END)
                    Running_Date.delete(0,END)
                    Seat_Available.delete(0,END)
                    showerror('error','Runs Id not Exist')
                
            


        def Page2_features():
            root.destroy()
            self.Page2_features()

        Button(root,text="Add Run",font="Arial 15 bold",bg="light green",command=Add_Run,bd=7).grid(row=3,column=8)     
        Button(root,text="Delete Run",font="Arial 15 bold",bg="light green",fg="red",command=Delete_Run,bd=7).grid(row=3,column=9)
        Home_img=PhotoImage(file=".\\home.png")     
        Button(root,image=Home_img,bg="light green",command=Page2_features).grid(row=3,column=10)       

        root.mainloop()

                             


        

    def page8_add_Route(self):
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()
        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date varchar(20) ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number)')

        root=Tk()
        root.title("Add Route")
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        fr=Frame(root)
        fr.grid(row=0,column=2,columnspan=10)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//10)
        fr.grid(row=1,column=2,columnspan=10)
        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40)

        Label(root,text='Add Bus Route Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)

        Label(root,text='',bg='alice blue').grid(row=3,column=0,padx=100)

        Label(root,text='Route Id',font="Arial 12 bold").grid(row=3,column=1)
        Route_Id=Entry(root,font="Arial 12 bold")       
        Route_Id.grid(row=3,column=2)

        Label(root,text='Station Name',font="Arial 12 bold").grid(row=3,column=3)
        Station_Name=Entry(root,font="Arial 12 bold") 
        Station_Name.grid(row=3,column=4)

        Label(root,text='Station ID',font="Arial 12 bold").grid(row=3,column=5)
        Station_ID=Entry(root,font="Arial 12 bold") 
        Station_ID.grid(row=3,column=6)

        def Add_Route():
            if len(Route_Id.get())==0 and len(Station_Name.get())==0 and len(Station_ID.get())==0:
                showerror('Value Missing','Please Enter The Values')
            elif len(Route_Id.get())==0:
                showerror('Value Missing','Please Enter The Route_Id')
            elif len(Station_Name.get())==0:
                showerror('Value Missing','Please Enter Station_Name')
            elif len(Station_ID.get())==0:
                showerror('Value Missing','Please Enter Station_ID')
            elif(Route_Id.get().isalpha()):
                showerror('Error','Enter Route Id in numeric')
            elif(Station_Name.get().isnumeric()):
                showerror('Error','Enter Station Name correctly')
            
            elif(Station_ID.get().isalpha()):
                showerror('Error','Enter Station Id in numeric')
            else:
                route=Route_Id.get()
                station=Station_Name.get()
                stationid=Station_ID.get()
                
                y=(route ,station ,stationid)
                query=('insert into route(route_id,station_name ,station_id) values(?,?,?)')
                cur.execute(query,y)
                con.commit()
                showinfo('Add  Route Entry','Bus route Record Added')
                query2='select * from route where route_id=? and station_id=?'
                valu=(Route_Id.get(),Station_ID.get())

                cur.execute(query2,valu)

                result=cur.fetchall()
                Label(root,text=result,font='arial 10 bold').grid(row=4,column=4)
                Route_Id.delete(0,END)
                Station_Name.delete(0,END)
                Station_ID.delete(0,END)
                
            
        def Delete_Route():
            if len(Route_Id.get())==0 and len(Station_Name.get())==0 and len(Station_ID.get())==0:
                showerror('Value Missing','Please Enter The All Values')
            elif len(Route_Id.get())==0:
                showerror('Value Missing','Please Enter The Route_Id')
            elif len(Station_Name.get())==0:
                showerror('Value Missing','Please Enter Station_Name')
            elif len(Station_ID.get())==0:
                showerror('Value Missing','Please Enter Station_ID')
            elif(Route_Id.get().isalpha()):
                showerror('Error','Enter Route Id in numeric')
            elif(Station_Name.get().isnumeric()):
                showerror('Error','Enter Station Name correctly')
            
            elif(Station_ID.get().isalpha()):
                showerror('Error','Enter Station Id in numeric')
            else:    
                y=Route_Id.get()
                query='select route_id from route where route_id=?'
                cur.execute(query,y)
                res=cur.fetchall()
                
                if(res):
                    showinfo('found','Route Id Exist')
                    x=(Route_Id.get(),Station_ID.get())
                    query='delete from route where route_id=? and station_id=?'
                    cur.execute(query,x)
                    con.commit()
                    Label(root,text='                Deleted            ',font='arial 10 bold',bg='alice blue').grid(row=4,column=4)
                    Route_Id.delete(0,END)
                    Station_Name.delete(0,END)
                    Station_ID.delete(0,END)
                    showinfo('Deleted','Route Detail Deleted Successfully')
                    
                else:
                    Route_Id.delete(0,END)
                    Station_Name.delete(0,END)
                    Station_ID.delete(0,END)
                    showerror('Error','Route Id not Exist')
            
        def Page2_features():
            root.destroy()
            self.Page2_features()

       
        Button(root,text="Add Route",font="Arial 15 bold",bg="light green",command=Add_Route,bd=5).grid(row=3,column=7,padx=10)   
        Button(root,text="Delete Route",font="Arial 15 bold",bg="light green",fg="red",command=Delete_Route,bd=5).grid(row=3,column=8,pady=50)
        Home_img=PhotoImage(file=".\\home.png")    
        Button(root,image=Home_img,bg="light green",command=Page2_features).grid(row=4,column=8)      

        root.mainloop()

                          

        

    def page7_bus_details(self):
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()
        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date varchar(20) ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number)')



        root=Tk()
        root.title('Bus Details')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        fr=Frame(root)
        fr.grid(row=0,column=2,columnspan=10)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//15)
        fr.grid(row=1,column=2,columnspan=10)
        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 
        Label(root,text='Add Bus Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10,pady=20)
        Label(root,text='').grid(row=3,column=0,padx=5)
        Label(root,text='Bus Id',font="Arial 12 bold").grid(row=3,column=1)

        Bus_id=Entry(root,font="Arial 12 bold")        
        Bus_id.grid(row=3,column=2,padx=0)

        Label(root,text='Bus Type',font="Arial 12 bold").grid(row=3,column=3)
        Bus_type=StringVar()
        opt=["AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2X1","Non-AC-Sleeper 2X1"]
        Bus_type.set('Bustype')
        d_menu=OptionMenu(root,Bus_type,*opt).grid(row=3,column=4)          
        Label(root,text='Capacity',font="Arial 12 bold").grid(row=3,column=5)
        Capacity=Entry(root,font="Arial 12 bold") 
        Capacity.grid(row=3,column=6)
        Label(root,text='Fare Rs',font="Arial 12 bold").grid(row=3,column=7)
        Fare=Entry(root,font="Arial 12 bold") 
        Fare.grid(row=3,column=8)
        Label(root,text='Operator ID',font="Arial 12 bold").grid(row=3,column=9)

        Operator_ID=Entry(root,font="Arial 10 bold") 
        Operator_ID.grid(row=3,column=10)
        Label(root,text='Route ID',font="Arial 12 bold").grid(row=3,column=11)
        Route_id=Entry(root,font="Arial 12 bold") 
        Route_id.grid(row=3,column=12,pady=10)
        def Add_Bus():
            if len(Operator_ID.get())==0 and len(Route_id.get())==0 and len(Fare.get())==0 and len(Capacity.get())==0 and len(Bus_id.get())==0:
                showerror('Value Missing','Please Enter The All Values')
            elif len(Operator_ID.get())==0 :
                showerror('Value Missing','Please Enter The Operator_ID')
            elif len(Route_id.get())==0 :
                showerror('Value Missing','Please Enter The Route_id')
            elif len(Fare.get())==0 :
                showerror('Value Missing','Please Enter The Fare')
            elif len(Capacity.get())==0 :
                showerror('Value Missing','Please Enter The Capacity')
            elif len(Bus_id.get())==0:
                showerror('Value Missing','Please Enter The Bus_ID')
            elif(Operator_ID.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(Route_id.get().isalpha()):
                showerror('Error','Enter Route Id in numeric')
            elif(Fare.get().isalpha()):
                showerror('Error','Enter Fare in numeric')
            elif(Capacity.get().isalpha()):
                showerror('Error','Enter Capacity in numeric')
            elif(Bus_id.get().isalpha()):
                showerror('Error','Enter Bus id in numeric')
            else:
                y=(Bus_id.get(),Bus_type.get(),Capacity.get(),Fare.get(),Operator_ID.get(),Route_id.get())
                query=('insert into bus(Bus_id ,type ,capacity,fare, route_id,operator_id) values(?,?,?,?,?,?)')
                cur.execute(query,y)
                con.commit()
            
                showinfo('Add Bus Entry','Bus Record Added')
                value=Bus_id.get()
                cur.execute('select * from bus where bus_id=(?)',[value])
                result=cur.fetchall()
                Operator_ID.delete(0,END)
                Route_id.delete(0,END)
                Fare.delete(0,END)
                Capacity.delete(0,END)
                Bus_id.delete(0,END)
                Label(root,text=result,font='arial 10 bold').grid(row=7,column=2,columnspan=100)

                 
            
                
        def Edit_Bus():
            if len(Operator_ID.get())==0 and len(Route_id.get())==0 and len(Fare.get())==0 and len(Capacity.get())==0 and len(Bus_id.get())==0:
                showerror('Value Missing','Please Enter The All Values')
            elif len(Operator_ID.get())==0 :
                showerror('Value Missing','Please Enter The Operator_ID')
            elif len(Route_id.get())==0 :
                showerror('Value Missing','Please Enter The Route_id')
            elif len(Fare.get())==0 :
                showerror('Value Missing','Please Enter The Fare')
            elif len(Capacity.get())==0 :
                showerror('Value Missing','Please Enter The Capacity')
            elif len(Bus_id.get())==0:
                showerror('Value Missing','Please Enter The Bus_ID')
            elif(Operator_ID.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(Route_id.get().isalpha()):
                showerror('Error','Enter Route Id in numeric')
            elif(Fare.get().isalpha()):
                showerror('Error','Enter Fare in numeric')
            elif(Capacity.get().isalpha()):
                showerror('Error','Enter Capacity in numeric')
            elif(Bus_id.get().isalpha()):
                showerror('Error','Enter Bus id in numeric')
            else:
                y=(Bus_id.get())
                query='select * from bus where bus_id=?'
                cur.execute(query,y)
                res=cur.fetchall()
                if(res):
                    showinfo('Found','record found')
                    y=(Bus_type.get(),Capacity.get(),Fare.get(),Route_id.get(),Operator_ID.get(),Bus_id.get())
                    query='update bus set type=? ,capacity=?,fare=?,route_id=?,operator_id =? where bus_id=?'
                    cur.execute(query,y)
                    con.commit()
                    quer='select * from bus where bus_id=?'
                    cur.execute(quer,Bus_id.get())
                    result=cur.fetchall()
                    Label(root,text=result,font='arial 10 bold').grid(row=7,column=2,columnspan=100)
                    showinfo('Bus Entry Edit','Bus Record Edited Successfully') 
                else:
                    showerror('not found','error')
                Operator_ID.delete(0,END)
                Route_id.delete(0,END)
                Fare.delete(0,END)
                Capacity.delete(0,END)
                Bus_id.delete(0,END)    
                 
                

        def Page2_features():
            root.destroy()
            self.Page2_features()
        Button(root,text="Add Bus",font="Arial 15 bold",bg="light green",command=Add_Bus,bd=5).grid(row=4,column=7)    
        Button(root,text="Edit Bus",font="Arial 15 bold",bg="light green",command=Edit_Bus,bd=5).grid(row=4,column=8)
        Home_img=PhotoImage(file=".\\home.png")    
        Button(root,image=Home_img,bg="light green",command=Page2_features).grid(row=4,column=9)        

        root.mainloop()

                            


        

    def Page6_operator_details(self):
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date varchar(20) ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number)')


        root=Tk()
        Operator_id=0
        Operator_Name=0
        Ph_Number=0
        Address=0    
        Email=0
        root.title('Operator Details')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=100)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//10+420,columnspan=100)
        fr.grid(row=1,column=0,columnspan=100)

        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=0,pady=40,columnspan=100) 
        Label(root,text='Add Bus Operator Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=0,columnspan=100,pady=5) 

        Label(root,text='Operator id',font="Arial 11 bold").grid(row=3,column=47)
        Operator_id=Entry(root,font="Arial 10 bold")     
        Operator_id.grid(row=3,column=48)

        Label(root,text='Name',font="Arial 11 bold").grid(row=3,column=49)
        Operator_Name=Entry(root,font="Arial 10 bold")
        Operator_Name.grid(row=3,column=50)          

        Label(root,text='Address',font="Arial 11 bold").grid(row=3,column=51)
        Address=Entry(root,font="Arial 10 bold")
        Address.grid(row=3,column=52)

        Label(root,text='Phone',font="Arial 11 bold").grid(row=3,column=53)
        Ph_Number=Entry(root,font="Arial 10 bold")     
        Ph_Number.grid(row=3,column=54)

        Label(root,text='Email',font="Arial 11 bold").grid(row=3,column=55)
        Email=Entry(root,font="Arial 10 bold")     
        Email.grid(row=3,column=56)

        def Add_De():
            if(len(Operator_id.get())==0 and len(Operator_Name.get())==0 and len(Address.get())==0 and len(Ph_Number.get())==0 and len(Email.get())==0):
                showerror('Value Missing','Please Enter The All Values')
            elif(len(Operator_id.get())==0):
                showerror('Value Missing','Please Enter The Operator_id')
            elif(len(Operator_Name.get())==0):
                showerror('Value Missing','Please Enter The Operator_Name')
            elif(len(Address.get())==0):
                showerror('Value Missing','Please Enter The Address')
            elif(len(Ph_Number.get())==0):
                showerror('Value Missing','Please Enter The Ph_Number')
            elif(len(Email.get())==0):
                showerror('Value Missing','Please Enter The Email')
            elif(Operator_id.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(Operator_Name.get().isnumeric()):
                showerror('Error','Enter Operator Name correctly')
            elif(Address.get().isnumeric()):
                showerror('Error','Enter Address correctly')
            elif(Ph_Number.get().isalpha()):
                showerror('Error','Enter Mobile no. correctly')
            elif(len(Ph_Number.get())!=10):
                showerror('Error','Enter Mobile no. correctly 10 digits')
            else:
                operatorid=Operator_id.get()
                operatorname=Operator_Name.get()
                addressoperator=Address.get()
                phonenumber=Ph_Number.get()
                operatoremail=Email.get()

                query='insert into operator(operator_id,Name,address,phone,email) values(?,?,?,?,?)' 
                value=(operatorid,operatorname,addressoperator,phonenumber,operatoremail)
                cur.execute(query,value)
                con.commit()
                quer='select *from operator where operator_id=?'
                cur.execute(quer,operatorid)
                result=cur.fetchall()
                Label(root,text=result,font='arial 11 bold').grid(row=5,column=10,columnspan=100)
                
                Operator_id.delete(0,END)
                Operator_Name.delete(0,END)
                Address.delete(0,END)
                Ph_Number.delete(0,END)
                Email.delete(0,END)
                showinfo('Operator Entry','Operator Record Added successfully')
                
                
        def Edit_De():
            if(len(Operator_id.get())==0 and len(Operator_Name.get())==0 and len(Address.get())==0 and len(Ph_Number.get())==0 and len(Email.get())==0):
                showerror('Value Missing','Please Enter The Values')
            elif(len(Operator_id.get())==0):
                showerror('Value Missing','Please Enter The Operator_id')
            elif(len(Operator_Name.get())==0):
                showerror('Value Missing','Please Enter The Operator_Name')
            elif(len(Address.get())==0):
                showerror('Value Missing','Please Enter The Address')
            elif( len(Ph_Number.get())==0):
                showerror('Value Missing','Please Enter The Ph_Number')
            elif(len(Email.get())==0):
                showerror('Value Missing','Please Enter The Email')
            elif(Operator_id.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(Operator_Name.get().isnumeric()):
                showerror('Error','Enter Operator Name correctly')
            elif(Address.get().isnumeric()):
                showerror('Error','Enter Address correctly')
            elif(Ph_Number.get().isalpha()):
                showerror('Error','Enter Mobile no. correctly')
            elif(len(Ph_Number.get())!=10):
                showerror('Error','Enter Mobile no. correctly 10 digits')
            else:

                operatorid=Operator_id.get()
                operatorname=Operator_Name.get()
                addressoperator=Address.get()
                phonenumber=Ph_Number.get()
                operatoremail=Email.get()
                
                query1='select operator_id from operator where operator_id=?'
                cur.execute(query1,operatorid)
                res=cur.fetchall()
                if(res):
                    showinfo('Found','Operator ID Exixts')
                    query1='update operator set name=?,address=?,phone=?,email=? where operator_id=?'
                    value=(operatorname,addressoperator,phonenumber,operatoremail,operatorid)
                    cur.execute(query1,value)
                    con.commit()

                    query2='select * from operator where operator_id=?'
                    cur.execute(query2,operatorid)
                    result=cur.fetchall()
                    Label(root,text=result,font='arial 11 bold').grid(row=5,column=10,columnspan=100)

                    Operator_id.delete(0,END)
                    Operator_Name.delete(0,END)
                    Address.delete(0,END)
                    Ph_Number.delete(0,END)
                    Email.delete(0,END)
                
                    showinfo("Success","Edited Successfully")
                else:
                    showerror('Not found','Operator ID not exists')

        def Page2_features():
            root.destroy()
            self.Page2_features()
            
        Button(root,text="Add",font="Arial 15 bold",bg="light green",command=Add_De).grid(row=3,column=58,padx=0)
        Button(root,text="Edit",font="Arial 15 bold",bg="light green",command=Edit_De).grid(row=3,column=60,pady=20)
        Home_img=PhotoImage(file=".\\home.png")    
        Button(root,image=Home_img,bg="light green",command=Page2_features).grid(row=3,column=61)

        root.mainloop()





    def page5_check_booking(self):
        #Create the database in python
        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date varchar(20) ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number)')


        root=Tk()
        root.title('Check Your Booking')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
            
        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=20)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//4+210,columnspan=100)
        fr.grid(row=1,column=0,columnspan=20)
        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=100,pady=17)
        Label(root,text="Check Your Booking",font="Arial 15 bold",fg='black',bg="light green").grid(row=2,column=0,pady=40,columnspan=20)
        Label(root,text="").grid(row=3,column=0,padx=140)
        Label(root,text="Enter your Mobile No:",font="Arial 12 bold").grid(row=3,column=3)
        En_Mobile=Entry(root,font="Arial 12 bold")
        En_Mobile.grid(row=3,column=4)

        def Page2_features():
            root.destroy()
            self.Page2_features()

        def check_booking():
            if len(En_Mobile.get())==0:
                showerror('Value Missing','Please Enter Mobile No.')
            elif(En_Mobile.get().isalpha()):
                showerror('Error','Please Enter Mobile No. in Numeric')
            elif(len(En_Mobile.get())!=10):
                showerror('Error','Enter Mobile no. correctly 10 digits')
                
            else:
                frame=Frame(root,relief="groove",bd=7)
                frame.grid(row=5,column=0,columnspan=100)

                value=En_Mobile.get()
                cur.execute('select  * from booking_history where mobile=(?)',[value])

                res=cur.fetchall()
                if(res):
                    Label(root,text="Bus Ticket",font='arial 15 bold',fg='orange red').grid(row=4,column=4,)
                    Label(frame,text="Passenger:",font='Arial 10 bold',fg='blue').grid(row=3,column=0,)
                    Label(frame,text=res[0][0],font='Arial 10 bold').grid(row=3,column=1,)
                
                    Label(frame,text="Gender:",font='Arial 10 bold',fg='blue').grid(row=3,column=3,)
                    Label(frame,text=res[0][1],font='Arial 10 bold').grid(row=3,column=4,)
                
                    Label(frame,text="No. Of Seat:",font='Arial 10 bold',fg='blue').grid(row=4,column=0,)
                    Label(frame,text=res[0][2],font='Arial 10 bold').grid(row=4,column=1,)
                
                    Label(frame,text="Phone:",font='Arial 10 bold',fg='blue').grid(row=4,column=3,)
                    Label(frame,text=res[0][3],font='Arial 10 bold').grid(row=4,column=4,)
                
                    Label(frame,text="Age:",font='Arial 10 bold',fg='blue').grid(row=5,column=0)
                    Label(frame,text=res[0][4],font='Arial 10 bold').grid(row=5,column=1,)
                
                    Label(frame,text="Bus Name:",font='Arial 10 bold',fg='blue').grid(row=5,column=3,)
                    Label(frame,text=res[0][5],font='Arial 10 bold').grid(row=5,column=4,)
                
                    Label(frame,text="From:",font='Arial 10 bold',fg='blue').grid(row=6,column=0)
                    Label(frame,text=res[0][6],font='Arial 10 bold').grid(row=6,column=1,)
                
                    Label(frame,text="To:",font='Arial 10 bold',fg='blue').grid(row=6,column=3)
                    Label(frame,text=res[0][7],font='Arial 10 bold').grid(row=6,column=4)
                
                    Label(frame,text="Travel on:",font='Arial 10 bold',fg='blue').grid(row=7,column=0)
                    Label(frame,text=res[0][8],font='Arial 10 bold' ).grid(row=7,column=1)
                
                    Label(frame,text="Fare:",font='Arial 10 bold',fg='blue').grid(row=7,column=3)
                    Label(frame,text=res[0][2]*res[0][9],font='Arial 10 bold').grid(row=7,column=4)
                    value=str(res[0][2]*res[0][9])

                    Label(root,text="Your fare price is  Rs."+value,font='Arial 13 bold',fg='deep pink',bg='alice blue').grid(row=9,column=0,columnspan=82)
                    showinfo('Check Boooking Entry','Successfully Checked')
                    En_Mobile.delete(0,END)
                else:
                    showerror('Error','No booking with this Mobile no.')
                    if(askyesno('Booking','Do you want to do booking?')):
                        root.destroy()
                        self.Page3_Enter_Journey_Details_Show_Bus()
                

  
            
        Button(root,text="Check Booking",font="Arial 12 bold",command=check_booking,bd=4).grid(row=3,column=5)
        img_home=PhotoImage(file=".\\home.png")             
        
        
        Button(root,image=img_home,bg="light green",command=Page2_features).grid(row=3,column=7)

        root.mainloop()

        

    def Page4_Add_new_details_to_database(self):
        root=Tk()
        root.title('Add new details to database')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        
        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=10)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        
        Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//4+200)
        
        fr.grid(row=1,column=0,columnspan=10)
        
        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=20,pady=20)
        Label(root,text="Add New Details to DataBase",font="Arial 15 bold",fg='green',bg="white").grid(row=2,column=0,pady=20,columnspan=20)
        Label(root,text="").grid(row=3,column=0,padx=150)

        def Page6_operator_details():
            root.destroy()
            self.Page6_operator_details()
        def page7_bus_details():
            root.destroy()
            self.page7_bus_details()
        def page8_add_Route():
            root.destroy()
            self.page8_add_Route()
        def page9_Add_running():
            root.destroy()
            self.page9_Add_running()
        def Page2_features():
            root.destroy()
            self.Page2_features()
            
        Button(root,text="New Operator",font="Arial 11 bold",bg="light green",fg="black",command=Page6_operator_details).grid(row=3,column=1)

        Button(root,text="New Bus",font="Arial 11 bold",bg="tomato",fg="black",command=page7_bus_details).grid(row=3,column=2)

        Button(root,text="New Route",font="Arial 11 bold",bg="steel blue3",fg="black",command=page8_add_Route).grid(row=3,column=3)

        Button(root,text="New Run",font="Arial 11 bold",fg='black',bg='rosy brown',command=page9_Add_running).grid(row=3,column=4)
        Home_img=PhotoImage(file=".\\home.png")     
        Button(root,image=Home_img,bg="light green",command=Page2_features).grid(row=3,column=5)

        root.mainloop()
               

    

    def Page3_Enter_Journey_Details_Show_Bus(self):
        root=Tk()

        import sqlite3
        con=sqlite3.Connection('Bus_Booking')
        cur=con.cursor()

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
        cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(Bus_id) references runs(Bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(Bus_id number,date date ,seat_avaiable number,PRIMARY KEY(Bus_id,date))')
        #cur.execute('drop table booking_history')
        cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile varchar(10) PRIMARY KEY,age number,bus_select number,t_o varchar(13),fr varchar(13),date date,fare number,current_date varchar(20))')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #root.geometry('%dx%d+0+0'%(w,h))
        root.state("zoomed")

        root.title("Enter Journey Details")
        bus_select=IntVar()
        Bus1=0
        Bus2=0

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        img_home=PhotoImage(file=".\\home.png")
        Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)                               

        Label(root,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81,pady=30)
        Label(root,text="Enter Journey Details",font="Arial 20 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

        Label(root,text="To",font="Arial 15 bold").grid(row=3,column=33)
        To=Entry(root,font="Arial 10 bold")
        To.grid(row=3,column=34)

        Label(root,text="From",font="Arial 15 bold").grid(row=3,column=35)
        From=Entry(root,font="Arial 10 bold")
        From.grid(row=3,column=36)

        Label(root,text="Journey Date",font="Arial 15 bold").grid(row=3,column=37)
        #JDate=Entry(root,font="Arial 10 bold")
        #JDate.insert(0,"dd/mm/yyyy")
        JDate=Entry(root)
        JDate.grid(row=3,column=38)
        Label(root,text='dd/mm/yyyy',font='Arial 15 bold').grid(row=4,column=38)
        dict={}
        def show_bus():
            if(To.get().isspace() or From.get().isspace() or JDate.get().isspace()):
                showerror("Error","Missing!")
            elif(len(To.get())==0 and len(From.get())==0 and len(JDate.get())==0):
                showerror("Missing","Enter all the fields")
            elif(len(To.get())==0):
                showerror("Missing","Enter the source")
            elif len(From.get())==0:
                showerror("Missing","Enter the destination")
            elif len(JDate.get())==0:
                showerror("Missing","Enter the date")
         
            elif(To.get().isnumeric() or From.get().isnumeric()):
                showerror("Missing","Enter city names correctly!")
            
            else:
                to=To.get()
                fr=From.get()
                Jd=JDate.get()

                value=(to,fr,Jd)
                query='select name,type,seat_avaiable,capacity,fare,runs.bus_id from operator,bus,runs,route as t,route as f where operator.operator_id=bus.operator_id and bus.bus_id=runs.bus_id and bus.route_id=t.route_id and t.station_name=? and f.station_name=? and date=?'
                cur.execute(query,value)
                res=cur.fetchall()
                #print(res)
                
                i=1
                for a in res:
                    dict.update({i:a})
                    n=0
                    for b in a:
                        Bus1=Radiobutton(root,text="BUS"+str(i),variable=bus_select,value=i,font="Arial 10 bold")
                        Bus1.grid(row=6+i,column=33)
                        Label(root,text=b,font="Arial 10 bold").grid(row=6+i,column=34+n)
                        n=n+1
                    i=i+1
                #print(res)
                #print(dict)
                #print(dict[int(bus_select)])


                
                Label(root,text=" ").grid(row=4,column=0)
                Label(root,text="Select Bus",font="Arial 13 bold",fg="dark green").grid(row=5,column=33)
                Label(root,text="Operator",font="Arial 13 bold",fg="dark green").grid(row=5,column=34)
                Label(root,text="Bus Type",font="Arial 13 bold",fg="dark green").grid(row=5,column=35)
                Label(root,text="Available Seats",font="Arial 13 bold",fg="dark green").grid(row=5,column=36)
                Label(root,text="Total Seats",font="Arial 13 bold",fg="dark green").grid(row=5,column=37)
                Label(root,text="Fare",font="Arial 13 bold",fg="dark green").grid(row=5,column=38)
                Label(root,text="Bus ID",font="Arial 13 bold",fg="dark green").grid(row=5,column=39)
                Button(root,text="Proceed To Book",font="Arial 13 bold",bg="light green",fg="black",border=5,command=proceed_to_book).grid(row=6,column=40)

                ''''
                Bus1=Radiobutton(root,text="BUS1",variable=bus_select,value=1,font="Arial 10 bold")
                Bus1.grid(row=7,column=33)
                Bus2=Radiobutton(root,text="BUS2",variable=bus_select,value=2,font="Arial 10 bold")
                Bus2.grid(row=8,column=33)
                Bus3=Radiobutton(root,text="BUS3",variable=bus_select,value=3,font="Arial 10 bold")
                Bus3.grid(row=9,column=33)
                Bus4=Radiobutton(root,text="BUS4",variable=bus_select,value=4,font="Arial 10 bold")
                Bus4.grid(row=10,column=33)
        '''

                


        def proceed_to_book():
            if bus_select.get()==0:
                showerror('Select','Please Select Bus')
            else:
                #print(bus_select.get())
                k=bus_select.get()
                #print(dict[k])
                pass_details=dict[k]
                #print(ans[0],ans[3])
                Label(root,text="Fill Passenger Details To Book The Bus Ticket",font="Arial 20 bold",bg="light blue",fg="red").grid(row=13,column=0,columnspan=81,pady=30)

                Label(root,text="Name",font="Arial 15 bold").grid(row=14,column=33)
                name=Entry(root,font="Arial 10 bold")
                name.grid(row=14,column=34)

                Label(root,text="Gender",font="Arial 10 bold").grid(row=14,column=35)
                gender=StringVar()
                gender.set("Gender")
                opt=("Male","Female","Other")
                d_menu=OptionMenu(root,gender,*opt).grid(row=14,column=36)

                Label(root,text="No. Of Seats",font="Arial 15 bold").grid(row=14,column=37)
                seat=Entry(root,font="Arial 10 bold")
                seat.grid(row=14,column=38)

                Label(root,text="Mobile No.",font="Arial 15 bold").grid(row=14,column=39)
                mobile=Entry(root,font="Arial 10 bold")
                mobile.grid(row=14,column=40)

                Label(root,text="Age",font="Arial 15 bold").grid(row=14,column=41)
                age=Entry(root,font="Arial 10 bold")
                age.grid(row=14,column=42)
                def book_seat():
                    if(len(name.get())==0 and len(seat.get())==0 and len(age.get())==0 and len(mobile.get())==0):
                        showerror("Missing","Enter all the fields")
                    elif len(name.get())==0 :
                        showerror("Missing","Enter The name")
                    elif len(seat.get())==0 :
                        showerror("Missing","Enter The seat")
                    elif len(mobile.get())==0:
                        showerror("Missing","Enter The Mobile_number")
                    elif len(age.get())==0:
                        showerror("Missing","Enter The age")
                    elif(name.get().isnumeric()):
                        showerror("Missing","Enter Name correctly!")
                    elif(seat.get().isalpha()):
                        showerror("Error","Enter the seat in numeric")
                    elif(len(mobile.get())!=10) or mobile.get().isalpha():
                        showerror("Error","Enter 10 digit Mobile no.")
                    elif(age.get().isalpha() or int(age.get())<=11 or int(age.get())>100 ):
                        showerror("Missing","Enter age correctly!")
                    else:
                        s=int(seat.get())
                        f=int(pass_details[4])
                        v=s*f
                        if(askyesno('Confirm','Do you want to proceed ? Total fare is Rs.'+str(v))):
                            m=int(pass_details[2])
                            n=int(seat.get())
                            if(m-n>=0):
                                query1='update runs set seat_avaiable=(?) where bus_id=? and date=?'
                                value1=((m-n),pass_details[5],JDate.get())
                                cur.execute(query1,value1)
                                con.commit()
                                
                                value=(name.get(),gender.get(),seat.get(),mobile.get(),age.get(),pass_details[0],To.get(),From.get(),JDate.get(),pass_details[4])
                                query='insert into Booking_history(passenger_name,Gender,No_of_seats,mobile,age,bus_select,t_o,fr,date,fare)values(?,?,?,?,?,?,?,?,?,?)'
                                cur.execute(query,value)
                                con.commit()
                                #value1=(mobile.get())
                                #query1='select * from Booking_history where mobile =?'
                        
                                #cur.execute(query1,value1)
                                #res=cur.fetchall()
                        
                                #Label(root,text=res,font="Arial 8 bold").grid(row=15,column=37) 
                                showinfo("Success","Booked Successfully")
                                s=int(seat.get())
                                f=int(pass_details[4])
                                v=s*f
                                showinfo('Fare','Fare is Rs.'+str(v))
                                if(askyesnocancel('Ticket','Want to get the TICKET')):
                                    root.destroy()
                                    self.page5_check_booking()
                                else:
                                    root.destroy()
                                    self.Page2_Home_Page()
                            else:
                                showerror('Error','Seats not available')
                            
                        
                
                    

                Button(root,text="Book Seat",font="Arial 13 bold",bg="light green",fg="black",command=book_seat,bd=5).grid(row=14,column=43)
            


            
        Button(root,text="Show Bus",font="Arial 13 bold",bg="seagreen3",fg="black",command=show_bus,bd=5).grid(row=3,column=39)

        def Page2_features():
            root.destroy()
            self.Page2_features()
        Button(root,image=img_home,bg='light green',command=Page2_features).grid(row=3,column=40)
                                                                                        

        root.mainloop()
        
    
    

    def Page2_features(self):

        root=Tk()
        root.title('Features')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))


        def fun1():
            root.destroy()
            self.Page3_Enter_Journey_Details_Show_Bus()
        def fun2():
            root.destroy()
            self.page5_check_booking()
        def fun3():
            root.destroy()
            self.Page4_Add_new_details_to_database()
        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=10)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=1,padx=w//3+120)
        fr.grid(row=1,column=0,columnspan=12)
        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=1,pady=60)
        Label(root,text="").grid(row=2,column=0,padx=w//9)
        Button(root,text="Seat Booking",font="Arial 15 bold",bg="light green",fg="black",command=fun1).grid(row=2,column=1,padx=15)

        Button(root,text="Check Booked Seat",font="Arial 15 bold",bg="green3",fg="black",command=fun2).grid(row=2,column=2,padx=50)

        Button(root,text="Add Bus Details",font="Arial 15 bold",bg="green",fg="black",command=fun3).grid(row=2,column=4)

        Label(root,text="For Admin Only",font="Arial 10 bold",fg='red',bg='alice blue').grid(row=3,column=4,pady=30)


        root.mainloop()


    def intro(self):
        
         
        root=Tk()
        root.title('Online Bus Booking System')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.geometry('%dx%d+0+0'%(w,h))
        Bus_img=PhotoImage(file=".\\Bus_for_project.png")
        Label(root,image=Bus_img).pack()
        Label(root,text='Online Bus Booking System',font="Arial 25 bold",bg="light blue",fg="red").pack(pady=20)
             

        Label(root,text='Name: JYOTI SINGH',font="Arial 15 bold", fg='blue').pack(pady=20)
             
        Label(root,text='Enrollment No: 211B157',font="Arial 15 bold",fg='blue').pack(pady=20)
             
        Label(root,text='Mobile: 7049022984',font="Arial 15 bold", fg='blue').pack(pady=20)
             
        Label(root,text='Submitted to: Dr. Mahesh Kumar',font="Arial 20 bold",bg="light blue",fg="red").pack(pady=20)

        Label(root,text='Project Based Learing',font="Arial 13 bold",fg="red").pack()
       
        def close(e=0):
            root.destroy()
            self.Page2_features()
        root.after(5000,close)
               
        root.mainloop()                          
      
t=Test()
t.intro()
                                                                            





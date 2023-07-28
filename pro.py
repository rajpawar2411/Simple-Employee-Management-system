from tkinter import *
from tkinter.messagebox import *
from requests import *
from PIL import ImageTk,Image
from sqlite3 import *
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt

def location():
	wa="https://ipinfo.io/"
	res=get(wa)
	
	data=res.json()
	city_name=data["city"]
	state_name=data["region"]
	msg="Location: "+" " + str(city_name) + "," + state_name
	lb.config(text=msg)

def temprature():
	a1="https://api.openweathermap.org/data/2.5/weather"
	a2="?q=thane"
	a3="&appid=" + "a804c955ff896c1385910d5013811f8d"
	a4="&units=" + "metric"
	wa2 = a1+a2+a3+a4
	res2=get(wa2)
	data2=res2.json()
	temp=data2["main"]["temp"]
	msg2="Temprature: "+" " + str(temp) + "\u2103"
	lb2.config(text=msg2)
def f1():
	addw.deiconify()
	mw.withdraw()
def f2():
	mw.deiconify() 
	addw.withdraw()
def add():
	id=id_ent.get()
	id=id.strip()
	if (id==""):
		showwarning("!","ID cannot be empty!")
		id_ent.delete(0,END)
		id_ent.focus()
		return
	elif (not id.isdigit()):
		showwarning("!","ID cannot be string")
		id_ent.delete(0,END)
		id_ent.focus()
		return


	name=nm_ent.get()
	name=name.strip()
	if (name==""):
		showwarning("!","name cannot be empty!")
		nm_ent.delete(0,END)
		nm_ent.focus()
		return
	elif (not name.isalpha()):
		showwarning("!","name cannot have numbers")
		nm_ent.delete(0,END)
		nm_ent.focus()
		return
	elif len(name)<=2:
		showwarning("!","name is too short")
		nm_ent.delete(0,END)
		nm_ent.focus()
		return
	elif len(name)>100:
		showwarning("!","name is too long")
		nm_ent.delete(0,END)
		nm_ent.focus()
		return

	salary=slr_ent.get()
	salary=salary.strip()
	if (salary==""):
		showwarning("!","salary cannot be empty!")
		slr_ent.delete(0,END)
		slr_ent.focus()
		return
	elif (not salary.isdigit()):
		showwarning("!","salary cannot be string")
		slr_ent.delete(0,END)
		slr_ent.focus()
		return

	con=None
	try:
		con=connect('ems.db')
		cursor=con.cursor()
		sql="insert into tb3 values('%s','%s','%s')"
		cursor.execute(sql % (id,name,salary))
		con.commit()
		showinfo("!","Thank You")
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
		id_ent.delete(0,END)
		nm_ent.delete(0,END)
		slr_ent.delete(0,END)
		id_ent.focus()

def f3():
	vw.deiconify()
	mw.withdraw()
	vw_st.delete("1.0",END)
	con=None
	try:
		con=connect("ems.db")
		cursor=con.cursor()
		sql="select * from tb3"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info+= "\n" + "ID : " + str(d[0]) + "    " + "Name : " + str(d[1]) + "    " + "Salary : " + str(d[2]) + "\n"
		vw_st.insert(INSERT,info)
	except Exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
def f4():
	mw.deiconify()
	vw.withdraw()
	
def f5():
	dltw.deiconify()
	mw.withdraw()
def f6():
	mw.deiconify()
	dltw.withdraw()	
def dltt():
	con=None
	try:
		con=connect("ems.db")
		cursor=con.cursor()
		sql="delete from tb3 where id = '%s' "
		id=dltent.get()
		id=id.strip()
		if (id=="") or (not id.isdigit()):
			showwarning("!","Invalid ID")
			dltent.delete(0,END)
			dltent.focus()
			return
		my_var=askyesno("Delete","Confirm Delete ?")
		if my_var:
			cursor.execute(sql % (id))
			if cursor.rowcount==1:
				con.commit()
				showinfo("Thank You","Record Deleted")
			else:
				showwarning("!","Record does not Exists")
	except Exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
		dltent.delete(0,END)
		dltent.focus()
def on_closing():
	if askyesno("Exit","Do You Want to Exit ?"):
		mw.destroy()
def f7():
	updw.deiconify()
	mw.withdraw()
def f8():
	mw.deiconify()
	updw.withdraw()
def updt():
	con=None
	try:
		con=connect("ems.db")
		cursor=con.cursor()
		sql="update tb3 set name='%s',salary='%s' where id='%s' "
		id2=id_ent2.get()
		id2=id2.strip()
		if (id2==""):
			showwarning("!","ID cannot be empty!")
			id_ent2.delete(0,END)
			id_ent2.focus()
			return
		elif (not id2.isdigit()):
			showwarning("!","ID cannot be string")
			id_ent2.delete(0,END)
			id_ent2.focus()
			return

		name2=nm_ent2.get()
		name2=name2.strip()
		if (name2==""):
			showwarning("!","name cannot be empty!")
			nm_ent2.delete(0,END)
			nm_ent2.focus()
			return
		elif (not name2.isalpha()):
			showwarning("!","name cannot have numbers")
			nm_ent2.delete(0,END)
			nm_ent2.focus()
			return
		elif len(name2)<=2:
			showwarning("!","name is too short")
			nm_ent2.delete(0,END)
			nm_ent2.focus()
			return
		elif len(name2)>100:
			showwarning("!","name is too long")
			nm_ent2.delete(0,END)
			nm_ent2.focus()
			return


		salary2=slr_ent2.get()
		salary2=salary2.strip()
		if (salary2==""):
			showwarning("!","salary cannot be empty!")
			slr_ent2.delete(0,END)
			slr_ent2.focus()
			return
		elif (not salary2.isdigit()):
			showwarning("!","salary cannot be string")
			slr_ent2.delete(0,END)
			slr_ent2.focus()
			return
		id_ent2.delete(0,END)
		nm_ent2.delete(0,END)
		slr_ent2.delete(0,END)
		id_ent2.focus()

		cursor.execute(sql % (name2,salary2,id2))
		if cursor.rowcount==1:
			con.commit()
			showinfo("!","Updated")
		else:
			showwarning("!","Record does not exists")
	except Exception as e:
		con.rollback()
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

	
def f9():
	con = None
	try:
		con = connect("ems.db")
		cursor = con.cursor()
		sql = 'SELECT name, salary FROM tb3 ORDER BY salary DESC LIMIT 5'
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		salary = []
		for i in data:
			name.append(i[0])
			salary.append(i[1])
		plt.figure(figsize=(8,6))
		c = ['red', 'yellow', 'black', 'blue' , 'orange' ]
		plt.rcParams.update({'text.color': "blue", 'axes.labelcolor': "green"})
		ax = plt.axes()
		ax.set_facecolor("lightblue")  # Setting the background color of the plot using facecolor
		
		
		plt.bar(name, salary ,  color= c)
		plt.xlabel("Names of Employee" , fontsize = 15)
		plt.ylabel("Salary of Employee", fontsize = 15)
		plt.title("Top 5 Highest Salaried Employee", fontsize = 15)
		#plt.grid()
		plt.show()
	except Exception as e:
        	showerror("issue ", e)
	        con.rollback()
	finally:
		if con is not None:
			con.close()
def f10():
	mw.deiconify()
	chw.withdraw()




mw=Tk()
mw.title("Employee Management System")
mw.geometry("1200x700+30+30")
f=("arial",20,"bold")

image_icon=PhotoImage(file="emp.png")
mw.iconphoto(False,image_icon)

img1=ImageTk.PhotoImage(Image.open("ems.png"))
label2=Label(mw,image=img1)
label2.place(x=520,y=0)

ems_lb=Label(mw,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),fg="black")
ems_lb.place(x=260,y=230)

addbtn=Button(mw,text="ADD",font=f,width=10,bg="light blue",command=f1)
viewbtn=Button(mw,text="VIEW",font=f,width=10,bg="light blue",command=f3)
updatebtn=Button(mw,text="UPDATE",font=f,width=10,bg="light blue",command=f7)
dltbtn=Button(mw,text="DELETE",font=f,width=10,bg="light blue",command=f5)
chrtbtn=Button(mw,text="CHARTS",font=f,width=10,bg="light blue",command=f9)
addbtn.place(x=400,y=380)
viewbtn.place(x=400,y=450)
updatebtn.place(x=680,y=380)
dltbtn.place(x=680,y=450)
chrtbtn.place(x=540,y=530)

lb=Label(mw,text="",font=("Time New Roman",17,"bold"),width=40,bg="light sky blue")
location()
lb.place(x=0,y=630)

lb2=Label(mw,text="",font=("Time New Roman",17,"bold"),width=60,bg="light sky blue")
temprature()
lb2.place(x=540,y=630)

# Add window
addw=Toplevel(mw)
addw.title("ADD EMP")
addw.geometry("1200x700+30+30")

addw.iconphoto(False,image_icon)

img2=ImageTk.PhotoImage(Image.open("bg.png"))
lb2=Label(addw,image=img2)
lb2.place(x=0,y=0,relwidth=1,relheight=1)

id_lb=Label(addw,text="Enter ID",font=f,width=15,bg="cornflower blue",fg="white")
id_ent=Entry(addw,font=f,width=25)
id_lb.pack(pady=20)
id_ent.pack(pady=20)

nm_lb=Label(addw,text="Enter Name",font=f,width=15,bg="cornflower blue",fg="white")
nm_ent=Entry(addw,font=f,width=25)
nm_lb.pack(pady=20)
nm_ent.pack(pady=20)

slr_lb=Label(addw,text="Enter Salary",font=f,width=15,bg="cornflower blue",fg="white")
slr_ent=Entry(addw,font=f,width=25)
slr_lb.pack(pady=20)
slr_ent.pack(pady=20)

sv=Button(addw,text="SAVE",width=10,font=f,bg="light green",command=add)
sv.pack(pady=20)

bck=Button(addw,text="BACK",font=f,width=10,command=f2,bg="light grey")
bck.pack(pady=20)
addw.withdraw()

# view window
vw=Toplevel(mw)
vw.title("View EMP")
vw.geometry("1200x700+30+30")

vw.iconphoto(False,image_icon)

img3=ImageTk.PhotoImage(Image.open("bg.png"))
lb3=Label(vw,image=img3)
lb3.place(x=0,y=0,relwidth=1,relheight=1)

vw_st=ScrolledText(vw,font=f,width=50,height=12)
vw_st.place(x=250,y=150)

vwbck_btn=Button(vw,text="BACK",font=f,command=f4,width=20)
vwbck_btn.place(x=430,y=570)

vw.withdraw()

# update window
updw=Toplevel(mw)
updw.title("Update EMP")
updw.geometry("1200x700+30+30")

updw.iconphoto(False,image_icon)

img5=ImageTk.PhotoImage(Image.open("bg.png"))
lb5=Label(updw,image=img5)
lb5.place(x=0,y=0,relwidth=1,relheight=1)

id_lb=Label(updw,text="Enter ID to update",font=f,bg="light blue",width=30)
id_lb.place(x=370,y=100)

id_ent2=Entry(updw,font=f)
id_ent2.place(x=480,y=150)

nm_lb=Label(updw,text="Enter name",font=f,bg="light blue",width=30)
nm_lb.place(x=370,y=250)

nm_ent2=Entry(updw,font=f)
nm_ent2.place(x=480,y=300)

slr_lb=Label(updw,text="Enter salary",font=f,bg="light blue",width=30)
slr_lb.place(x=370,y=400)

slr_ent2=Entry(updw,font=f)
slr_ent2.place(x=480,y=450)

upd=Button(updw,text="UPDATE",font=f,bg="light green",command=updt)
upd.place(x=570,y=500)

upd_bck=Button(updw,text="BACK",font=f,bg="light grey",command=f8)
upd_bck.place(x=590,y=600)
updw.withdraw()

# delete window
dltw=Toplevel(mw)
dltw.title("Delete EMP")
dltw.geometry("1200x700+30+30")

dltw.iconphoto(False,image_icon)

img4=ImageTk.PhotoImage(Image.open("bg.png"))
lb4=Label(dltw,image=img4)
lb4.place(x=0,y=0,relwidth=1,relheight=1)

dltlb=Label(dltw,text="Enter ID to be Deleted",font=f,bg="light blue",width=30)
dltlb.place(x=350,y=100)

dltent=Entry(dltw,font=f)
dltent.place(x=450,y=200)

dltbtn=Button(dltw,text="DELETE",font=f,bg="light blue",command=dltt)
dltbtn.place(x=540,y=330)

dltbck_btn=Button(dltw,text="BACK",font=f,width=20,bg="light grey",command=f6)
dltbck_btn.place(x=430,y=550)
dltw.withdraw()




def on_closing():
	if askyesno("Exit","Do You Want To Exit ? "):
		mw.destroy()

dltw.protocol("WM_DELETE_WINDOW",on_closing)
updw.protocol("WM_DELETE_WINDOW",on_closing)
vw.protocol("WM_DELETE_WINDOW",on_closing)
addw.protocol("WM_DELETE_WINDOW",on_closing)
mw.protocol("WM_DELETE_WINDOW",on_closing)
mw.mainloop()
from tkinter import *
from tkinter import messagebox
import sqlite3
import uuid
from calendar import *

root = Tk()
root.config(bg='#D0ECE7')
root.geometry("940x580+300+100")
root.resizable(False, False)
root.title('Welcome')


photo=PhotoImage(file='rrulogo.png')
master=Label(image=photo)
master.pack()

conn = sqlite3.connect('Main.db')
c = conn.cursor()

def About():
    about = Tk()
    about.geometry("900x100+220+300")
    about.title('About')
    about.resizable(False, False)
    w = Label(about, text='\n This is a online outpass system implemented using tkinter. \n help for online outpass \n',font=('Bookman Old Style', 15, 'bold'),fg='#0F5347')
    w.pack()
    about.mainloop()
def Team():
    team = Tk()
    team.geometry("300x180+550+250")
    team.title('Team')
    team.resizable(False, False)
    w = Label(team, text='\nmihir\nviveksir\njay patel(3rd year)\nand smit patel (3rd year)\n ',font=('Bookman Old Style', 15, 'bold'),fg='#0F5347')
    w.pack()
    team.mainloop()
def Help():
    help = Tk()
    help.geometry("700x200+380+300")
    help.title('Help..')
    help.resizable(False, False)
    w = Label(help,text='\n Click on SIGNUP if you dont have your userid.\nClick on LOGIN to fill the outpass details. \n (signup requirment) \n please enter user id number forme (warden office give you)\n password is any character \n ',font=('Bookman Old Style', 15, 'bold'),fg='#0F5347')
    w.pack()
    help.mainloop()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='MENU', menu=filemenu)
filemenu.add_command(label='About',command=About)
filemenu.add_command(label='Team',command=Team)
filemenu.add_separator()
filemenu.add_command(label='Help',command=Help)
helpmenu = Menu(menu)

s_name = StringVar()
u_sn = IntVar()
pass_word = StringVar()
def signup():
    s = Tk()
    s.config(bg='#D0ECE7')
    s.geometry("550x400+400+170")
    s.resizable(False, False)
    s.title('Sign_up')


    #create database and insert values for signup
    def insert():
        conn = sqlite3.connect('Main.db')
        # c = conn.cursor()
        sname = e1.get()
        usn = e2.get()
        password = e3.get()
        # c.execute('CREATE TABLE IF NOT EXISTS details (s_name Text NOT NULL, u_sn NUMBER PRIMARY KEY, pass_word TEXT NOT NULL)')
        # c.execute("insert into details values('mohit',6,'gh')")
        conn.execute('INSERT INTO details (s_name, u_sn, pass_word)  VALUES (?,?,?)', (sname, usn, password,))
        conn.commit()
        conn.close()

    l = Label(s, text='       SIGNUP          ', bg='#083C41', fg='white', font=('Comic Sans MS', 40, 'bold')).place(
        x=0,
        y=0)
    Label(s, text='NAME :', bg='#D0ECE7', font=('Bookman Old Style', 15, 'bold')).place(x=60, y=140)
    Label(s, text='USERID :', bg='#D0ECE7', font=('Bookman Old Style', 15, 'bold')).place(x=60, y=190)
    Label(s, text='PASSWORD :', bg='#D0ECE7', font=('Bookman Old Style', 15, 'bold')).place(x=60, y=240)
    e1 = Entry(s, width=20, font=('Verdana', 15))
    e1.place(x=210, y=140)
    e2 = Entry(s, width=20, font=('Verdana', 15))
    e2.place(x=210, y=190)
    e3 = Entry(s, width=20, font=('Verdana', 15))
    e3.place(x=210, y=240)
    Button(s, text='SIGNUP', width=10, command=insert, font=('Bookman Old Style', 15)).place(x=230, y=290)

    # Button(s, text='show', width=10, command=query, font=('Bookman Old Style', 15)).place(x=230, y=360)

    s.mainloop()



Label(root, text=' WELCOME TO ONLINE OUTPASS IN RRU ', bg='#083C41', fg='white', font=('Comic Sans MS', 20, 'bold')).place(x=175, y=0)
Label(root,text='USERID :', bg='#7F8C8D' ,font=('Bookman Old Style',15,'bold')).place(x=280,y=250)
Label(root,text='PASSWORD :',bg='#7F8C8D',font=('Bookman Old Style',15,'bold')).place(x=280,y=290)
e1=Entry(root, width=20,font=('Verdana', 15))
e1.place(x=415,y=250)
e2=Entry(root,show='*',width=20,font=('Verdana', 15))
e2.place(x=415,y=290)
Button(root,text='SIGNUP',width=10,command=signup,font=('Bookman Old Style', 15)).place(x=500,y=330)
wname = e1.get()
passw = e2.get()
c.execute('CREATE TABLE IF NOT EXISTS warden (s_name Text NOT NULL,pass_word TEXT NOT NULL)')
#c.execute("insert into warden values('WARDEN','warden')")

def login():
    f = Tk()
    f.config(bg='#D0ECE7')
    f.geometry("560x640+400+20")
    f.resizable(False, False)
    f.title('outpass')

    conn = sqlite3.connect('Main.db')
    # c = conn.cursor()
    Label(f, text='       DETAILS         ', bg='#083C41', fg='white',font=('Comic Sans MS', 40, 'bold')).place(x=0, y=0)
    Label(f, text='NAME :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=110)
    Label(f, text='USN :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=150)
    Label(f, text='ROOM NO. :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=190)
    Label(f, text='YEAR :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=230)
    Label(f, text='PLACE :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=270)
    Label(f, text='PHONE NO. :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=310)
    Label(f, text='PURPOSE :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=350)
    Label(f, text='DATE TO :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=390)
    Label(f, text='DATE FROM :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=430)
    Label(f, text='TIME TO :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=470)
    Label(f, text='TIME FROM :', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=100, y=510)

    sname = e1.get()
    e = Entry(f, width=20, font=('Verdana', 10))
    e.insert(0,sname)
    e.config(state=DISABLED)
    e.place(x=270, y=110)
    e2 = Entry(f, width=20, font=('Verdana', 10))
    e2.place(x=270, y=150)
    e3 = Entry(f, width=20, font=('Verdana', 10))
    e3.place(x=270, y=190)
    e5 = Entry(f, width=20, font=('Verdana', 10))
    e5.place(x=270, y=270)
    e6 = Entry(f, width=20, font=('Verdana', 10))
    e6.place(x=270, y=310)
    e7 = Entry(f, width=20, font=('Verdana', 10))
    e7.place(x=270, y=350)
    e4 = Spinbox(f, from_=1, to=4, width=5)
    e4.place(x=270, y=230)
    e8 = Entry(f, width=20, font=('Verdana', 10))
    e8.place(x=270, y=390)
    def cal_func():
      def calval():
        e8.insert(0, cal.get_date())
      top = Toplevel(f)
      top.title('Date_to')
      x = root.winfo_x()
      y = root.winfo_y()
      top.geometry("+%d+%d" % (x + 150, y + 200))
      cal = Calendar(top, font="Arial 14", selectmode="day")
      cal.pack(fill="both", expand=True)
      btn3 = Button(top, text="click Me", command=calval)
      btn3.pack()
    
    months = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
    Sb1 = Spinbox(f, from_=1, to=31, width=5)
    Sb2 = Spinbox(f, values=months, width=5)
    Sb3 = Spinbox(f, from_=2022, to=2030, width=5)
    Sb1.place(x=270, y=390)
    Sb2.place(x=330, y=390)
    Sb3.place(x=390, y=390)
    e9 = Entry(f, width=20, font=('Verdana', 10))
    e9.place(x=270, y=430)
    def cal_func():
      def calval():
        e9.insert(0, cal.get_date())
      top = Toplevel(f)
      top.title('Date_from')
      x = root.winfo_x()
      y = root.winfo_y()
      top.geometry("+%d+%d" % (x + 150, y + 200))
      cal = Calendar(top, font="Arial 14", selectmode="day")
      cal.pack(fill="both", expand=True)
      btn3 = Button(top, text="click Me", command=calval)
      btn3.pack()
      top.mainloop()
    # btn1 = Button(f, text="Calendar", command=cal_func)
    # btn1.place(x=440, y=430)
    Sb4 = Spinbox(f, from_=1, to=31, width=5)
    Sb5 = Spinbox(f, values=months, width=5)
    Sb6 = Spinbox(f, from_=2022, to=2030, width=5)
    Sb4.place(x=270, y=430)
    Sb5.place(x=330, y=430)
    Sb6.place(x=390, y=430)

    time = ('AM', 'PM')
    Label(f, text=': ', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=315, y=465)
    T1 = Spinbox(f, from_=1, to=12, width=5)
    T3 = Spinbox(f, values=time, width=5)
    T2 = Spinbox(f, from_=00, to=60, width=5)
    T1.place(x=270, y=470)
    T3.place(x=390, y=470)
    T2.place(x=330, y=470)
    Label(f, text=': ', bg='#D0ECE7', font=('Bookman Old Style', 14, 'bold')).place(x=315, y=505)
    T4 = Spinbox(f, from_=1, to=12, width=5)
    T6 = Spinbox(f, values=time, width=5)
    T5 = Spinbox(f, from_=00, to=60, width=5)
    T4.place(x=270, y=510)
    T6.place(x=390, y=510)
    T5.place(x=330, y=510)
    Button(f, text='SUBMIT', width=10, font=('Bookman Old Style', 14)).place(x=210, y=560)

    def inserts():
        conn = sqlite3.connect('Main.db')
        c = conn.cursor()
        # sname = e1.get()
        # usn = e2.get()
        i_d = e2.get()
        roomno = e3.get()
        year = e4.get()
        pl_ace = e5.get()
        phoneno = e6.get()
        pur_pose = e7.get()
        date_to = Sb1.get() + Sb2.get() + Sb3.get()
        date_from = Sb4.get() + Sb5.get() + Sb6.get()
        time_to = T1.get() + T2.get() + T3.get()
        time_from = T4.get() + T5.get() + T6.get()
        # c.execute('CREATE TABLE s_details(u_sn NUMBER, course real, y_ear NUMBER, place TEXT,phone NUMBER,purpose TEXT,d_to NUMBER,d_from NUMBER,t_to TEXT,t_from TEXT)')
        c.execute('INSERT INTO s_details (u_sn,room,y_ear,place,phone,purpose,d_to,d_from,t_to,t_from)  VALUES (?,?,?,?,?,?,?,?,?,?)',(i_d,roomno, year, pl_ace, phoneno, pur_pose, date_to, date_from, time_to, time_from))
        conn.commit()
        conn.close()
    Button(f, text='SUBMIT',command=inserts, width=10, font=('Bookman Old Style', 14)).place(x=210, y=560)
    f.mainloop()
def warden():

    m = Tk()
    m.config(bg='#D0ECE7')
    m.geometry("940x580+200+70")
    m.resizable(False, False)
    frame1 = Frame(m)
    frame1.grid(row=0, column=0)
    frame2 = Frame(m)
    frame2.grid(row=1, column=0)
    s = Scrollbar(frame2, orient='vertical')
    s.pack(side=RIGHT, fill=Y)
    canvas1 = Canvas(frame1, width=940, height=75)
    canvas1.pack()
    Label(canvas1, text='              WELCOME               ', bg='#083C41', fg='white',
          font=('Comic Sans MS', 40, 'bold')).place(x=0, y=0)
    canvas2 = Canvas(frame2, width=920, height=495, bg='#D0ECE7')
    canvas2.pack()

    m.mainloop()
def error():
    messagebox.askretrycancel("invalid", "🙁try again?🙁")


def query():

    wname = e1.get()
    passw = e2.get()
    
    cursor = conn.cursor()
    cursor.execute("SELECT s_name, u_sn, pass_word from details")

    war = cursor.fetchall()
    user_dict={}

    for value in war:
        user_dict[value[1]] = value[2]

    # print(user_dict)
    # print(wname, passw)
    # print(user_dict[wname], passw)
    try:
        if user_dict[int(wname)] == passw:
            print('correct')
            login()
    except:
        print('wrong')
        error()



Button(root,text='LOGIN',width=10,command=query,font=('Bookman Old Style', 15)).place(x=320,y=330)

conn.commit()
root.mainloop()


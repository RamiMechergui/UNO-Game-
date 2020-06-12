from tkinter import *
from tkinter import messagebox
from datetime import *
#********************************************Playing***Uno**Game********************************************************
class UNO :
    def __init__(self,Mainwindow,ls):
        self.WelcomeImage = PhotoImage(file='C:\\Users\\stree\\OneDrive\\Bureau\\UNO GAME\\Header.png')
        self.Mainwindow=Mainwindow
        self.ls=ls
        for i in range(0,len(self.ls)):
            self.C=Crea(self.Mainwindow,self.ls[i],i)
        self.Bt2=Button(self.Mainwindow,text='Quit UNO Game',font=('arial',12),bg='black',fg='white',
                        activebackground='blue',activeforeground='black',command=QUITMAINWINDOW)
        self.Bt2.place(x=320,y=520)
class Crea :
    def __init__(self,Mainwindow,Name,Number):
        self.Number=Number
        i = 0
        self.z= 0
        self.w= 0
        if self.Number == i:
           pass
        elif self.Number == 1 :
            self.z=250
        elif self.Number == 2 :
            self.w=250
        elif self.Number == 3 :
            self.z=250
            self.w=250
        self.Name=Name
        self.var=IntVar()
        self.var2=IntVar()
        self.LSF = LabelFrame(Mainwindow, height=250, width=250,
                              bg='powder blue',).pack(fill='both',expand='yes')
        self.LbF = LabelFrame(self.LSF, text=self.Name, height=250, width=250,
                              bg='powder blue',font=('arial', 16, 'bold')).place(x=i + self.z, y=i + self.w)
        self.LB=Label(self.LbF,text='Current score',bg='orange',
                              font=('arial',16)).place(x=10+self.z,y=50+self.w)
        self.En=Entry(self.LbF,textvariable=self.var,state='readonly',width=6,
                             font=('arial',16),justify='center').place(x=self.z+160,y=50+self.w)
        self.LB2=Label(self.LbF,text='Score to add',bg='yellow',
                               font=('arial',16)).place(x=10+self.z,y=110+self.w)
        self.En2=Entry(self.LbF,textvariable=self.var2,width=6,
                               font=('arial',16),justify='center').place(x=160+self.z,y=110+self.w)
        self.BtAdd=Button(self.LbF,activebackground='red',font=('arial', 16, 'bold'),
                                  text='Add',
                                  command = lambda : self.fn(self.var.get(),self.var2.get())).place(x=180+self.z,y=150+self.w)

    def fn(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.x = self.n1 + self.n2
        self.var.set(self.x)
        self.var2.set(0)
        if self.x >= 500 :
            self.LB2 = Label(self.LbF, text=f"{self.Name } Game Over " ,padx=35,pady=115,
                                       bg='red', font=('arial', 16)).place(x=0 + self.z, y=0 + self.w)


class aff():
    def __init__(self, Mainwindow, ls):
        self.Mainwindow = Mainwindow
        self.ls = ls
        self.txt = ''
        self.Fm = LabelFrame(self.Mainwindow, text='The List of Players is : ',
                             bg='powder blue',
                             fg='Purple',
                             font=('arial', 16, 'bold'), padx=40, pady=40)

        self.Fm.place(relx=0.21, rely=0.3)
        x=0
        while x < len(self.ls):
              self.txt=self.txt +self.ls[x]+'\n'
              x=x+1
        Lb = Label(self.Fm, text=self.txt, bg='powder blue', font=('arial', 12, 'bold')).pack()
        bt = Button(self.Fm, text='Valider', activebackground='red',
                    command=lambda:self.toward(self.Mainwindow,self.ls)).place(relx=0.7, rely=1.1)
        bt2 = Button(self.Fm, text='Retour', activebackground='red',
                     command = lambda: self.fn(self.Mainwindow, self.WelcomeImage) ).place(relx=0.1, rely=1.1)

    def fn(self, Mainwindow, WelcomeImage):
        self.Fm.forget()
        k = WelcomePg(self.Mainwindow, self.WelcomeImage)

    def toward(self,Mainwindow,ls):
        self.Fm.pack_forget()
        C=UNO(self.Mainwindow,self.ls)
#**********************************Getting***Players**Names**************************************************************
class GetPlayersNames:

    def __init__(self,Mainwindow,WelcomeImage,x):
        self.Mainwindow=Mainwindow
        self.E = 0
        self.Names=[]
        self.WelcomeImage = WelcomeImage
        self.var = StringVar()
        self.x=x
        self.var2 = StringVar()
        self.var2.set('Put the name of the first Player :')
        self.WelcomeFrame = LabelFrame(self.Mainwindow,
                                  text='You are welcome',
                                  bg='powder blue',
                                  fg='Purple',
                                 height=200,
                                  width=650,
                                  font=('arial', 16, 'bold'),
                                  bd=3)
        self.WelcomeFrame.pack(pady=50)
        Welcomebackground = Label(self.WelcomeFrame,
                                  image=self.WelcomeImage).pack()
        self.WelcomeMessage = Label(self.WelcomeFrame,
                                    textvariable=self.var2,
                                    bg='powder blue').pack(padx=5, pady=9)
        self.WelcomeEntry = Entry(self.WelcomeFrame,
                             bg='white',
                             textvariable=self.var,
                             justify='center').pack()
        WelcomeButton = Button(self.WelcomeFrame,
                               text='Next',
                               padx=10,
                               pady=5,
                               activebackground='red',
                               command=lambda:self.click(self.var.get())).pack(side='right',padx=60,pady=10)
        QuitButton = Button(self.WelcomeFrame,
                             text='Quit',
                             padx=10,
                             pady=5,
                            activebackground='red',
                            command = lambda: Mainwindow.destroy() ).place(x=60,y=284)
        QuitButton = Button(self.WelcomeFrame,
                            text='Quit',
                            padx=10,
                            pady=5,
                            activebackground='red',
                            command=lambda: self.Quit()).place(x=60, y=284)

    def Quit(self):
            if messagebox.askokcancel("Quit", "Did You Want to quit UNO Game"):
                self.Mainwindow.destroy()
    def click(self,f):
        OrderLs=['second','third','fourth','fifth','sixth','seventh']
        self.x=self.x -1
        if f.upper() in self.Names :
            Welcomewarning = messagebox.showerror('Error', 'Please enter a new name')
            self.var.set('')
        elif f.isalpha() and self.x > 0 :
            self.var2.set(f'Put the name of the {OrderLs[self.E]} player')
            self.E=self.E+1
            self.Names.append(f)
            self.var.set('')
        elif f.isalpha() != True :
            Welcomewarning = messagebox.showerror('Error', 'Please enter an alphabetical name without space ')
            self.var.set('')
        else:
            self.Names.append(f)
            self.WelcomeFrame.forget()
            K=self.Callthelist(self.Mainwindow,self.Names)

    def Callthelist(self,Mainwindow,ls):
        B=aff(self.Mainwindow,self.Names)
#***************************************Generating**Welcome Page********************************************************
class WelcomePg :
    def __init__(self,Mainwindow,WelcomeImage):
        self.Mainwindow=Mainwindow
        self.WelcomeImage = WelcomeImage
        self.var = IntVar()
        self.WelcomeFrame = LabelFrame(self.Mainwindow,
                                  text='You are welcome',
                                  bg='powder blue',
                                  fg='Purple',
                                  height=200,
                                  width=650,
                                  font=('arial', 16, 'bold'),
                                  bd=3)
        self.WelcomeFrame.pack(pady=50)
        Welcomebackground = Label(self.WelcomeFrame,
                                  image=self.WelcomeImage).pack()
        self.WelcomeMessage = Label(self.WelcomeFrame,
                               text="Put the number of Players",
                               bg='powder blue').pack(padx=5, pady=9)
        self.WelcomeEntry = Entry(self.WelcomeFrame,
                             bg='white',
                             textvariable=self.var,
                             justify='center').pack()
        self.WelcomeButton = Button(self.WelcomeFrame,
                               text='Next',
                               padx=10,
                               pady=5,
                               activebackground='red',
                               command=lambda:self.click(self.var.get())).pack(side='right',padx=60,pady=10)
        QuitButton = Button(self.WelcomeFrame,
                            text='Quit',
                            padx=10,
                            pady=5,
                            activebackground='red',
                            command = lambda: self.Quit()).place(x=60,y=284)

    def Quit(self):
        if messagebox.askokcancel("Quit", "Did You Want to quit UNO Game"):
            self.Mainwindow.destroy()

    def click(self, x):
        if x not in [2, 3, 4] :
            Welcomewarning = messagebox.showerror('Error', 'Please enter a number of players between 2 and 4')
        else :
            self.WelcomeFrame.forget()
            f=self.CallMe(self.Mainwindow,self.WelcomeImage,x)
    def CallMe(self,Mainwindow,WelcomeImage,x):
        K=GetPlayersNames(Mainwindow,WelcomeImage,x)
#*******************************************************The Main Program************************************************
MainWindow =Tk()
var=StringVar()
var.set(datetime.now())
MainWindow.geometry('510x550+900+20')
MainWindow.config(bg='powder blue')
MainWindow.resizable(False,False)
MainWindow.title('UnoGame')
MainWindow.iconbitmap('C:\\Users\\stree\\OneDrive\\Bureau\\UNO GAME\\Uno Game.ico')
logo = PhotoImage(file='C:\\Users\\stree\\OneDrive\\Bureau\\UNO GAME\\Dev.png')
photo=logo.subsample(3,3)
LB=Label(MainWindow,image = photo,width=120,height=150).place(x=0,y=297)
LB2=Label(MainWindow,text='Developped by \n Rami Mechergui \n For Business inquiries \n Street.cherk@gmail.com \n 54811289').place(x=0,y=470)
WelcomeImage=PhotoImage(file='C:\\Users\\stree\\OneDrive\\Bureau\\UNO GAME\\Header.png')
A = WelcomePg(MainWindow, WelcomeImage)
B=Entry(MainWindow,textvariable=var,state='readonly',font=('arial',15,'bold'),width=17).pack(side='bottom')
def QUITMAINWINDOW():
    if messagebox.askokcancel("Quit","Did You Want to quit UNO Game"):
        MainWindow.destroy()
MainWindow.protocol("WM_DELETE_WINDOW",QUITMAINWINDOW)
MainWindow.mainloop()
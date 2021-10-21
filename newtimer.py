import tkinter as tk
import datetime
import time as T
class NewWindow():
    def __init__(self,root,mytimer,mytree):
        self.mytimer = mytimer
        self.mytree = mytree
        self.newWin = tk.Toplevel(root)
        self.newWin.title("New Timer")
        self.newWin.geometry("500x300+850+400")
      #  self.newWin.resizable(width=0, height=0)
        self.newWin.config(bg="black")
        self.e_new_timer = tk.Entry(self.newWin, font=("Dejavu", 20, "bold"))
        self.e_new_timer.insert(tk.END, "name")
        tk.Button(self.newWin,text = "create",bg = "#faea01", fg = "black",highlightbackground= "black",activebackground = "blue",font = ("Dejavu",17,"bold"),command = lambda: self.Create(None)).grid(row = 0,column = 1)

        self.fill_circle = tk.PhotoImage(file= "./images/fill_circle.png")
        self.empty_circle = tk.PhotoImage(file = "./images/empty_circle.png")
        self.add  = tk.PhotoImage(file="./images/add.png")
        self.sub = tk.PhotoImage(file="./images/rest.png")

        self.rb_str = tk.StringVar()

        self.rb1 = tk.Button(self.newWin,text = "F",highlightbackground= "black",bd = 0,image=self.empty_circle,bg = "black",command = lambda:self.RadioButton(0))
        self.rb2 = tk.Button(self.newWin,text = "F",highlightbackground= "black",bd = 0,image=self.empty_circle,bg = "black",command = lambda:self.RadioButton(1))
        self.lbl1 = tk.Label(self.newWin,text = "Timerkeeper",bg = "black",fg = "#faea01",font = ("Dejavu",18,"bold"))
        self.lbl2 = tk.Label(self.newWin,text = "Timer",bg = "black",fg = "#faea01",font = ("Dejavu",18,"bold"))

        tk.Label(self.newWin, text="Press Enter*", fg="yellow", bg="black").grid(row=1,sticky=tk.W)

        self.frame1 = tk.Frame(self.newWin,bg = "black",bd = 10,highlightbackground="#faea01",heigh = 150,width = 300,relief = tk.SUNKEN)
        self.frame2 = tk.Frame(self.newWin, bg="black", bd=10, highlightbackground="#faea01", heigh=150, width=300,relief=tk.SUNKEN)
        self.timer_frame = tk.Frame(self.newWin, bg="black")

        self.CheckVar1 = tk.IntVar()
        self.CheckVar2 = tk.IntVar()
        self.CheckVar3 = tk.IntVar()
        self.CheckVar4 = tk.IntVar()
        self.SVT = []
        self.e_new_timer.grid(row=0, column=0)
        self.rb1.grid(row = 2,pady = 20,column = 0,sticky=tk.W)
        self.rb2.grid(row = 2,pady = 15,column = 0,padx = 100,sticky=tk.E)
        self.lbl1.place(x= 65,y=80)
        self.lbl2.place(x= 310, y=80)

        self.newWin.bind("<Return>", self.Create)
    def RadioButton(self,txt_btn):
        if txt_btn == 0:
            if self.rb1["text"] == "F":
                self.rb1["text"] = "T"
                self.rb1["image"] = self.fill_circle
                self.rb2["text"] = "F"
                self.rb2["image"] = self.empty_circle
                self.SetTimerkeeper()
        if txt_btn == 1:
            if self.rb2["text"] == "F":
                self.rb2["text"] = "T"
                self.rb2["image"] = self.fill_circle
                self.rb1["text"] = "F"
                self.rb1["image"] = self.empty_circle
                self.SetTimer()
    def SetTimer(self):
        self.frame2.grid_forget()

        self.select1 = tk.Checkbutton(self.frame1, text="All time count",bg = "black",fg = "#faea01",highlightbackground= "black",selectcolor="black",variable = self.CheckVar2,font = ("Dejavu",15))
        self.select2 = tk.Checkbutton(self.frame1, text="Alarm", bg="black", fg="#faea01", selectcolor="black",highlightbackground= "black",variable=self.CheckVar3, font=("Dejavu", 15))
        self.select3 = tk.Checkbutton(self.frame1, text="reset at the end", bg="black", fg="#faea01", selectcolor="black", highlightbackground="black", variable=self.CheckVar4, font=("Dejavu", 15))
        self.frame1.grid(row=3, column=0, sticky=tk.NW)
        self.frame1.grid(row=3, column=0, sticky=tk.NW)
        self.select1.grid(row=0,sticky = tk.W)
        self.select2.grid(row=1,sticky = tk.W)
        self.select3.grid(row=2, sticky=tk.W)
        self.TimerModify()
    def SetTimerkeeper(self):
        self.frame1.grid_forget()
        self.timer_frame.grid_forget()
        self.select1 = tk.Checkbutton(self.frame2,text = "All time count",highlightbackground= "black",bg = "black",fg = "#faea01",selectcolor="black",variable = self.CheckVar1,font = ("Dejavu",15))
        self.frame2.grid(row=3, column=0, sticky=tk.NW)
        self.select1.grid(row=0,column = 0,sticky = tk.W)
    def TimerModify(self):
        self.timer_frame.grid(row = 3,columnspan = 3,sticky = tk.E)
        def addtime(n):
            if n >= 10: svt = self.SVT[n-10]
            else: svt = self.SVT[n]
            if n >= 10: txt = int(svt.get())+10
            else: txt = int(svt.get())+1
            if txt > 59 and n != 0: txt = 0
            txt = str(txt)
            if len(txt)<2:
                svt.set("0"+txt)
            else: svt.set(txt)
        def subtime(n):
            if n >= 10: svt = self.SVT[n-10]
            else: svt = self.SVT[n]
            if n >= 10: txt = int(svt.get())-10
            else: txt = int(svt.get())-1
            if txt <0: txt = 59
            txt = str(txt)
            if len(txt)<2:
                svt.set("0"+txt)
            else: svt.set(txt)

        svt1 = tk.StringVar(value= "00")
        svt2 = tk.StringVar(value= "00")
        svt3 = tk.StringVar(value= "00")

        self.SVT = [svt1,svt2,svt3] #SVT = String Var Text

        groove1 = tk.Label(self.timer_frame, textvariable = svt1,width=2)
        groove2 = tk.Label(self.timer_frame, textvariable = svt2,width=2)
        groove3 = tk.Label(self.timer_frame, textvariable = svt3,width=2)
        groove1.config(bg="black", fg="#faea01", bd = 5,font=("ds-digital", 55, "bold"))
        groove2.config(bg="black", fg="#faea01", bd = 5,font=("ds-digital", 55, "bold"))
        groove3.config(bg="black", fg="#faea01", bd = 5,font=("ds-digital", 55, "bold"))
        # this buttons add 1 to the clock
        add0 = tk.Button(self.timer_frame, image=self.add, bg="black", highlightbackground="black",command=lambda: addtime(0))
        add1 = tk.Button(self.timer_frame, image=self.add, bg="black", highlightbackground="black",command=lambda: addtime(1))
        add2 = tk.Button(self.timer_frame, image=self.add, bg="black", highlightbackground="black",command=lambda: addtime(2))
        #this buttons add 10 to the clock
        add10 = tk.Button(self.timer_frame, image=self.add, bg="black", highlightbackground="black",command=lambda: addtime(10))
        add11 = tk.Button(self.timer_frame, image=self.add, bg="black", highlightbackground="black",command=lambda: addtime(11))
        add12 = tk.Button(self.timer_frame, image=self.add, bg="black", highlightbackground="black",command=lambda: addtime(12))
        # this buttons substrack 1 to the clock
        sub0 = tk.Button(self.timer_frame, image=self.sub, bg="black", highlightbackground="black",command=lambda: subtime(0))
        sub1 = tk.Button(self.timer_frame, image=self.sub, bg="black", highlightbackground="black",command=lambda: subtime(1))
        sub2 = tk.Button(self.timer_frame, image=self.sub, bg="black", highlightbackground="black",command=lambda: subtime(2))
        # this buttons substrack 10 to the clock
        sub10 = tk.Button(self.timer_frame, image=self.sub, bg="black", highlightbackground="black",command=lambda: subtime(10))
        sub11 = tk.Button(self.timer_frame, image=self.sub, bg="black", highlightbackground="black",command=lambda: subtime(11))
        sub12 = tk.Button(self.timer_frame, image=self.sub, bg="black", highlightbackground="black",command=lambda: subtime(12))

        add10.grid(row=0, column=2,padx = 18,sticky = tk.W)
        add11.grid(row=0, column=1,padx = 18,sticky = tk.W)
        add12.grid(row=0, column=0,padx = 18,sticky = tk.W)

        add0.grid(row=0, column=2,padx = 18,sticky = tk.E)
        add1.grid(row=0, column=1,padx = 18,sticky = tk.E)
        add2.grid(row=0, column=0,padx = 18,sticky = tk.E)

        sub10.grid(row=2, column=2,padx = 18,sticky = tk.W)
        sub11.grid(row=2, column=1,padx = 18,sticky = tk.W)
        sub12.grid(row=2, column=0,padx = 18,sticky = tk.W)

        sub0.grid(row=2, column=2,padx = 18,sticky = tk.E)
        sub1.grid(row=2, column=1,padx = 18,sticky = tk.E)
        sub2.grid(row=2, column=0,padx = 18,sticky = tk.E)

        groove1.grid(row=1, column=2)
        groove2.grid(row=1, column=1)
        groove3.grid(row=1, column=0)
    def Create(self,event):
        time = [0,0,0]
        all_time = 0
        reset = "False"
        alarm = "False"
        if self.rb1["text"] == "T":
            all = str(bool(self.CheckVar1.get()))
            if all == "True": all_time = T.time()
            keeper = "True"
            alarm = "False"
        elif self.rb2["text"] == "T":
            all = str(bool(self.CheckVar2.get()))
            if all == "True":  all_time = T.time()
            keeper = "False"
            time = [ int(i.get()) for i in self.SVT]
            alarm = str(bool(self.CheckVar3.get()))
            reset = str(bool(self.CheckVar4.get()))
        row = {"name": self.e_new_timer.get(), "s": time[0], "m": time[1], "h": time[2], "date": datetime.datetime.now().strftime("%d/%m/%Y"),"all":all,"all_time": all_time,"keeper":keeper,"alarm":alarm,"reset": reset, "S":time[0],"M":time[1],"H":time[2]}
        self.mytimer.AddButton(self.e_new_timer.get(),row)
        self.mytree.reset_tree()
        self.newWin.destroy()


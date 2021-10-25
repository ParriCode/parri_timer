#! /usr/bin/env python
import tkinter as tk
from tkinter import messagebox
import time
import csv
import newtimer as NT
from playsound import playsound
class Data:
    def __init__(self):
        self.fieldnames = ["name", "s", "m", "h", "date","all","all_time","keeper","alarm","reset","S","M","H"]
        self.data = {}
        with open("data.csv", "r") as csvreader:
            csvreader = csv.DictReader(csvreader)
            for row in csvreader:
                self.data.update({row["name"]: row})
    def NewData(self,name,row):
        self.data[name] = row
    def Save(self,name,l):
        self.data[name]["s"] = l[0]
        self.data[name]["m"] = l[1]
        self.data[name]["h"] = l[2]
    def Close(self):
        with open("data.csv", "w") as csvwriter:
            csvwriter = csv.DictWriter(csvwriter,fieldnames=self.fieldnames)
            csvwriter.writeheader()
            for i in self.data: csvwriter.writerow(self.data[i])
        quit()
    def Delete(self,name):
        self.data.pop(name)
class TimerButtons():
    def __init__(self):
        self.timer = Timer()
        self.timerbutton = {}
        self.textbutton = {}
        self.CreateButton()
        self.lbl = tk.Label(frame, textvariable= "0:0:0",bg = "black",fg = "yellow",font=("ds-digital",200,"bold"))
        self.lbl1 = tk.Label(root, text="", bg="black", fg="yellow", font=("Arial", 25, "bold"))
        self.lbl2 = tk.Label(root, text="", bg="black", fg="yellow", font=("Arial", 25, "bold"))
        self.lbl3 = tk.Label(root, text="", bg="black", fg="yellow", font=("Arial", 25, "bold"))
        self.lbl4 = tk.Label(root, text="", bg="black", fg="yellow", font=("Arial", 25, "bold"))
        self.lbl5 = tk.Label(root, text="", bg="black", fg="yellow", font=("Arial", 25, "bold"))
        self.lbl6 = tk.Label(root, text="", bg="black", fg="yellow", font=("Arial", 25, "bold"))
        self.lbl.place(x = 50,y=50)
        self.lbl1.place(x=500, y=660)
        self.lbl2.place(x=500, y=710)
        self.lbl3.place(x=500, y=760)
        self.lbl4.place(x=500, y=810)
        self.lbl5.place(x=500, y=860)
        self.lbl6.place(x=500, y=910)
    def CreateButton(self):
        X = 250
        l = 0
        for timer in  data.data:
            def show(p=timer):
                return self.ShowButton(p)
            def func(x=timer):
                if self.timerbutton[x]["start_button"]["text"] == "►": return self.StartButton(x)
                else: return self.QuitButton(x)
            def delete(y = timer):
                return self.DeleteButton(y)
            def restart(j = timer):
                ans = tk.messagebox.askyesno(title="parri-detele-timer", message="Are you sure?")
                if ans == True:
                    self.timer.runtimer[j]["text"].set("00:00:00")
                    return self.timer.RestartTimer(j)

            s = str(data.data[timer]["s"])
            m = str(data.data[timer]["m"])
            h = str(data.data[timer]["h"])

            if len(s) == 1: s = "0" + s
            if len(m) == 1: m = "0" + m
            if len(h) == 1: h = "0" + h

            self.timer.runtimer.update({timer: {"text": tk.StringVar(value=f"{h}:{m}:{s}")}})
            self.timer.runtimer[timer]["time"] = [0, 0, 0]
            self.timer.runtimer[timer]["run"] = False

            self.timerbutton.update({timer:{"frame": tk.LabelFrame(root,text = timer,padx = 20)}})
            self.timerbutton[timer]["frame"].config(bg = "black",fg = "yellow",bd =5,font = ("Arial", 20, "bold"))

            frm = self.timerbutton[timer]["frame"]

            self.timerbutton[timer].update({"button" :tk.Button(frm, textvariable = self.timer.runtimer[timer]["text"],command = show)})
            self.timerbutton[timer]["button"].config(bg="black",width = 7, fg="yellow",bd = 10,font=("ds-digital", 22, "bold"))

            self.timerbutton[timer].update({"start_button": tk.Button(frm,text = "►",command = func)})
            self.timerbutton[timer]["start_button"].config(bg="black",bd = 0,highlightbackground= "black" ,fg=yew, font=("Arial", 25, "bold"))

            self.timerbutton[timer].update({"trush_button": tk.Button(frm, image = img_trush1_timer ,command = delete)})
            self.timerbutton[timer]["trush_button"].config(width = 50,heigh = 50,bd = 0,bg = "black",highlightbackground= "black",activebackground = "red")

            self.timerbutton[timer].update({"reload_button": tk.Button(frm, image = img_reload, padx=20,command = restart)})
            self.timerbutton[timer]["reload_button"].config(bg="black",width = 50,heigh = 50, fg="yellow", bd=0,highlightbackground= "black",activebackground = "blue")

            if mytree.eye_button[timer]["text"] == "T":
                l+=1
                X += 190
                self.timerbutton[timer]["frame"].place(x=X, y=100)
                self.timerbutton[timer]["button"].grid(row=1, column=0)
                self.timerbutton[timer]["start_button"].grid(row=2, column=0, sticky=tk.W)
                self.timerbutton[timer]["trush_button"].grid(row=2, column=0, columnspan=3, sticky=tk.E)
                self.timerbutton[timer]["reload_button"].grid(row=2, column=0, columnspan=2)
        self.ReplaceButton()
    def PlaceButton(self):
        X = 250
        l= 0
        for TIMER in data.data:
            if mytree.eye_button[TIMER]["text"] == "T" and l <= 5:
                l+= 1
                X += 190
                self.timerbutton[TIMER]["frame"].place(x=X, y=100)
    def ReplaceButton(self):
        for TIMER in self.timerbutton:
            self.timerbutton[TIMER]["frame"].place_forget()
        self.PlaceButton()
    def ShowButton(self,name):
        try: self.lbl["textvariable"] = self.timer.runtimer[name]["text"]
        except:
            s = str(data.data[name]["s"])
            m = str(data.data[name]["m"])
            h = str(data.data[name]["h"])
            if len(s) == 1: s = "0" + s
            if len(m) == 1: m = "0" + m
            if len(h) == 1: h = "0" + h
            self.lbl["textvariable"] = tk.StringVar(value = f"{h}:{m}:{s}")
        type_ = "Timerkeeper"
        if not data.data[name]["keeper"] == "True": type_ = "Count down timer"
        self.lbl1["text"] = "Creating date:  "+data.data[name]["date"]
        self.lbl2["text"] = "All time count:  " + data.data[name]["all"]
        self.lbl3["text"] = "Name:   "+name
        self.lbl4["text"] = "Type:   " + type_
        self.lbl5["text"] = "Alarm:  " + data.data[name]["alarm"]
        self.lbl6["text"] = "reset:  " + data.data[name]["reset"]
    def AddButton(self,name,row):
        for TIMER in self.timerbutton:
            self.timer.StopTimer(TIMER)
            self.timerbutton[TIMER]["frame"].destroy()
            self.timerbutton[TIMER]["button"].destroy()
            self.timerbutton[TIMER]["start_button"].destroy()
            self.timerbutton[TIMER]["trush_button"].destroy()
            self.timerbutton[TIMER]["reload_button"].destroy()
        self.timerbutton = {}
        data.NewData(name,row)
        mytree.reset_tree()
        self.CreateButton()
    def StartButton(self,btn):
        self.timer.StartTimer(btn)
    def QuitButton(self,btn):
        self.timer.StopTimer(btn)
    def DeleteButton(self,btn):
        ans = tk.messagebox.askyesno(title="parri-detele-timer", message="Are you sure?")
        if ans == True:
            self.timer.StopTimer(btn)
            data.Delete(btn)
            mytree.reset_tree()
            for element in self.timerbutton[btn].keys():
                self.timerbutton[btn][element].destroy()
            self.timerbutton.pop(btn)
            self.timer.runtimer.pop(btn)
            self.ReplaceButton()
class Timer:
    def __init__(self):
        self.init = 0
        self.t = 0
        self.button_x = 300
        self.runtimer = {}
        self.after =  None
        self.timerdict = {}
    def StartTimer(self,name):
        mytimer.timerbutton[name]["button"]["highlightbackground"] = "red"
        mytimer.timerbutton[name]["start_button"]["text"] = "■"
        Key = True
        if  data.data[name]["all"] == "False":
            self.runtimer[name]["time"][0] = int(data.data[name]["s"])
            self.runtimer[name]["time"][1] = int(data.data[name]["m"])
            self.runtimer[name]["time"][2] = int(data.data[name]["h"])
        else:
            time_ = data.data[name]["all_time"]
            s = int(time.time() - float(time_))
            h = int(s/3600)
            s = int(s%3600)
            m = int(s/60)
            s = int(s%60)
            if not data.data[name]["keeper"] == "True":
                H = int(data.data[name]["H"])-h
                M = int(data.data[name]["M"])-m
                S = int(data.data[name]["S"])-s
                if M<0: M = 60+M ; H = H-1
                if S < 0: S = 60 +S
                if S < 0 or M < 0 or H < 0 or(S,M,H) == (0,0,0):
                    data.data[name]["s"] = int(data.data[name]["S"])
                    data.data[name]["m"] = int(data.data[name]["M"])
                    data.data[name]["h"] = int(data.data[name]["H"])

                    self.RestartTimer(name)
                    Key = False
                else:
                    self.runtimer[name]["time"][0] = int(S)
                    self.runtimer[name]["time"][1] = int(M)
                    self.runtimer[name]["time"][2] = int(H)
            else:
                self.runtimer[name]["time"][0] = int(data.data[name]["S"])+ s
                self.runtimer[name]["time"][1] = int(data.data[name]["M"])+ m
                self.runtimer[name]["time"][2] = int(data.data[name]["H"])+ h
        if Key == True:
            self.runtimer[name]["run"] = True
            self.init = time.time()
            self.t = 0
            self.RunTimer()
    def RunTimer(self):
        t = round(time.time()-self.init)
        if t >= self.t+1:
            self.t = t
            for name in self.runtimer:
                if self.runtimer[name]["run"] == True:
                    if data.data[name]["keeper"] == "True":
                        self.runtimer[name]["time"][0] += 1
                        if self.runtimer[name]["time"][0] == 60:
                            self.runtimer[name]["time"][1] += 1
                            self.runtimer[name]["time"][0] = 0
                        if self.runtimer[name]["time"][1] == 60:
                            self.runtimer[name]["time"][1] = 0
                            self.runtimer[name]["time"][2] += 1
                    else:
                        self.runtimer[name]["time"][0] -= 1
                        if self.runtimer[name]["time"][0] < 0:
                            self.runtimer[name]["time"][1] -= 1
                            self.runtimer[name]["time"][0] = 59
                        if self.runtimer[name]["time"][1] < 0:
                            self.runtimer[name]["time"][1] = 59
                            self.runtimer[name]["time"][2] -= 1
                        if self.runtimer[name]["time"][2] <0: self.RestartTimer(name)
                        if self.runtimer[name]["time"][0] <= 0 and self.runtimer[name]["time"][1] <= 0 and self.runtimer[name]["time"][2] <= 0:
                            self.RestartTimer(name)
                            if data.data[name]["alarm"] == "True": playsound('./sounds/alarm.wav')
                            if data.data[name]["reset"] == "True": self.StartTimer(name)
                            else:
                                mytimer.timerbutton[name]["button"]["highlightbackground"] = "white"
                                mytimer.timerbutton[name]["start_button"]["text"] = "►"
                    s = str(self.runtimer[name]["time"][0])
                    m = str(self.runtimer[name]["time"][1])
                    h = str(self.runtimer[name]["time"][2])
                    if len(s) == 1: s = "0" + s
                    if len(m) == 1: m = "0" + m
                    if len(h) == 1: h = "0" + h
                    self.runtimer[name]["text"].set(f"{h}:{m}:{s}")
        self.after = root.after(100,self.RunTimer)
    def StopTimer(self,name):
        mytimer.timerbutton[name]["button"]["highlightbackground"] = "white"
        mytimer.timerbutton[name]["start_button"]["text"] = "►"
        self.runtimer[name]["run"] = False
        if self.runtimer[name]["time"] != [0,0,0] or not data.data[name]["keeper"]=="True":
            data.Save(name,self.runtimer[name]["time"])
    def RestartTimer(self,name):
        data.data[name]["all_time"] = time.time()
        if data.data[name]["all"] == "True" or not data.data[name]["keeper"] == "True":
            data.data[name]["s"] = data.data[name]["S"]
            data.data[name]["m"] = data.data[name]["M"]
            data.data[name]["h"] = data.data[name]["H"]
            s = data.data[name]["s"]
            m = data.data[name]["m"]
            h = data.data[name]["h"]
            if len(s) < 2: s = "0" + s
            if len(m) < 2: m = "0" + m
            if len(h) < 2: h = "0" + h
            self.runtimer[name]["time"][0] = int(s)
            self.runtimer[name]["time"][1] = int(m)
            self.runtimer[name]["time"][2] = int(h)
            self.runtimer[name]["text"].set(f"{h}:{m}:{s}")
        else:
            data.data[name]["s"] = 0
            data.data[name]["m"] = 0
            data.data[name]["h"] = 0
            self.runtimer[name]["time"][0] = 0
            self.runtimer[name]["time"][1] = 0
            self.runtimer[name]["time"][2] = 0
        if not data.data[name]["reset"] == "True":
            self.StopTimer(name)
class TimerTree:
    def __init__(self):
        self.butns = list(data.data.keys())
        self.eye_button = {}
        self.trush_button = {}
        self.btns = tk.StringVar(value = self.butns)
        self.tree_dir = tk.Listbox(root,listvariable = self.btns,bd = 10,heigh= 12,width = 19,bg="black", fg="yellow", font=("Arial", 20, "bold"))
        self.tree_dir.bind("<<ListboxSelect>>",self.timer_select)
        self.tree_dir.grid(row = 4,column = 0,padx = 10)
        Y = 261
        for name in self.butns:
            def eye(x = name):
                if self.eye_button[x]["text"] == "F":
                    self.eye_button[x]["image"] = img_open_eye
                    self.eye_button[x]["text"] = "T"
                    mytimer.ReplaceButton()
                else:
                    self.eye_button[x]["text"] = "F"
                    self.eye_button[x]["image"] = img_close_eye
                    mytimer.ReplaceButton()
            def remove(j = name):
                if list(mytimer.timer.runtimer.keys()).count(j)>0:
                    mytimer.DeleteButton(j)
                else:
                    ans = tk.messagebox.askyesno(title="parri-detele-timer", message="Are you sure?")
                    if ans == True:
                        data.Delete(j)
                        mytree.reset_tree()
            self.eye_button.update({name:tk.Button(root,text = "T",image = img_open_eye,bg = "black",bd=0,highlightbackground= "black",command = eye)})
            self.eye_button[name].place(x = 270,y=Y)

            self.trush_button.update({name: tk.Button(root,image=img_trush2_timer, bg="black", bd=0,highlightbackground="black",activebackground = "red", command=remove)})
            self.trush_button[name].place(x=235, y=Y)
            Y += 32
    def timer_select(self,event):
        btn_select = self.tree_dir.get(self.tree_dir.curselection())
        mytimer.ShowButton(btn_select)
    def reset_tree(self):
        Y = 261
        for btn in self.butns:
            self.eye_button[btn].destroy()
            self.trush_button[btn].destroy()
        self.butns = list(data.data.keys())
        self.btns.set(self.butns)
        for name in self.butns:
            def eye(x = name):
                if self.eye_button[x]["text"] == "F":
                    self.eye_button[x]["image"] = img_open_eye
                    self.eye_button[x]["text"] = "T"
                    mytimer.ReplaceButton()
                else:
                    self.eye_button[x]["text"] = "F"
                    self.eye_button[x]["image"] = img_close_eye
                    mytimer.ReplaceButton()
            def remove(j=name):
                if list(mytimer.timer.runtimer.keys()).count(j) > 0:
                    mytimer.DeleteButton(j)
                else:
                    ans = tk.messagebox.askyesno(title="parri-detele-timer", message="Are you sure?")
                    if ans == True:
                        data.Delete(j)
                        mytree.reset_tree()
            self.eye_button.update({name:tk.Button(root,text = "T",image = img_open_eye,bg = "black",bd=0,highlightbackground= "black",command = eye)})
            self.eye_button[name].place(x = 270,y=Y)
            self.trush_button.update({name: tk.Button(root,image=img_trush2_timer, bg="black", bd=0,highlightbackground="black", command=remove)})
            self.trush_button[name].place(x=235, y=Y)
            Y += 32
def CreateNewTimer():
   NT.NewWindow(root,mytimer,mytree)
#//////////////////////////////////////////////////////////////////////////////
#config creating the root
root = tk.Tk()
root.title("Parri-Timer")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
ico = tk.PhotoImage(file =r"./images/alarm.png")
root.iconphoto(True,ico)
root.configure(bg="black")
#crating the central clock
frame = tk.LabelFrame(root,width = 1150, height = 400)
frame.config(bg = "black",bd = 20)
frame.place(x = 440,y = 250)
#creating the imges for the program
img_title = tk.PhotoImage(file ="images/title.png")
img_add_timer = tk.PhotoImage(file ="images/add_timer.png")
img_config = tk.PhotoImage(file ="images/gear.png")
img_trush_timer = tk.PhotoImage(file ="images/trash.png")
img_reload = tk.PhotoImage(file ="images/reload.png").subsample(3, 3)
img_trush1_timer = tk.PhotoImage(file ="images/trash.png").subsample(3, 3)
img_trush2_timer = tk.PhotoImage(file ="images/trash.png").subsample(3, 3)
img_open_eye = tk.PhotoImage(file ="images/open_eye.png").subsample(3, 3)
img_close_eye = tk.PhotoImage(file ="images/close_eye.png").subsample(3, 3)
yew = "#faea01"
#starting the three objects
data = Data() #starting the data base
mytree = TimerTree() #starting the Timer tree
mytimer = TimerButtons() #starting all the timer_buttons
#title
lbl_title = tk.Label(root,image = img_title,bg = "black")
#btn add timer
btn_add_timer = tk.Button(root,image = img_add_timer,bd = 0,bg = "black",highlightbackground= "black",command = CreateNewTimer)
#btn_config = tk.Button(root,image = img_config,bd = 0,bg = "black",highlightbackground= "black",command = CreateNewTimer)
#grid the title and the butotn
lbl_title.grid(row = 0,column = 0,sticky= tk.W)
btn_add_timer.grid(row = 1,column = 0,padx = 10,pady = 10,sticky = tk.W)
#btn_config.grid(row = 1,column = 1,padx = 10,pady = 10,sticky = tk.W)
root.protocol('WM_DELETE_WINDOW',data.Close)
root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

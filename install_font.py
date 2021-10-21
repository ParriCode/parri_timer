import tkinter as tk
import os
import json
def Install():
    os.system("sudo cp -r ./fonts/ds_digital /usr/share/fonts/truetype")
    os.system("fc-cache -f -v")
    with open("config.json", "r+") as jfile:
        conf = json.load(jfile)
        conf["digital"] = True
        jfile.seek(0)
        json.dump(conf,jfile)
def LaterPlus(win):
    with open("config.json", "r+") as jfile:
        conf = json.load(jfile)
        conf["show_installer"] = False
        jfile.seek(0)
        json.dump(conf,jfile)
    win.destroy()
def ask():
    init_win = tk.Tk()
    init_win.geometry("500x200")
    init_win.resizable(width=0,height=0)
    init_win.config(bg= "black")
    danger = tk.PhotoImage(file = "./images/danger.png")
    tk.Label(init_win,bg = "black",image= danger).place(x= 20,y= 10)
    tk.Label(init_win,text = "Its recomendable \ninstall ds-digital font",bg = "black",fg = "yellow",font = ("Arial",20)).place(x = 120,y = 10)
    tk.Button(init_win,text = "Install",bg = "yellow",fg = "black",highlightbackground = "black",font = ("Arial",15,"bold"),command = Install).place(x = 20,y = 140)
    tk.Button(init_win,text = "Later",bg = "yellow",fg = "black",highlightbackground = "black",font = ("Arial",15,"bold"),command = init_win.destroy).place(x = 160,y = 140)
    tk.Button(init_win,text = "Don't show again",bg = "yellow",fg = "black",highlightbackground = "black",font = ("Arial",15,"bold"),command = lambda:LaterPlus(init_win)).place(x = 280,y = 140)
    init_win.mainloop()

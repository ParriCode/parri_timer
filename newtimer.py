import tkinter as tk
class NewWindow():
    def __init__(self,root,mytimer,mytree):
        def DESTROY(event):
            mytimer.AddButton(e_new_timer.get())
            mytree.reset_tree()
            newWin.destroy()
        newWin = tk.Toplevel(root)
        newWin.title("New Timer")
        newWin.geometry("380x70+850+400")
        newWin.resizable(width=0, height=0)
        newWin.config(bg="black")
        e_new_timer = tk.Entry(newWin, font=("Dejavu", 20, "bold"))
        e_new_timer.insert(tk.END, "name")
        e_new_timer.grid(row=0, column=0)
        tk.Label(newWin, text="Press Enter*", fg="yellow", bg="black", font=("Arial", 15, "italic")).grid(row=1,sticky=tk.W)
        newWin.bind("<Return>", DESTROY)

#Create an autoclicker GUI
import time
import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import *

class Autoclicker:
    def __init__(self, master):
        self.master = master
        master.title("Autoclicker")
        master.geometry("300x300")
        master.resizable(False, False)
        master.configure(background="black")

        self.label = Label(master, text="Autoclicker", font=("Helvetica", 20), fg="white", bg="black")
        self.label.pack()

        self.label = Label(master, text="Clicks Per Second", font=("Helvetica", 10), fg="white", bg="black")
        self.label.pack()

        self.cps = Entry(master, width=10)
        self.cps.pack()

        self.start = Button(master, text="Start", command=self.start)
        self.start.pack()

        self.stop = Button(master, text="Stop", command=self.stop)
        self.stop.pack()

        self.quit = Button(master, text="Quit", command=master.quit)
        self.quit.pack()

    def start(self):
        self.cps = int(self.cps.get())
        self.delay = 1 / self.cps
        while True:
            pyautogui.click()
            time.sleep(self.delay)

    def stop(self):
        pass

root = tk.Tk()
my_gui = Autoclicker(root)
root.mainloop()

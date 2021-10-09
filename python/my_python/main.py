#!/usr/bin/env python3
# coding: utf-8
# -----------------------------
# Author: mhcrnl@gmail.com

import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text="new window",
                                 width=25, command=self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = none


def main():
    root=tk.Tk()
    app = Demo1(root)
    root.mainloop()


if __name__=="__main__":
    main()
    

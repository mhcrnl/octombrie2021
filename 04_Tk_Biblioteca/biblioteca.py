#!/usr/bin/env python3
# coding: utf-8
#___________________________________________import modules
import pickle
import os.path
from tkinter import *
import tkinter.messagebox
from tkinter import ttk

#__________________________________________Class Carte
class Carte:
    """ Clasa Carte """
    
    def __init__(self, autor, titlu, editura, an, descriere, pret):
        self.autor = autor
        self.titlu = titlu
        self.editura = editura
        self.an = an
        self.descriere = descriere
        self.pret = pret

#__________________________________________Class Biblioteca
class Biblioteca:
    """ Clasa Biblioteca """
    
    def __init__(self, parent, titlu):
        self.parent = parent
        self.parent.title(titlu)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.initialization()
        self.icon()
        self.bind()
        self.set_listbox()
        self.lbx_names.focus_set()

    def icon(self):
        p1 = PhotoImage(file='teamwork.png')
        self.parent.iconphoto(False, p1)

    def bind(self):
        self.lbx_names.bind('<ButtonRelease-1>', self.on_click_lb)
        self.lbx_names.bind('<KeyRelease>', self.on_click_lb)

    def which_selected(self):
        return int(self.lbx_names.curselection()[0])
    
    def on_click_lb(self, event=None):
        self.set_data()

    def set_data(self):
        self.autor_var    .set(self.lst_carte[self.which_selected()].autor)
        self.titlu_var    .set(self.lst_carte[self.which_selected()].titlu)
        self.editura_var  .set(self.lst_carte[self.which_selected()].editura)
        self.an_var       .set(self.lst_carte[self.which_selected()].an)
        self.descriere_var.set(self.lst_carte[self.which_selected()].descriere)
        self.pret_var     .set(self.lst_carte[self.which_selected()].pret)

    def set_listbox(self):
        self.lbx_names.delete(0, END)
        for dat in range(len(self.lst_carte)):
            self.lbx_names.insert(END, self.lst_carte[dat].autor)
        self.lbx_names.selection_set(0) 
    #_______________________________________function initialization
    def initialization(self):
        main_frame = Frame(self.parent)
        main_frame.pack(fill=BOTH, expand=YES)

        self.autor_var = StringVar()
        self.titlu_var = StringVar()
        self.editura_var = StringVar()
        self.an_var = StringVar()
        self.descriere_var = StringVar()
        self.pret_var = StringVar()

        self.status_bar = Label(main_frame, text="Mihai Cornel mhcrnl@gmail.com -2021-", relief=SUNKEN,
                                bd=1).pack(side=BOTTOM, fill=X)

        frame1 = Frame(main_frame, bd=10)
        frame1.pack(fill=BOTH, expand=YES, side=LEFT)

        scroll = ttk.Scrollbar(frame1, orient=VERTICAL)
        self.lbx_names = Listbox(frame1, width=30, yscrollcommand=scroll.set)

        self.lbx_names.pack(fill=Y, side=LEFT)
        scroll.config(command=self.lbx_names.yview)
        scroll.pack(side=LEFT, fill=Y)

        frame2 = Frame(main_frame, bd=10)
        frame2.pack(fill=BOTH, expand=YES, side=RIGHT)

        frame3 = Frame(frame2)
        frame3.pack(side=TOP, expand=YES)

        
        Label(frame3, text="Autor:").grid(row=0, column=0, sticky=W)
        self.ent_autor = Entry(frame3, textvariable=self.autor_var, width=30)
        self.ent_autor.grid(row=0, column=1)

        Label(frame3, text="Titlu:").grid(row=1, column=0, sticky=W)
        self.ent_titlu = Entry(frame3, textvariable=self.titlu_var, width=30)
        self.ent_titlu.grid(row=1, column=1)

        Label(frame3, text="Editura:").grid(row=2, column=0, sticky=W)
        self.ent_editura = Entry(frame3, textvariable=self.editura_var,width=30)
        self.ent_editura.grid(row=2, column=1)

        Label(frame3, text="An").grid(row=3, column=0, sticky=W)
        self.ent_an = Entry(frame3, textvariable=self.an_var, width=10)
        self.ent_an.grid(row=3, column=1)

        Label(frame3, text="Descriere:").grid(row=4, column=0, sticky=W)
        self.ent_descriere = Entry(frame3, textvariable=self.descriere_var, width=40)
        self.ent_descriere.grid(row=4, column=1)

        Label(frame3, text="Pret:").grid(row=5, column=0, sticky=W)
        self.ent_pret = Entry(frame3, textvariable=self.pret_var, width=10)
        self.ent_pret.grid(row=5, column=1)

        frame4 = Frame(frame2)
        frame4.pack(side=BOTTOM, expand=YES)

        self.btn_new = ttk.Button(frame4, text="Nou",command=self.on_new, width=8)
        self.btn_new.pack(side=LEFT)
        
        self.btn_add = ttk.Button(frame4, text="Adauga", command=self.on_add, width=8)
        self.btn_add.pack(side=LEFT)
        
        self.btn_mod = ttk.Button(frame4, text="Modifica", command=self.on_mod, width=8)
        self.btn_mod.pack(side=LEFT)
        
        self.btn_del = ttk.Button(frame4, text="Sterge", command=self.on_del, width=8)
        self.btn_del.pack(side=LEFT)

        self.btn_inchide = ttk.Button(frame4, text="Inchide", command=self.on_exit, width=8)
        self.btn_inchide.pack(side=LEFT)

        self.lst_carte = self.load_address()

    def on_add(self, event=None):
        carte = Carte(self.autor_var.get(),
                      self.titlu_var.get(),
                      self.editura_var.get(),
                      self.an_var.get(),
                      self.descriere_var.get(),
                      self.pret_var.get())
        self.lst_carte.append(carte)
        self.set_listbox()
        self.save_address()


    def on_new(self, event=None):
        self.ent_autor.delete(0,END)
        self.ent_titlu.delete(0,END)
        self.ent_editura.delete(0,END)
        self.ent_an.delete(0,END)
        self.ent_descriere.delete(0,END)
        self.ent_pret.delete(0,END)

    def on_mod(self, event=None):
        self.lst_carte[self.which_selected()].autor = self.autor_var.get()
        self.lst_carte[self.which_selected()].titlu = self.titlu_var.get()
        self.lst_carte[self.which_selected()].editura = self.editura_var.get()
        self.lst_carte[self.which_selected()].an = self.an_var.get()
        self.lst_carte[self.which_selected()].descriere = self.descriere_var.get()
        self.lst_carte[self.which_selected()].pret = self.pret_var.get()
        self.set_listbox()
        self.modify_address()

    def on_del(self, event=None):
        del self.lst_carte[self.which_selected()]
        self.set_listbox()
        self.on_new()
        self.delete_address()

    def save_address(self):
        outfile = open("address.dat", "wb")
        pickle.dump(self.lst_carte, outfile)
        tkinter.messagebox.showinfo("Carte Salvata!","O carte noua a fost adaugata")
        outfile.close()

    def modify_address(self):
        outfile = open("address.dat", "wb")
        pickle.dump(self.lst_carte, outfile)
        tkinter.messagebox.showinfo("Carte modificata!", "Modificare salvata.")
        outfile.close()

    def delete_address(self):
        outfile = open("address.dat", "wb")
        pickle.dump(self.lst_carte, outfile)
        tkinter.messagebox.showinfo("Carte stearsa", "Cartea a fost stearsa.")
        outfile.close()

    def load_address(self):
        if not os.path.isfile("address.dat"):
            return []
        try:
            infile = open("address.dat", "rb")
            lst_carte = pickle.load(infile)
        except EOFError:
            lst_carte = []
        infile.close()
        return lst_carte
    
    #_______________________________________function on_exit
    def on_exit(self, event=None):
        self.parent.destroy()



if __name__ == "__main__":
    root = Tk()
    appl = Biblioteca(root, "BIBLIOTECA")
    root = mainloop()
        
    

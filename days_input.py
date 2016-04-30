'''
Description here: 


Created by: Kenny Chong (kennychong89@gmail.com)
Date: 02/28/2016

Note: Works only for Python 3.x and above.
'''
import tkinter as Tkinter
from tkinter import ttk
import Table as dtable

class DaysInput(ttk.LabelFrame):
	
    def __init__(self, master=None, **kw):
        ttk.LabelFrame.__init__(self, master, **kw)
	
        self._hours = Tkinter.IntVar()
        self._pay = Tkinter.DoubleVar()
        self.__init_widgets()

    def __init_widgets(self):
        frame1 = ttk.Frame(self)

        ttk.Label(frame1, text="Hours:").grid(row=0, sticky=Tkinter.E, padx=5)
        ttk.Entry(frame1, width=3, textvariable=self._hours).grid(row=0, column=1, sticky=Tkinter.E, padx=10)
	
        ttk.Label(frame1, text="Pay:").grid(row=0, column=2, sticky=Tkinter.E, padx=1, pady=10)
        ttk.Entry(frame1, width=5, textvariable=self._pay).grid(row=0, column=3, sticky=Tkinter.E, padx=1)
	
        self._fill_button = ttk.Button(frame1, text="Fill Table")
        self._fill_button.grid(row=0, column=4, sticky=Tkinter.E, padx=10, pady=10)
       
        frame1.pack(anchor="nw", fill="x")

        frame2 = ttk.Frame(self)
	
        self._day_table = days_cal_table = dtable.Table(frame2, rows=7, columns=4,  labels=["Days", "Hours", "Pay Per Hour", "Exclude"])
        self._day_table.grid(row=0, column=0, sticky=Tkinter.E)

        frame2.pack(anchor="nw", fill="x")

        self._clear_button = ttk.Button(self, text="Clear Entries")
        self._clear_button.pack(side=Tkinter.RIGHT, padx=5, pady=5)

        # bind buttons and other widgets here
        self._fill_button.bind("<Button-1>", self.__fillTable)  
        self._clear_button.bind("<Button-1>", self.__clearTable)
        
    def __fillTable(self, event):
        table_rows = self._day_table.get_rows()
        
        for row in range(table_rows):
            self._day_table.set_hour(row, self.get_hour())
            self._day_table.set_pay(row, self.get_pay())
    
    def __clearTable(self, event):    
        table_rows = self._day_table.get_rows()
        
        for row in range(table_rows):
            self._day_table.set_hour(row, 0)
            self._day_table.set_pay(row, 0.0)

    def get_hour(self):
        return self._hours.get()

    def get_pay(self):
        return self._pay.get()

    def get_table(self):
        return self._day_table

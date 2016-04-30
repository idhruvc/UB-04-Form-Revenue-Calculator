'''
Description here: 


Created by: Kenny Chong (kennychong89@gmail.com)
Date: 02/28/2016

Note: Works only for Python 3.x and above.
'''
import tkinter as Tkinter
from tkinter import ttk

class RateInput(ttk.LabelFrame):
	
    def __init__(self, master=None, **kw):
        ttk.LabelFrame.__init__(self, master, **kw)
	
        self._units = Tkinter.IntVar()
        self._revcode = Tkinter.StringVar()
        self._description = Tkinter.StringVar()
        self._billing_code = Tkinter.StringVar()
        self.__init_widgets()

    def __init_widgets(self):
        ttk.Label(self, text="Units:").grid(row=0, sticky=Tkinter.E, padx=(1,5), pady=10)
        ttk.Entry(self, width=3, textvariable=self._units).grid(row=0, column=1, sticky=Tkinter.W, padx=10)
	
        ttk.Label(self, text="Rev Code:").grid(row=0, column=2, sticky=Tkinter.E, padx=1, pady=10)
        ttk.Entry(self, width=5, textvariable=self._revcode).grid(row=0, column=3, sticky=Tkinter.W, padx=10)

        ttk.Label(self, text="Description:").grid(row=1, sticky=Tkinter.E, padx=1, pady=10)
        ttk.Entry(self, width=20, textvariable=self._description).grid(row=1, column=1, sticky=Tkinter.E, padx=10)
		
        ttk.Label(self, text="Billing Code:").grid(row=2, sticky=Tkinter.E, padx=1, pady=10)
        ttk.Entry(self, width=20, textvariable=self._billing_code).grid(row=2, column=1, sticky=Tkinter.E, padx=10)
		
        self._units.set(4)
        self._revcode.set("0570")
        self._description.set("Personal Care Aide")
        self._billing_code.set("T1019")

    def get_units(self):
        return self._units.get()
    
    def get_rev_code(self):
	    return self._revcode.get()
		
    def get_description(self):
	    return self._description.get()
	
    def get_billing_code(self):
        return self._billing_code.get()
		
    #def get_pay_per_units(self):
        #return self._pay_per_units.get()

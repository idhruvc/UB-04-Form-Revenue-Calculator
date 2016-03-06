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
        #self._pay_per_units = Tkinter.DoubleVar()
        self.__init_widgets()

    def __init_widgets(self):
        ttk.Label(self, text="Units:").grid(row=0, sticky=Tkinter.E, padx=1)
        ttk.Entry(self, width=3, textvariable=self._units).grid(row=0, column=1, sticky=Tkinter.E, padx=10, pady=10)
	
        #ttk.Label(self, text="Pay Per Units:").grid(row=0, column=2, sticky=Tkinter.E, padx=1, pady=10)
        #ttk.Entry(self, width=5, textvariable=self._pay_per_units).grid(row=0, column=3, sticky=Tkinter.E, padx=10)

        self._units.set(4)
        #self._pay_per_units.set(0.00)

    def get_units(self):
        return self._units.get()
    
    #def get_pay_per_units(self):
        #return self._pay_per_units.get()

'''
Description here: 


Created by: Kenny Chong (kennychong89@gmail.com)
Date: 02/28/2016

Note: Works only for Python 3.x and above.
'''
import tkinter as Tkinter
from tkinter import ttk

class Table(ttk.Frame):
	
    def __init__(self, master=None, rows=10, columns=2, labels=[], **kw):
        ttk.Frame.__init__(self, master, **kw)
	
        self._rows = rows
        self._columns = columns
        self._row_data = dict()
        self.__init_table(labels)
	
    def __init_table(self, labels):
       self._widgets = []
       
       # write labels for the table
       for column in range(self._columns):
           label = ttk.Label(self, text=labels[column], borderwidth=0, width=10)
           label.grid(row=0, column=column, sticky="nsew", padx=5, pady=5)	

  
       days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")	

       # write each row
       for row in range(1,self._rows+1):
           current_row = []
           day_label = ttk.Label(self, text=days[row-1], borderwidth=0, width=10)
           day_label.grid(row=row, column=0, sticky="nsew", padx=5, pady=1)
           
           hour_entry_val = Tkinter.IntVar()
           hour_entry = ttk.Entry(self, width=5, textvariable=hour_entry_val)
           hour_entry.grid(row=row, column=1, sticky="nsew", padx=5, pady=1)

           pay_entry_val = Tkinter.DoubleVar()
           pay_entry = ttk.Entry(self, width=5, textvariable=pay_entry_val)
           pay_entry.grid(row=row, column=2, sticky="nsew", padx=5, pady=1)

           # remember to make this button functional
           exclude_entry_val = Tkinter.BooleanVar()
           exclude_checkbutton = ttk.Checkbutton(self, variable = exclude_entry_val)
           exclude_checkbutton.grid(row=row, column=3, sticky="nsew", padx=5, pady=1) 

           #current_row.append({'day': row, 'hour_entry': hour_entry, 'pay_entry': pay_entry})

           self._row_data[row-1] = {'hour_value': hour_entry_val, 'pay_value': pay_entry_val, 'excluded_value': exclude_entry_val}

    def set_hour(self, row, hour=0):
        if row in self._row_data:
           self._row_data[row]['hour_value'].set(hour)
      
    def set_pay(self, row, pay=0.00):
        if row in self._row_data:
           self._row_data[row]['pay_value'].set(pay)

    def get_hour(self, row):
        if row in self._row_data:
           return self._row_data[row]['hour_value'].get()

    def get_pay(self, row):
        if row in self._row_data:
           return self._row_data[row]['pay_value'].get()
 
    def get_rows(self):
        return self._rows

    def is_day_excluded(self, row):
        if row in self._row_data:
           return self._row_data[row]['excluded_value'].get()

if __name__ == "__main__":
    root = Tkinter.Tk()
 
    t = Table(root,rows=7, columns=4, labels=["Days", "Hours", "Pay Per Hour", "Exclude"])
    t.pack(expand=1, fill='both')

    root.mainloop()

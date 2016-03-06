'''
Description here: 


Created by: Kenny Chong (kennychong89@gmail.com)
Date: 02/28/2016

Note: Works only for Python 3.x and above.
'''
import tkinter as Tkinter
import calendar
from datetime import datetime, date, timedelta
from tkinter import ttk
from PIL import Image, ImageTk

class DatePicker(ttk.LabelFrame):
	
    def __init__(self, master=None, **kw):
        ttk.LabelFrame.__init__(self, master, **kw)
	
        self._from_date = Tkinter.StringVar()
        self._to_date = Tkinter.StringVar()
        self.__init_widgets()

    def __init_widgets(self):
        pil_image = Image.open("calendar-256.png")
        pil_image.thumbnail((10,10), Image.ANTIALIAS)

        self.calendar_icon = ImageTk.PhotoImage(pil_image)

        ttk.Label(self, text="From:").grid(row=0, sticky=Tkinter.E, padx=1, pady=(10,10))
        
        ttk.Entry(self, width=10, textvariable=self._from_date).grid(row=0, column=1, sticky=Tkinter.E, padx=(1,1))    
        ttk.Button(self, text="Calendar", image=self.calendar_icon).grid(row=0, column=2, sticky=Tkinter.E, padx=(1,1))
	
        ttk.Label(self, text="To:").grid(row=0, column=3, sticky=Tkinter.E, padx=(15,1), pady=(10,10))
        ttk.Entry(self, width=10, textvariable=self._to_date).grid(row=0, column=4, sticky=Tkinter.E, padx=(1,1))
        ttk.Button(self, text="Calendar", image=self.calendar_icon).grid(row=0, column=5, sticky=Tkinter.E, padx=1)

        self._from_date.set(self.__get_first_day_of_current_month())
        self._to_date.set(self.__get_last_day_of_current_month())	

    def get_from_date(self):
        return self._from_date.get()

    def get_to_date(self):
        return self._to_date.get()

    '''
        The implementations for the set of functions below are derived from "Python Cookbook 3rd Edition"
    '''
    def __get_first_day_of_current_month(self):
        return date.strftime(date.today().replace(day=1), "%x")

    def __get_last_day_of_current_month(self):
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)

        end_date = start_date + timedelta(days=days_in_month - 1)
        
        return date.strftime(end_date, "%x")

    def get_date_range(start, stop, step):
        while start <= stop:
            yield start
            start += step

    def get_all_days_from_date_range(self):
        from_date = datetime.strptime(self.get_from_date(), "%x")
        to_date = datetime.strptime(self.get_to_date(), "%x")

        temp = []
 
        for d in DatePicker.get_date_range(from_date, to_date, timedelta(days=1)):
            day = calendar.weekday(d.year, d.month, d.day)
            temp.append((day, date.strftime(d, "%m/%d/%Y")))     
        
        return temp 

def test():
    '''
    root = Tkinter.Tk()
    
    datepickerFrame = DatePicker(root,text=DatePicker.get_last_day_of_current_month())    
    datepickerFrame.pack(expand=1, fill='both')

    root.mainloop()
    '''
    #print(DatePicker.get_last_day_of_current_month())

    x = DatePicker.get_all_days_from_date_range()
    print(x)

if __name__ == '__main__':
    test()

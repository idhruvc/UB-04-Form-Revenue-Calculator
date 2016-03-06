'''
The purpose of this program helps simplify revenue processing for the UB-04 medical claim form.
Given the month and days serviced and the charge rate, the program will calculate
and display the total charges for each day of a specific month. 

Created by: Kenny Chong (kennychong89@gmail.com)
Date: 02/28/2016

Note: Works only for Python 3.x and above.
'''
import tkinter as Tkinter
from tkinter import ttk

import date_picker as dp
import rate_input  as rp
import days_input  as di

# Program start
class BillingCalculator:

    def __init__(self):
        root = Tkinter.Tk()
        root.title("UB-04 Claim Form Revenue Calculator")

        ''' GUI initialization starts here '''
        # test
        frame_left = ttk.Frame(root)
        frame_left.pack(side=Tkinter.LEFT, fill='y')

        self._date_picker_frame = dp.DatePicker(frame_left, text="Date")
        self._date_picker_frame.pack(expand=1, fill='both')

        self._rate_input_frame = rp.RateInput(frame_left, text="Rate")
        self._rate_input_frame.pack(expand=1, fill='both')

        self._days_input_frame = di.DaysInput(frame_left, text="Days")
        self._days_input_frame.pack(expand=1, fill='both')

        self._calculate_button = ttk.Button(frame_left, text="Calculate")
        self._calculate_button.pack(side=Tkinter.RIGHT, padx=5, pady=5)
        self._calculate_button.bind("<Button-1>", self.__calculate)
    
        frame_right = ttk.Frame(root)
        frame_right.pack(side=Tkinter.RIGHT, expand=1, fill='both')

        self._content_text = Tkinter.Text(frame_right, wrap='word', height=10, width=50)
        self._content_text.pack(side=Tkinter.LEFT, expand=1, fill='both')
        
        scroll_bar = ttk.Scrollbar(frame_right)
        self._content_text.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self._content_text.yview)
        scroll_bar.pack(side=Tkinter.RIGHT, fill='y')

        ''' GUI initialization ends here '''
    
        root.mainloop()	 

    def __calculate(self, event):
       # get dates
       dates = self._date_picker_frame.get_all_days_from_date_range()
       units = self._rate_input_frame.get_units()
       #pay_per_units = self._rate_input_frame.get_pay_per_units()

       table = self._days_input_frame.get_table()
       records = []       
       total_bill = 0.00

       for d in dates:
           day_num, day_string = d[0], d[1]
           excluded = table.is_day_excluded(int(day_num))
          
           if not excluded:
               hour = table.get_hour(int(day_num))
               pay = table.get_pay(int(day_num))

               total_units_for_date = units * hour
               total_pay_for_date = pay * hour
               total_bill += total_pay_for_date

               records.append(day_string + " | " + str(total_units_for_date) + " | " + str(round(total_pay_for_date,2)))
       
       self.__update_record(records, total_bill)

    def __update_record(self, records, total_bill):
        self._content_text.delete('1.0', Tkinter.END)
        i = 1
        
        for r in records:
           if i < 10:
               self._content_text.insert(Tkinter.END, "0" + str(i) + ". " + r + "\n")
           else:
               self._content_text.insert(Tkinter.END, str(i) + ". " + r + "\n")
       
           i += 1

        self._content_text.insert(Tkinter.END, "Total: " + str(round(total_bill,2)))

if __name__ == '__main__':
    test = BillingCalculator()

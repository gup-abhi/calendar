#Tkinter module for GUI
from tkinter import *

#Calendar module for getting calendar
import calendar

#calling calendar modules calendar function to get specific calendar
text = calendar.calendar(2020)

#creating window to display our calendar
root = Tk()

#setting window size
root.geometry("500x650")

#window title
root.title("Calendar")

#creating heading by using label component
label1 = Label(root, text = 'CALENDAR', bg = 'dark gray', font = ('times', 28, 'bold'))

#placing label in the window
label1.grid(row = 1, column = 1, padx = 5, pady = 5)

#setting background color of window
root.config(background = 'white')

#creating another label to put calendar data
label2 = Label(root, text = text, font = 'Consoles 10')

#placing label in the window
label2.grid(row = 2, column = 1, padx = 20, pady = 10)
root.mainloop()
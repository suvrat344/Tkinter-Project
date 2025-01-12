from tkinter import *
from datetime import date

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Age Calculator")
photo = PhotoImage(file = r"./AgeCalculator.png")
myImage = Label(image = photo)
myImage.pack(padx = 15, pady = 15)


def calculateAge():
  year = int(yearValue.get())
  month = int(monthValue.get())
  day = int(dayValue.get())
  today = date.today()
  birthdate = date(year,month,day)
  years = today.year - birthdate.year
  months = today.month - birthdate.month
  days = today.day - birthdate.day
  
  if(months < 0):
    years = years - 1
    months = months + 12
    
  if(days < 0):
    months = months - 1
    if(today.month == 1):
      previous_month = 12
    else:
      previous_month = today.month - 1
      
    if(previous_month in [1,3,5,7,8,10,12]):
      days = days + 31
    elif(previous_month in [4,6,9,11]):
      days = days + 30
    elif(previous_month == 2):
      if(today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0)):
        days += 29
      else:
        days += 28
      
  
  Label(root, text = f"Age : {years} years, {months} months, {day} days", font = 23).place(x = 250, y = 550)

# name
Label(text = "Name", font = 23).place(x = 200, y = 250)
nameValue = StringVar()
nameEntry = Entry(root, textvariable = nameValue, width = 30, font = 20, bd = 2)
nameEntry.place(x = 300, y = 250)

# year
yearValue = StringVar()
Label(text = "Year", font = 23).place(x = 200, y = 300)
yearEntry = Entry(root, textvariable = yearValue, width = 30, font = 20, bd = 2)
yearEntry.place(x = 300, y = 300)

# month 
monthValue = StringVar()
Label(text = "Month", font = 23).place(x = 200, y = 350)
monthEntry = Entry(root, textvariable = monthValue, width = 30, font = 20, bd = 2)
monthEntry.place(x = 300, y = 350)

# day
dayValue = StringVar()
Label(text = "Day", font = 23).place(x = 200, y = 400)
dayEntry = Entry(root, textvariable = dayValue, width = 30, font = 20, bd = 2)
dayEntry.place(x = 300, y = 400)

Button(text = "Calculate", width = 11, bd = 5, bg = "black", fg = "white", font = 20, command = calculateAge).place(x = 350, y = 500)

root.mainloop()
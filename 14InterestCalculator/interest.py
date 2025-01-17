from tkinter import *

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("500x350")
root.resizable(False, False)

def calculateSimpleInterest():
  principal = int(principalValue.get())
  interest = int(interestValue.get())
  time = int(timeValue.get())
  si = principal * interest * time * 0.01
  
  simpleInterest = Label(root, text = f"Simple Interest {si}", font = "arial 20")
  simpleInterest.place(x = 100, y = 230)
  

Label(root, text = "Simple Interest Calculator", font = "arial 25").place(x = 50, y = 20)

# principal
principalValue = StringVar()
principal = Label(root, text = "Principal", font = "arial 15")
principal.place(x = 50, y = 80)
principalEntry = Entry(root, textvariable = principalValue, width = 15, font = "arial 15")
principalEntry.place(x = 200, y = 80)


# roi
interestValue = StringVar()
interest = Label(root, text = "Rate of Interest", font = "arial 15")
interest.place(x = 50, y = 130)
interestEntry = Entry(root, textvariable = interestValue, width = 15, font = "arial 15")
interestEntry.place(x = 200, y = 130)


# time
timeValue = StringVar()
time = Label(root, text = "Time(Years)", font = "arial 15")
time.place(x = 50, y = 180)
timeEntry = Entry(root, textvariable = timeValue, width = 15, font = "arial 15")
timeEntry.place(x = 200, y = 180)


# calculate button
Button(text = "Calculate", command = calculateSimpleInterest, font = "arial 15").place(x = 380, y = 80)

# exit button
Button(text = "Exit", command = exit, width = 8, font = "arial 15").place(x = 380, y = 130)

root.mainloop()
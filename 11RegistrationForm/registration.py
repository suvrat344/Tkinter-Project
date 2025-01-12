from tkinter import *

# create window
root = Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False, False)

def register():
  # fetch data from fields
  name_info = nameValue.get()
  phone_info = phoneValue.get()
  gender_info = genderValue.get()
  email_info = emailValue.get()
  
  # write data in file
  file = open(name_info + ".txt","w")
  file.write(name_info+"\n")
  file.write(phone_info+"\n")
  file.write(gender_info+"\n")
  file.write(email_info+"\n")
  file.close()
  
  # delete entry after write in the file
  nameEntry.delete(0,END)
  phoneEntry.delete(0,END)
  genderEntry.delete(0,END)
  emailEntry.delete(0,END)
  
  Label(text = "Registration Success", fg = "green", font = ("calibri", 11)).place(x = 250, y = 420)
  
  
Label(root, text = "Python Registration Form", font = "arial 25").pack(pady = 50)

# name field
nameValue = StringVar()
Label(text = "Name", font = 23).place(x = 100, y = 150)
nameEntry = Entry(root, textvariable = nameValue, width = 30, bd = 2, font = 20)
nameEntry.place(x = 200, y = 150)


# phone field
phoneValue = StringVar()
Label(text = "Phone", font = 23).place(x = 100, y = 200)
phoneEntry = Entry(root, textvariable = phoneValue, width = 30, bd = 2, font = 20)
phoneEntry.place(x = 200, y = 200)


# gender field
genderValue = StringVar()
Label(text = "Gender", font = 23).place(x = 100, y = 250)
genderEntry = Entry(root, textvariable = genderValue, width = 30, bd = 2, font = 20)
genderEntry.place(x = 200, y = 250)


# email field
emailValue =  StringVar()
Label(text = "Email", font = 23).place(x = 100, y = 300)
emailEntry = Entry(root, textvariable = emailValue, width = 30, bd = 2, font = 20)
emailEntry.place(x = 200, y = 300)


# check button
checkValue = IntVar()
checkbtn = Checkbutton(text = "Remember Me?", variable = checkValue)
checkbtn.place(x = 200, y = 340)


# register button
Button(text = "Register", font = 20, width = 11, height = 1, command = register).place(x = 250, y = 370)

root.mainloop()
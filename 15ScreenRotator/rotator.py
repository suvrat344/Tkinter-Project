# python -m pip install rotate-screen

from tkinter import *
import rotatescreen

root = Tk()
root.title("Screen Rotation")
root.resizable(False, False)
root.geometry("500x500")
root.configure(bg = "#54c5d1")

def Screen_Rotate(pos):
  screen = rotatescreen.get_primary_display()
  if(pos == "up"):
    screen.set_landscape()
  elif(pos == "right"):
    screen.set_portrait_flipped()
  elif(pos == "down"):
    screen.set_landscape_flipped()
  elif(pos == "left"):
    screen.set_portrait()

# background image
photo = PhotoImage(file = r"./background.png")
myImage = Label(image = photo)
myImage.pack(padx = 2, pady = 2)


# up button
Button(root,text = "Up",command = lambda : Screen_Rotate("up"), bg = "white", font = "arial 18", width = 5).place(x = 200, y = 50)

# right button
Button(root,text = "Right",command = lambda : Screen_Rotate("right"), bg = "white", font = "arial 18", width = 5).place(x = 402, y = 220)

# left button
Button(root,text = "Left",command = lambda : Screen_Rotate("left"), bg = "white", font = "arial 18", width = 5).place(x = 20, y = 220)

# down button
Button(root,text = "Down",command = lambda : Screen_Rotate("down"), bg = "white", font = "arial 18", width = 5).place(x = 220, y = 400)

root.mainloop()
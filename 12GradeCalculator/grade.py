from tkinter import *

root = Tk()
root.title("Grade Calculator")
root.geometry("500x500")
root.resizable(False, False)

def calculate():
  english = int(englishMarks.get())
  analyticalSkill = int(analyticalSkillMarks.get())
  generalKnowledge = int(generalKnowledgeMarks.get())
  total = english + analyticalSkill + generalKnowledge
  average = int(total / 3)
  Label(text = f"{total}", font = "arial 15 bold").place(x = 200, y = 220)
  Label(text = f"{average}", font = "arial 15 bold").place(x = 200, y = 270)
  if(average > 50):
    grade = "PASS"
  else:
    grade = "FAIL"
  Label(text = f"{grade}", font = "arial 15 bold", fg="blue").place(x = 200, y = 320)
  
# label
Label(root, text = "Grade Calculator", font = "arial 25").pack(pady = 20)

# english 
englishMarks = StringVar()
sub1 = Label(root, text = "English", font = "arial 10")
sub1.place(x = 50, y = 70)
englishMarksEntry = Entry(root, textvariable = englishMarks, font = "arial 15", width = 15) 
englishMarksEntry.place(x = 200, y = 70)


# analytical skills
analyticalSkillMarks = StringVar()
sub2 = Label(root, text = "Analytical Skill", font = "arial 10")
sub2.place(x = 50, y = 120)
analyticalSkillMarksEntry = Entry(root, textvariable = analyticalSkillMarks, font = "arial 15", width = 15) 
analyticalSkillMarksEntry.place(x = 200, y = 120)


# general knowledge
generalKnowledgeMarks = StringVar()
sub3 = Label(root, text = "General Knowledge", font = "arial 10")
sub3.place(x = 50, y = 170)
generalKnowledgeMarksEntry = Entry(root, textvariable = generalKnowledgeMarks, font = "arial 15", width = 15) 
generalKnowledgeMarksEntry.place(x = 200, y = 170)


# total
totalMarks = StringVar()
total = Label(root, text = "Total", font = "arial 10")
total.place(x = 50, y = 220)


# average
averageMarks = StringVar()
average = Label(root, text = "Average", font = "arial 10")
average.place(x = 50, y = 270)


# grade
gradeValue = StringVar()
grade = Label(root, text = "Grade", font = "arial 10")
grade.place(x = 50, y = 320)


# button
Button(text = "Calculate", font = "arial 15", bg = "white", bd = 5, command = calculate).place(x = 100, y = 370)

Button(text = "Exit", font = "arial 15", bg = "white", bd = 5, width = 10, command = exit).place(x = 300, y = 370)


root.mainloop()
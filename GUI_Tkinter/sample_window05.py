from tkinter import *

root = Tk()


#click_1
# def printName():
#     print("Chello my name is Bucky!")
#
# button_1 = Button(root, text="Print my name", command=printName)
# button_1.pack()

#click_2


def print_name(event):
    print("Chello my name is Bucky!")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", print_name)
button_1.pack()
root.mainloop()
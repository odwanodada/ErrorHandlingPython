from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Customer Account")
root.geometry("1000x400+400+200")



def result():
    amount = int(myEntry.get())

    try:
        if amount > 3000:
            output.configure(text="You qualify for the Malaysia trip")
        else:
            output.configure(text="Please deposit more funds for this excursion")
    except TypeError:
           output.configure(text="Please enter a number")



def exit():
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        root.destroy()
    else:
        pass







myLabel = Label(root,text="Enter Amount (R)").place(x=10,y=60)
myEntry = Entry(root,width= 20).place(x=200,y=60)

button = Button(root, text="Calculate", bg="yellow", width=7, activeforeground="yellow", font=("arial", 15, "bold"))
button.place(x=200,y=100)

button_exit = Button(root, text="Exit", bg="yellow", width=7, activeforeground="yellow", font=("arial", 15, "bold"),command=exit)
button_exit.place(x=350,y=100)

output = Label(root, width=20, height=3, bg="white",font=("arial", 20, "bold"))
output.place(x=200,y=150)






root.mainloop()
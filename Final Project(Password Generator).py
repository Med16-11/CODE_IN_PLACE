#The following program will generate password using random library 
#It will ask the user what kind of password they want to generate
#Stroong, average or poor and then it will generate password according to their choice

from tkinter import*
import random
import string


root = Tk()
root.title("PASSWORD GENERATOR")

title = StringVar()
label = Label(root,textvariable = title).pack()
title.set('The Strength of Password')

def selection():
    selection = choice.get()
    
choice = IntVar()
R1 = Radiobutton(root, text = "Poor", variable = choice,value = 1,command = selection).pack(anchor = CENTER)
R2 = Radiobutton(root, text = "Medium", variable = choice,value = 2,command = selection).pack(anchor = CENTER)
R3 = Radiobutton(root, text = "Strong", variable = choice,value = 3,command = selection).pack(anchor = CENTER)

labelchoice = Label(root)
labelchoice.pack()

lenlabel = StringVar()
lenlabel.set('Enter the length of the password')
lentitle = Label(root, textvariable = lenlabel).pack()

val = IntVar()
spinlength = Spinbox(root,from_ =8, to =24, textvariable = val,width = 13).pack()

def callback():
    Isum.config(text = passgen())
    
passgenButton =  Button(root, text = 'Generate Password',bd = 5,height = 2,command = callback,pady=3)
passgenButton.pack()
password=str(callback)
    
Isum = Label(root,text="")
Isum.pack(side=BOTTOM)
    
#for poor password
poor = string.ascii_uppercase+string.ascii_lowercase
medium = string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols = "!@#=$%^&*()_+}]:;?/.,~"
strong = poor+medium+symbols
    
def passgen():
    if choice.get() == 1:
        return"".join(random.sample(poor,val.get()))
    elif choice.get() == 2:
        return"".join(random.sample(medium,val.get()))
    elif choice.get() == 3:
        return"".join(random.sample(strong,val.get()))
        
root.mainloop()
    

    

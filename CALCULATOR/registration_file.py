from tkinter import *
root = Tk()
root.title("Registration From")
root.geometry("500x300")

def submit():
    print("submit!")

Label(text="Registraion Form", font="poppins 15 bold").grid(row=0, column=3)

name = Label(root,text="Name", font="poppins 10")
phone = Label(root, text="Phone", font="poppins 10")
gender = Label(root, text="Gender", font="poppins 10")
emergency = Label(root, text="Emergency", font="poppins 10")
paymentmood = Label(root, text="Paymentmood", font="poppins 10")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

name_value = StringVar
phone_value = StringVar
gender_value = StringVar
emergency_value = StringVar
paymentmood_value = StringVar
check_value = IntVar

name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
emergency_entry = Entry(root, textvariable=emergency_value)
paymentmood_entry = Entry(root, textvariable=paymentmood_value)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
paymentmood_entry.grid(row=5, column=3)

checkbutton = Checkbutton(text="remember me?", variable=check_value)
checkbutton.grid(row=6, column=3)

Button(text="Submit", command=submit).grid(row=7, column=3)

root.mainloop()

from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")


    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_month.config(text=month)
    lab_day.config(text=day)
    lab_year.config(text=year)
    lab_date.config(text=date)
    lab_am.config(text=am)
    lab_hr.after(200, date_time())


clock = Tk()
clock.title("     ***** Digital Clock *******     ")
clock.geometry("1000x700")
clock.config(bg="yellow")

# hr min sec

lab_hr = Label(clock, text="00", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_hr.place(x=100, y=150, height=150, width=150)

lab_hr_txt = Label(clock, text="Hour", font=("poppins", 20, "bold"), bg="red", fg="white")
lab_hr_txt.place(x=100, y=330, height=30, width=150)


lab_min = Label(clock, text="00", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_min.place(x=350, y=150, height=150, width=150)

lab_min_txt = Label(clock, text="Minute", font=("poppins", 15, "bold"), bg="red", fg="white")
lab_min_txt.place(x=350, y=330, height=30, width=150)


lab_sec = Label(clock, text="00", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_sec.place(x=600, y=150, height=150, width=150)

lab_sec_txt = Label(clock, text="Second", font=("poppins", 15, "bold"), bg="red", fg="white")
lab_sec_txt.place(x=600, y=330, height=30, width=150)

lab_am = Label(clock, text="AM", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_am.place(x=800, y=150, height=150, width=150)

lab_such_txt = Label(clock, text="AM/PM", font=("poppins", 15, "bold"), bg="red", fg="white")
lab_such_txt.place(x=800, y=330, height=30, width=150)

lab_date = Label(clock, text="12", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_date.place(x=100, y=420, height=150, width=150)

lab_date_txt = Label(clock, text="Date", font=("poppins", 15, "bold"), bg="red", fg="white")
lab_date_txt.place(x=100, y=600, height=30, width=150)


lab_month = Label(clock, text="12", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_month.place(x=350, y=420, height=150, width=150)

lab_month_txt = Label(clock, text="Month", font=("poppins", 15, "bold"), bg="red", fg="white")
lab_month_txt.place(x=350, y=600, height=30, width=150)

lab_year = Label(clock, text="12", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_year.place(x=600, y=420, height=150, width=150)

lab_year_txt = Label(clock, text="Year", font=("poppins", 15, "bold"), bg="red", fg="white")
lab_year_txt.place(x=600, y=600, height=30, width=150)

lab_day = Label(clock, text="12", font=("poppins", 45, "bold"), bg="red", fg="white")
lab_day.place(x=800, y=420, height=150, width=150)

lab_day_txt = Label(clock, text="Day", font=("poppins", 15, "bold"), bg="red", fg="white")
lab_day_txt.place(x=800, y=600, height=30, width=150)

date_time()
clock.mainloop()

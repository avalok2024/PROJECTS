from tkinter import *
import speedtest

def speedcheck():
    spa = speedtest.Speedtest()
    spa.get_server()
    down = str(round(spa.downlaod()/(10**6), 3)) + "Mbps"
    up = str(round(spa.upload()/(10**6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)



sp = Tk()
sp.title("Internet Test")
sp.geometry("500x600")
sp.config(background="blue")

lab = Label(sp, text="Internet Speed Test", font="poppins 15 bold", background="white", foreground="red")
lab.place(x=75, y=50, height=50, width=350)

lab = Label(sp, text="Download Speed", font="poppins 15 bold", background="white", foreground="red")
lab.place(x=75, y=170, height=50, width=350)

lab_down = Label(sp, text="00", font="poppins 15 bold", background="white", foreground="red")
lab_down.place(x=75, y=240, height=50, width=350)

lab = Label(sp, text="Uploading speed", font="poppins 15 bold", background="white", foreground="red")
lab.place(x=75, y=310, height=50, width=350)

lab_up = Label(sp, text="00", font="poppins 15 bold", background="white", foreground="red")
lab_up.place(x=75, y=380, height=50, width=350)

button = Button(text="Start", font="poppins 14", background="red", foreground="white", command=speedcheck)
button.place(x=75, y=500, height=50, width=350)

sp.mainloop()

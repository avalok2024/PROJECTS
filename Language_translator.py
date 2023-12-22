from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES,Translator

def change(text = "type...", src = "English", dest = "hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text=text1, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg="red")

lab_text = Label(root, text="Translator!", font=("poppins", 20, "bold"))
lab_text.place(x=125, y=30, height=35.5, width=250)

lav_txt = Label(root, text="Source Text", font=("poppins", 14, "bold"))
lav_txt.place(x=125, y=75.5, height=30, width=250)

frame = Frame(root).pack(side=BOTTOM)

sor_txt = Text(frame, font=("poppins", 15, "bold"), wrap=WORD)
sor_txt.place(x=65, y=140, height=100.5, width=370)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, values =list_text)
comb_sor.place(x=20, y=300, height=40, width=146)
comb_sor.set("English")

button_change = Button(frame, text="Translator", relief=RAISED, command=data)
button_change.place(x=186, y=300, height=40, width=146)

comb_dest = ttk.Combobox(frame, values =list_text,)
comb_dest.place(x=352, y=300, height=40, width=146)
comb_dest.set("Hindi")

dest_txt = Text(frame, font=("poppins", 15))
dest_txt.place(x=65, y=400, height=100.5, width=370)

root.mainloop()

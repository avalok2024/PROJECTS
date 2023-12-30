import random as r
from time import *

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = 1
        except:
            error += 1
    return error

def speed(time_str, time_end, usertest):
    time_diff = time_str - time_end
    time_r = round(time_diff, 2)
    total_speed = len(usertest)/time_r
    return round(total_speed)


while True:
    chk = input("Are you ready buddy to play yes(y)/ no(n) : ")
    if chk == "y":
        test = ["I got the hell comin' your way",
        "Feelings hot to kill a top guerilla",
        "Wishin' of a riot inside my lobe",
        "Give it up to Zion, then my fire grows",
        "Spirit of a lion describes my soul"]
        test1 = r.choice(test)


        print("*******    Typing master     **********")

        print()
        print()
        print(test1)


        test_1 = time()
        testinput = input("Enter : ")
        test_2 = time()


        print(f"Speed : {speed(test_1, test_2, testinput)} w/sec")
        print(f"Error : {mistake(test1,testinput)}")
    elif chk == "n":
        print("thanks for playing the game!")
    else:
        print("invalid or wrong syntax")




from tkinter import *

typing = Tk()
typing.title("typing master for androids")

typing.geometry("1080x1920")

typing.mainloop()

from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time = time_e - time_s
    time_R = round(time, 2)
    speed = len(userinput)/ time_R
    return round(speed)


while True:
    chk = input("Are you ready yes(y) or no(n) : ")
    if chk == "yes":
        test = ["The only thing we have to fear is fear itself",
        "Well done is better than well said",
        "Spread love everywhere you go"]
        test1 = r.choice(test)

        print("     ******  Typing speed   ******")

        print(test1)
        print()
        print()

        time_1 = time()
        testinput = input(" Enter : ")
        time_2 = time()

        print("Speed : ", speed_time(time_1, time_2, testinput), "w/sec")
        print("Error : ", mistake(test1, testinput))
    elif chk == "no":
        print("thanks for interest!")
    else:
        print("Wrong or Invalid keyword")

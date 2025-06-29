from random import random
def main(y):
    if y=="n":
        num=round(random()*100)
        x=0
        while x!=num:
            x=int(input(">"))
            if x<num:
                print("Higher!")
            elif x>num:
                print("Lower!")
        print("You win!")
    elif y!="c":
        print("L for Lower, H for Higher and Y for You Win!")
        b=""
        low=0
        hi=100
        guess=50
        print(50)
        while b!="y":
            b=input("Lower or higher? ")
            if b=="h":
                low=guess
                guess=round((low+hi)/2)
            elif b=="l":
                hi=guess
                guess=round((low+hi)/2)
            print(guess)
main(input("You say the number? "))

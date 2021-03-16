def main():
    import math
    import modulcalc
    import os
    import sys

    print("*******************************************"
          "\nwelcome to our advanced calculator "
          "\naddition ===> +"
          "\nsubtraction ===> -"
          "\nmultiplication ===> *"
          "\ndivision ===> /"
          "\nlogarithms ===> log"
          "\nsquare root ===> // "
          "\nskip ===> 'q'"
          "\n*******************************************"
          )

    while True:
        opr = input("enter operation from above: ")

        if opr in ("+", "/", "*", "-", "log", "//", "q"):
            num1 = float(input("1. number: "))
            num2 = float(input("2. number: "))

            if opr == "+":
                print(num1, "+", num2, "=", modulcalc.add(num1, num2))

            elif opr == "-":
                print(num1, "-", num2, "=", modulcalc.sub(num1, num2))

            elif opr == "*":
                print(num1, "*", num2, "=", modulcalc.mult(num1, num2))

            elif opr == "/":
                print(num1, "/", num2, "=", modulcalc.div(num1, num2))

            elif opr == "log":
                print(num1, "log", num2, "=", modulcalc.log(num1, num2))

            elif opr == "//":
                print(num1, "//", num2, "=", modulcalc.sqrt(num1, num2))

            elif opr == "q" or num1 == "q" or num2 == "q":
                break
            break
        else:
            print("Invalid Input ")

    restart = input("Do you want to start again?(yes):").lower()
    if restart == "yes":
        main()


    else:
        exit()

main()
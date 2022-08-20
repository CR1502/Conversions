"""This programme uses the program Conversions.py
    as a module and to use it we have to import it as a normal module.


    This programme is a menu driven programme that has two major components
    the first component begin the base conversion part and the second
    component does the shifting operations.
"""
import Conversions

while True:
    print("Welcome to the Conversions program.")
    print("1. Base Conversions")
    print("2. Shifting operators")
    print("3. Exit")
    choice_1 = int(input("Enter a valid choice from the given list: "))

    if choice_1 == 1:
        print("1. Binary to Decimal.")
        print("2. Decimal to Binary.")
        print("3. Binary to Octal.")
        print("4. Octal to Binary.")
        print("5. Decimal to Hexadecimal.")
        print("6. Hexadecimal to Decimal.")
        print("7. Hexadecimal to Binary.")
        print("8. Binary to Hexadecimal.")
        choice_2 = int(input("Enter a valid choice from the give list: "))
        if choice_2 == 1:
            d = list(input("Enter a binary value: "))
            print("The decimal equivalent of it is: ", Conversions.bin_to_dec(d))
        elif choice_2 == 2:
            b = int(input("Enter a decimal value: "))
            print("The binary equivalent of it is: ", Conversions.dec_to_bin(b))
        elif choice_2 == 3:
            o = str(input("Enter a binary value: "))
            print("The octal equivalent of it is: ", Conversions.bin_to_oct(o))
        elif choice_2 == 4:
            b = str(input("Enter an octal value: "))
            print("The binary equivalent of it is: ", Conversions.oct_to_bin(b))
        elif choice_2 == 5:
            d = int(input("Enter a decimal value: "))
            print("The hexadecimal equivalent of it is: ", Conversions.dec_to_hex(d))
        elif choice_2 == 6:
            h = str(input("Enter a hexadecimal value: "))
            print("The decimal equivalent of it is: ", Conversions.hex_to_dec(h))
        elif choice_2 == 7:
            h = str(input("Enter a hexadecimal value: "))
            print("The binary equivalent of it is: ", Conversions.hex_to_bin(h))
        elif choice_2 == 8:
            b = str(input("Enter an binary value: "))
            print("The hexadecimal equivalent of it is: ", Conversions.bin_to_hex(b))
        else:
            print("Enter a valid choice!")

    elif choice_1 == 2:
        print("1. Left shift")
        print("2. Right shift")
        choice_3 = int(input("Enter your choice: "))

        if choice_3 == 1:
            a = int(input("Enter a decimal number: "))
            b = int(input("Enter the number of shifts to be done: "))
            print("the result after the Left Shift is completed: ", Conversions.left_shift(a, b))
        elif choice_3 == 2:
            a = int(input("Enter a decimal number: "))
            b = int(input("Enter the number of shifts to be done: "))
            print("the result after the Right Shift is completed: ", Conversions.right_shift(a, b))
        else:
            print("Enter a valid choice")

    else:
        print("Thank you for using Conversions program")
        exit()
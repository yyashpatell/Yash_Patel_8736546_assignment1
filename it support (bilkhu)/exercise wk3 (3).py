inputChar = input("please enter in either a alpha character, a digit or a space.")

if inputChar.isalpha():
    print("hey, you entered in a digit")

elif inputChar.isspace():
    print("hey, you entered in a space")

else:
    print("you entered in something totally else")
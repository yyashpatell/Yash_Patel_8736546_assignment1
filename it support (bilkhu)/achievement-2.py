x = str(input("please enter a character:"))

if((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z')):

    if (x == str.lower(x)):

        print("output is:" + str.upper(x))

    elif(x == str.upper(x)):

        print("the output is:" + str.lower(x))


else:
    print("sorry, PLEASE ENTER A CHARACTER!!!!")
    
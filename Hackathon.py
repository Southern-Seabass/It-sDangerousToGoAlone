print("Do you want to play a game?")
answer = input("Type \"yes\" here if you want to play => ")
while answer != "yes":
    print("preeeeeeeeeeety please... can you pleeeeeeeeeease type \"yes\"")
    answer = input("type your reply here => ")
if answer == "yes":
    print("")
    print("Thank you! From now on, if you need a hint, just type \"hint\"")
    print("Now try to complete my quest!")
    print("Here's my first clue that will lead you to a hidden code")
    print("if you find it, type in the anwswer below")
    print("Here's the clue: 11010010. Btw the answer will never contain capital letters.")
    code_1 = input("what's the code: ")
    while code_1 != "avocado":
        if code_1 == "210":
            print("")
            print("you're on the right track, now try to find the code. You're going to have to search the school though...")
            code_1 = input("what's the code: ") 
        elif code_1 == "hint":
            print("")
            print("roominate about it a bit")  
            code_1 = input("what's the code: ")  
        else:
            print("")
            print("incorrect")
            code_1 = input("what's the code: ")  
if code_1 == "avocado":
    print("")
    print("Allan Alcorn's inspiration is located where in the school")
    code_2 = input("what's the code: ")
    while code_2 != "bubbles":
        if code_2 == "pong":
            print("")
            print("You gotta look for it!")
            code_2 = input("what's the code: ")
        elif code_2 == "Pong":
            print("")
            print("You gotta look for it!")
        elif code_2 == "hint":
            print("")
            print("where is the ping pong table at BB&N")  
            code_2 = input("what's the code: ")  
        else:
            print("")
            print("incorrect")
            code_2 = input("what's the code: ")
if code_2 == "bubbles":
    print("")
    print("The Gaussian Integral multipled by 50, minus 7, and rounded to the nearest integer")
    code_3 = input("what's the code: ")
    while code_3 != "remedy":
        if code_3 == "vanguard":
            print("")
            print("You gotta look for it!")
            code_3 = input("what's the code: ")
        elif code_3 == "Vanguard":
            print("")
            print("You can look it up, dw looking it up is not cheating")
        elif code_3 == "hint":
            print("")
            print("You can look it up, dw looking it up is not cheating")  
            code_3 = input("what's the code: ")  
        else:
            print("")
            print("incorrect")
            code_3 = input("what's the code: ")
if code_3 == "remedy":
    print("")
    print("Here’s a poem: there's two codes to find")
    print("")
    print("In two classrooms, students spend their freetime")
    print("Partaking in academic hobbies.")
    print("The locations aren’t far from each other")
    print("They share countless commonalities")
    print("Such as Deep Blue")
    print("That is my clue")
    print("If you aren't from BB&N, just type\"skip\"")
    code_4 = input("what's the code: ")
    while code_4 != "star-struck":
        if code_4 == "hint":
            print("")
            print("They’re club rooms and my hint is a chess computer algorithm")
        elif code_4 == "skip":
            print("")
            print("Congratulations! Thank you for completing my submission despite its lack of complexity.")
            code_4 = input("what's the code: ")
        else:
            print("")
            print("incorrect")
            code_4 = input("what's the code: ")
if code_4 == "star-struck":
    print("Congratulations! Thank you for completing my submission despite its lack of complexity.")

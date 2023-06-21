answer_yes = ["Yes", "yes", "Y", "y"]
answer_no = ["No", "no", "N", "n"]

print("""
Welcome to the Adventure Game!
It is spooky Halloween night in Salem and you are out trick or treating. 
As you are walking by you find an old house.
Will you knock on the door. (Yes / No)
""")

ans1 = input("")

if ans1 in answer_yes:
    print("An old lady opens the door and asks if you are under 12")

    ans2 = input("")

    if ans2 in answer_yes:
        print("You can get a sweet! You won the game!")

    elif ans2 in answer_no:
        print("You are too old to go trick or treaing. GAME OVER!")

    else:
        print("You typed the wrong input. GOOD BYE")

elif ans1 in answer_no:
    print("A zombie starts chasing you. Will you run or knock on the door for help? (Yes / No)")

    ans3 = input("")

    if ans1 in answer_yes:
        print("Congrats! An old lady opens the door & lets you in. You are safe.")
        
    elif ans3 in answer_no:
        print("The zombie attacked you. You are dead. GAME OVER!")
            
    else:
        print("You typed the wrong input. GOOD BYE")
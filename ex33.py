def main():


    right = 'path'
    left = 'cave'

    print("What is your gender?")
    gender = input()

    print("You wake up in a forest, With nothing on you.")

    print("You see a path on your right, and a cave on your left. Which do you choose?")

    direction = input("> ")

    if direction == "right":
        print("You walk on the path, not certain of what may lie ahead.")
    else:
        print("Upon entering the cave, you see a golden sword.")

play = 'yes'
while play != "no":
    main()
    print("Do you want to play again?")
    play = input()

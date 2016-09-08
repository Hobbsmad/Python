def main():

    print("What is your name?")
    name = input()

    print("How old are you?")

    age = float(input())

    if age > 35:
        print("Time for a tombstone!")
        print("Hello, your name is %s, and you're %d years old." % (name, age))
    else:
        print("Have a nice life!")

        print("Hello, your name is %s, and you're %d years old." % (name, age))

play = 'yes'
while play != "no":
    main()
    print("Do you want to play again?")
    play = input()

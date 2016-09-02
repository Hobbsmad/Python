print("What is your name?")
name = input()


age = float(input('Age?'))

if age > 35:
    print("Time for a tombstone!")
else:
    print("Have a nice life!")

print("Hello my name is %s, and I'm %d years old." % (name, age))

print("Welcome to the fizzbuzz game!")
x=0
x = int(input("Select a number between 1 and 100"))
for x in range(1, x+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
        print(x)
print("Bye!")
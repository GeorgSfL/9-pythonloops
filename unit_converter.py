print("Dear user, the purpose of this program is to convert kilometers into miles.")
km = 0
while True:
        km = float(input("Please enter amount of km you want to convert into miles:"))
        print(km*0.6214)
        km = input("Do you you want to perform another conversion? (y/n)")
        if km == "y":
            continue
        elif km == "n":
            print("Bye!")
            break

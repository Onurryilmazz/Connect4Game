with open("Hamle.txt","r") as f:
            a = f.readlines()
            actions = a[-1]

lastAction = actions.split("-")
print(lastAction)
class Save():
    with open("save.txt", "w") as f:
        f.write("inventory")

x = None
y = None
possibleexits = None
lockedexit = None
Key1 = "key1"
Key2 = "key2"
Key3 = "key3"
inventory = []
userattemptedexit = None
gamebeat = False
def rooms():
    global x, y, possibleexits, lockedexit, Key1, Key2, Key3, inventory, userattemptedexit, gamebeat
    while not gamebeat:
        if x == None and y == None:
           x = 0
           y = 0
        #Origin:
        if x == 0 and y == 0:
            possibleexits = "Up"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None
        #Y axis
        elif x in range(0, 2) and y in range(1, 3) or x == -2 and y in range(-1, -3):
            possibleexits = "Up", "Down", "Left", "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None

        elif x in range(0, 2) and y == 3:
            possibleexits = "Down", "Left", "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None

        elif x == 3 and y == 3 or x == 2 and y == -1: #Special room
            print("Whats this? You think you see something shiny! It might be a key!")
            possibleexits = "Down", "Left"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            if userattemptedexit.lower().strip() == "grab" and Key1 not in inventory:
                inventory.append(Key1)
                print("You got key 1!\nGame Saved!")
                return inventory
                return x
                return y
            else:
                print("Nope just your imagination")

        elif x == 2 and y == 2 or x == 1 and y == 0:
            possibleexits = "Up", "Down", "Left"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None


        elif x == 2 and y == 1: #ONLY MOVING LEFT
            possibleexits = "Left", "Up"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None


        elif x == 2 and y == -3 or x == -3 and y == 1:
            possibleexits = "Down", "Up"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None


        elif x == 1 and y == -1:
            possibleexits = "Up", "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None

        elif x == -1 and y == -1:
            possibleexits = "Down", "Left"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None


        elif x == -1 and y == 1:
            possibleexits = "Up", "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None


        elif x == -1 and y == 2:
            possibleexits = "Up", "Down", "Left", "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            items = None

        elif x == -2 and y == 2:
            possibleexits = "Left", "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")

        elif x == -3 and y == 2:
            possibleexits = "Up", "Left", "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")

        elif x == -3 and y == 3:
            possibleexits = "Down"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            if userattemptedexit.lower().strip() == "grab" and Key3 not in inventory:
                inventory.append(Key3)
                print("You got key 3!\nGame Saved!")
                return inventory
                return x
                return y
            else:
                print("Nope just your imagination")


        elif x == -3 and y == 0:
            possibleexits = "Down"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")

        elif x == 1 and y == -3:
            print("You think you see something gold in the corner!")
            possibleexits = "Right"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")
            if userattemptedexit.lower().strip() == "grab" and Key2 not in inventory:
                inventory.append(Key2)
                print("You got key 2!\nGame Saved!")
                return inventory
                return x
                return y
            else:
                print("Nope just your imagination")

        elif x == 2 and y == -3:
            possibleexits = "Up", "Left"
            userattemptedexit = input(f"The possible exits are: {possibleexits}\n")

        if not userattemptedexit is None:
            gamebeat = moving(userattemptedexit.title().strip())

def moving(userattemptedexit):
    global x, y, possibleexits
    if userattemptedexit in possibleexits:
        if userattemptedexit == "Up":
            y += 1
        elif userattemptedexit == "Down":
            if x == -3 and y == 0:
                print("You have reached the final locked door...")
                if Key1 and Key2 and Key3 in inventory:
                    print("You unlock the final door! You won!")
                    return True
                else:
                    print("You don't have enough keys...")
            else:
                y -= 1
        elif userattemptedexit == "Left":
            x -= 1
        elif userattemptedexit == "Right":
            x += 1
    else:
        print("Something went wrong, try again.")
    return False

print("Welcome to Dugdon:")
a =  input("Would you like to:\nStart New Game\nLoad Game\nQuitgame\n").lower().strip()

if a in ["start", "s"]:
    print("You wake up in historic Dugdon, capital of RioShad.\nYou must escape before you use up all your oxygen.")
    rooms()
elif a in ["load", "l"]:
    print("Loading game")
    print("Jk lol, didn't figure it out")
else:
    print("Dang okay, be like that I guess.")
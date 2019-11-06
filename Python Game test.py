print("Welcome to the dungeon. There will be great challenges and bounties ahead, are you sure you want to continue?")
Choice_Start = input("Yes or No?: ")
Choice_Start = str(Choice_Start)
Life = 100
Attack = 15
Defense = 15
if(Choice_Start == str("No")):
    print("Are you kidding me? Why did you even come here then. *Grunt* I'm getting too old for this")
    exit(0)
if(Choice_Start == str("Yes")):
    print("Very well, then be on your way future hero.")
else:
        print(Choice_Start + "... Seriously? You couldn't even spell Yes correctly?")
        exit(0)
Player_Name = input("What is your name, future hero?: ")
print(Player_Name + ", That's a wonderful name! *mumbling* \x1B[3mFor someone as stupid as you...\x1B[23m")
print("*Ehm* Moving on...")
while True:
    Choice1 = input("What will you do next? (Type 'Help' if you're stuck):")
    if(Choice1 == ("Help")):
        print("List of usable commands:")
        print("Buy")
        print("Sell")
        print("Stats")
        print("Attack")
        print("Defend")
        print("Proceed")
        print("Suicide")
    if(Choice1 == ("Buy")):
        print("You can't buy here")
    if(Choice1 == ("Sell")):
        print("You can't sell your soul for anything even if you wanted to")
    if(Choice1 == ("Attack")):
        print("There's nothing to attack",Player_Name+"...")
    if(Choice1 == ("Defend")):
        print("You wanna defend against me? Fine... take this 1 damage")
        Life = Life-1
    if(Life <= 0):
        print("You died at the start of the game. Are you happy with yourself?")
        exit(0)
    if(Choice1 == ("Stats")):
        print("Your current life is:",str(Life) +", Your current Attack is:",str(Attack) +", Your current Defense is:",str(Defense))
    if(Choice1 == ("Suicide")):
        print("I knew you didn't have what it takes...")
        exit(0)
    if(Choice1 == ("Proceed")):
        break
print("You have encountered your first enemy. A slime! A classic enemy for basically every RPG ever")
print("Entity: Slime")
print("Health total: 999999999999999999")
trash_value = input("No, this can't be right %s" % (Player_Name) +", RIGHT?!")
print("Ohh, my scanner was just acting up")
print("Health total: 9")
print("\x1B[3mA cute and almost harmless slime\x1B[23m")
while True:
    Choice2 = input("")
import time 
import random
# Base Player stats
Strength = 1
HP = 100
Charisma = 1 
boarHP = 10
floatingEyeHP = 75
coins = 0

# Player Name
playerName = input("What is your adventurer's name? ")
print("So you are",playerName,"...")

# Storyline
time.sleep(1)
print("""
    In a forest long long ago""",playerName,""" was adventuring thruough a forest..."""
    )
Action = input("And you run into a wild boar. What will you do? ").lower()
how_many = int(input("How many times? "))
if Action == "attack":
    for i in range(how_many):
        print(f"The boar has {boarHP} HP")
        if boarHP <= 0:
            print("The boar is already dead")
            break
        print(f"You attacked the boar for 1HP (Attack {i+1})")
        boarHP -= 1
        print("Boar HP", boarHP) 
    if boarHP <= 0:
        print("The boar is dead")
    else:
        print(f"{playerName} left the boar at {boarHP} HP and continued on")
  
time.sleep(1)

# # Upgrading
print("After the encounter with the boar you continue on your adventure finding a witch who can increse a attribute by a random number")
Action2 = input("Which attribute do you want to increase? ").lower()

if Action2 == "strength":
    print(f"You have {Strength} Strength")
    roll = random.randint(1,5)
    print(f"you gained {roll} Strength points")
    Strength = Strength + roll
    print(f"Your new Strength is {Strength}")
elif Action2 == "hp":
    print(f"You have {HP} HP")
    roll = random.randint(25,75)
    print(f"you gained {roll} HP")
    HP = HP + roll
    print(f"Your new HP is {HP}")
elif Action2 == "charisma":
    print(f"You have {Charisma} Charisma")
    roll = random.randint(1,5)
    print(f"you gained {roll} Charisma Points")
    Charisma= Charisma + roll
    print(f"Your new Charisma is {Charisma} but why did you do this? XD")
else:
    print(f"{playerName} said who are you? And walks away")

# First turn based battle
print(""""As you walk through the forest it starts to shift into this domain and you see this floating eye""")
print("For this encounter on it will be turn based and the amount you attack is random so be prepared")
time.sleep(2)
Actino3 = input("What will you do? attack or run? (If you run now your challange ahead will be very hard) ").lower()
if Actino3 == "attack":
    how_many1 = int(input("How many times? "))
    for a in range(how_many1):
        print(f"The floating eye has {floatingEyeHP} HP")
        print(f"Your strength is {Strength}")
        roll1 = random.randint(2,74)*Strength
        print(f"You attacked the eye for {roll1}HP (Attack {a+1})")
        floatingEyeHP -= roll1 
        print(f"The floating eye has {floatingEyeHP} HP")
        time.sleep(0.5)
        floatingEyeAttack = random.randint(5,20)
        HP -= floatingEyeAttack
        print(f"The eye hit you for {floatingEyeAttack} HP")
        print(f"You have {HP} HP")
        Attackagain1 = input("Attack or Run? ").lower()
        if Attackagain1 == "attack":
            continue
        elif Attackagain1 == "run":
            print(f"{playerName} ran away safely")
            break 
        else:
            coins += random.randint(1,20)
            print(f"{playerName} left the floating eye at {floatingEyeHP} HP and gained {coins} anount of coins")
            break
            
    if floatingEyeHP <= 0:
        print("The floating eye is dead ")
    elif HP == 25:
        print("YOU ARE CRITICALLY LOW HP I ADVISE YOU RUN")
    elif HP == 0:
        print("You are dead...")
elif Actino3 == "run":
    confirm = input("Are you sure you want to leave? ").lower()
    if confirm == "yes":
        print(f"{playerName} left the domain somehow????")

# final merchant
time.sleep(2)
print(f""" As {playerName} assended from the domain with {coins} coins in their pocket they run into the traveling merchant""")
merchant = input(f"{playerName} walks towards the merchant to purchase an upgrade you can chose 2 stats to upgrade (HP always comes last) ").lower()
if merchant == "strength+hp":
    print(f"You have {Strength} Strength")
    roll = random.randint(1,5)
    print(f"you gained {roll} Strength points")
    Strength = Strength + roll
    print(f"Your new Strength is {Strength}") 
    print(f"You have {HP} HP")
    roll1 = random.randint(25,75)
    print(f"you gained {roll1} HP")
    HP = HP + roll1
    print(f"Your new HP is {HP}")
elif merchant == "charisma+hp":
    print(f"You have {Charisma} Charisma")
    roll = random.randint(1,5)
    print(f"you gained {roll} Charisma Points")
    Charisma= Charisma + roll
    print(f"You have {HP} HP")
    roll2 = random.randint(25,75)
    print(f"you gained {roll2} HP")
    HP = HP + roll2
    print(f"Your new HP is {HP}")
    print("You have to be making a troll build...")
elif merchant == "charisma+strength":
    print(f"You have {Strength} Strength")
    roll = random.randint(1,5)
    print(f"you gained {roll} Strength points")
    Strength = Strength + roll
    print(f"Your new Strength is {Strength}") 
    print(f"You have {Charisma} Charisma")
    roll1 = random.randint(1,5)
    print(f"you gained {roll1} Charisma Points")
    Charisma= Charisma + roll1
    print(f"Your new Charisma is {Charisma}") 
# final battle 
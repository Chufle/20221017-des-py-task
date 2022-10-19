
name_player1= input("enter player 1's name: ")
name_player2= input("enter player 2's name: ")

#sticks_take=int(0)
nameswitch=int(0)
sticks=13
while sticks>0:
    nameswitch += 1
    print("There are " + str(sticks) + " left")
    if not int(nameswitch % 2) == 0:
            sticks_take=int(input("How many do you take, " + name_player1 + " (between 1 and 3)"))
    else:
        sticks_take=int(input("How many do you take, " + name_player2 + " (between 1 and 3)"))
    print("switch " + str(nameswitch))
    sticks -= sticks_take
if not int(nameswitch % 2) == 0:
    print("game over, " + name_player1 + " wins")
else:
    print("game over, " + name_player2 + " wins")
from random import randint

number_of_dices=int(input("How many dice are we rolling?"))
dice_sides=int(input("How many sides on each die? "))

dice_result=[]

more=1
while not more=="q":
    for tries in range(1,number_of_dices+1):
        dice_number = randint(1,dice_sides)
        dice_result.append(int(dice_number))
    print(dice_result)
    dice_result=[]
    more=input("Roll again? ('q' for quit) ")

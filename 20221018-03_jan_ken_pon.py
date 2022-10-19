from random import randint
number_user = int(input ("1 for rock, 2 for paper, 3 for scissors. What is your choice? "))
if number_user == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""")
elif number_user == 2:
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif number_user == 3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
number_computer = int(randint(1,3))
if number_computer == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""")
elif number_computer == 2:
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif number_computer == 3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print(number_user)
print(number_computer)
if number_user == 1 and number_computer == 2 or (number_user == 2 and number_computer == 3) or (number_user == 3 and number_computer == 1):
    print("Computer wins")
elif (number_computer == 1 and number_user == 2) or (number_computer == 2 and number_user == 3) or (number_computer == 3 and number_user == 1):
    print("User wins")
elif number_user == number_computer:
    print("draw")
else:
    print("wrong input from user")

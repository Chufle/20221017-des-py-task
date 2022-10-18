# Write a script, where the user can enter a number. If the number is: 
#   - dividable by 3 print out "Fizz"
#   - dividable by 5 print out "Buzz"
#   - dividable by 3 & 5 print out "FizzBuzz"
#   - none of the above just print out the number
user_number=input("please enter a number:")
if int(user_number)%3==0  and int(user_number)%5==0 and int(user_number)%5==0:
    print("FizzBuzz")
elif int(user_number)%5==0:
    print("Buzz")
elif int(user_number)%3==0:
    print("Fizz")
else:
    print(user_number)
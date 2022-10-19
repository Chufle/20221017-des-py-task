# Write a script, where the user can enter a number. If the number is: 
#   - dividable by 3 print out "Fizz"
#   - dividable by 5 print out "Buzz"
#   - dividable by 3 & 5 print out "FizzBuzz"
#   - none of the above just print out the number


#user_number=input("please enter a number:")
for user_number in range(1,151):
    print(user_number)
    if int(user_number)%3==0  and int(user_number)%5==0 and int(user_number)%5==0:
        print("FizzBuzz")
    elif int(user_number)%5==0:
        print("Buzz")
    elif int(user_number)%3==0:
        print("Fizz")
    else:
        print("nothing")


# You can use your code from the previous FizzBuzz Task
# Create a loop to "fizzbuzz" the numbers from 1-150 (explanation is in the other task)
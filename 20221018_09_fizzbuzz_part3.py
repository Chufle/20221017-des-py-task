# Last FizzBuzz Challenge, I promise! You can use the logic from the other tasks, but if you want to train, start from scratch :)
# Write two functions:
#   - the first will fizzbuss from 1-100 without an argument
#   - the second will take one number as an argubent, to check for a fizzbuzz
#BOUNS:
#   - The function gets two argument, a starting number and a final number. Do the fizzbuzz for every number in this range.



def fizzbuzz_hundred():
    for user_number in range(1,101):
        print(user_number)
        if int(user_number)%3==0  and int(user_number)%5==0 and int(user_number)%5==0:
            print("FizzBuzz")
        elif int(user_number)%5==0:
            print("Buzz")
        elif int(user_number)%3==0:
            print("Fizz")
        else:
            print("nothing")

fizzbuzz_hundred()

def fizzbuzz_user(user_number):
    print(user_number)
    if int(user_number)%3==0  and int(user_number)%5==0 and int(user_number)%5==0:
        return("FizzBuzz")
    elif int(user_number)%5==0:
        return("Buzz")
    elif int(user_number)%3==0:
        return("Fizz")
    else:
        return("nothing")
print("#####################")
print(fizzbuzz_user(31))


def fizzbuzz_range(a,b):
    for user_number in range(a,b):
        print(user_number)
        if int(user_number)%3==0  and int(user_number)%5==0 and int(user_number)%5==0:
            print("FizzBuzz")
        elif int(user_number)%5==0:
            print("Buzz")
        elif int(user_number)%3==0:
            print("Fizz")
        else:
            print("nothing")

print("#####################")

print(fizzbuzz_range(1,31))
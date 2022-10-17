# Your own shop


#Create a file with a Python script that does the following:

#- Prints out a “banner” to welcome users to our shop
#- Asks the user for the name of the item they are buying
#- Asks the user for the price of that item
#- Asks the user for the quantity they are purchasing
#- Prints out a message that includes their subtotal (quantity 𝚡 price)

#Example output
#```
#WELCOME TO OUR USELESS STORE!
#*****************************
#what item are you purchasing?  taco
#what is the price of taco?  2.5
#how many taco are you buying?  5
 
#Added 5 taco(s) to shopping cart
#Subtotal: $12.5
#```

#- Make sure to convert user input to numbers when needed!
#- Use an f-strings when printing out the final total (goole is your friend)

from cmath import pi


print('''
WELCOME TO OUR USELESS STORE!
*****************************''')
item = input('what item are you purchasing? ')
price = input('what is the price of the ' + item + '? ')
amount = input('how many ' + item + ' are you buying? ')
subtotal = float(price) * float(amount)
print('Added ' + amount + ' ' + item +'(s) to shopping cart')
print('Subtotal: $' + str(subtotal))
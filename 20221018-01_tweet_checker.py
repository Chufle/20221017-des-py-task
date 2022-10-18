text=input("post a tweet here please:")
if len(text) < 14:  
    print("That " + str(len(text)) + " char tweet will work!")
else:
    print("**I'm sick and tired of people littering and leaving the...**")
print ("Your " + str(len(text)) + " char tweet is " + str(len(text)-14) + " chars too long")

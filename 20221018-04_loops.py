
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for printout in word:
    print(printout)
print('##################')    
# Write a while loop that does the same thing!
index_var=0
while index_var<len(word):
    print(word[index_var])
    index_var+=1

print('##################')  
#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
even_number=100
while even_number<141:
    print(even_number)
    even_number+=2


print('##################')  

# Write a for loop that does the same thing (with range())

for even_for in range(100,141,2):
    print(even_for)


print('##################')  
#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

passphrase = "ok"
while not passphrase == "sillygoose":
    passphrase=input("write sillygoose: ")
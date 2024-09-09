myAge = input("Enter age: ")
myAge = int(myAge)

if myAge >= 18:
    myComment = "You can vote."
else:
    if myAge >= 10:
        myComment = "You are in middle school."
    elif myAge >= 6:
        myComment = "You are in primary school."
    else:
        myComment = "You are too small to learn."

print("At age: " + str(myAge) + " -> " + myComment)
print("This program is written and demonstrated by Harshit Sidher (0221BCA054)")
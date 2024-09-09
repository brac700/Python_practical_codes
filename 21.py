var1 = 'a' in 'abcd' #True, since 'a' is in 'abcd'
print(var1)

var2 = 5 in [7,6,5,4] #True, since '5' is in [7,6,5,4]
print(var2)

var3 = '4' in [9,0,7,8] #False, since '4' is not in [9,0,7,8]
print(var3)

var4 = 'apple' in {'a':'apple', 'b':'boy', 'c':'cat'} #Not for value
print(var4)

print("Written and demonstrated by Harshit Sidher (0221BCA054)")
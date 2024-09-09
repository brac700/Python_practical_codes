#Python program to demonstrate equality and identicality

a = b = [1,2,3]
c = [1,2,3]
print('id(a)', id(a), 'id(b)', id(b), 'id(c)', id(c))
#id of a and b are same, but id of c is different
a is b #True
a is c #False
#a and c are different objects

print("Written and demonstrated by Harshit Sidher (0221BCA054)")
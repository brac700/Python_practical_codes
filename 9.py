#Byte example

b = bytes([65,66,67,68])
print(b)

#Accessing

print (b[0])
print(b[1])

#Iteration

for byte in b:
    print(byte, end=" ")
    print("\n")

#Bytearray example

ba = bytearray([65,66,67,68])
print(ba)

#Modifying

ba[0] = 97
print(ba)

#Element addition

ba.append(69)
print(ba)

#Converting bytearray to byte

b_converted = bytes(ba)
print(b_converted)
print("\n")

#Memory view

print("Memory view example")
b_mv = bytes([65,66,67,68])

#Creating memory view

mv = memoryview(b_mv)
print(mv)

#Accessing

mv_slice = mv[1:4]
print(mv_slice.tobytes())

#Creating bytearray and memory view

ba_mv = bytearray([65,66,67,68,69])
mv_ba = memoryview(ba_mv)

#Modifying original bytearray through memoryview

mv_ba[0] = 97
print(ba_mv)

print("\nWritten and executed by Harshit Sidher(0221BCA054)")
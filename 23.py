#input the student details
roll_no = input("Enter the roll number: ")
name = input("Enter the name: ")
student_class = input("Enter the student class: ")



#Input the marks of each subject
eng_mk = int(input("Enter the marks for English: "))
math_mk = int(input("Enter the marks for Mathematics: "))
sci_mk = int(input("Enter the marks for Science: "))
sst_mk = int(input("Enter the marks for Social Science: "))
com_mk = int(input("Enter the marks for Computers: "))


#for the sum of all marks
total = eng_mk + math_mk + sci_mk + sst_mk + com_mk
total_mk = total/5

if(total_mk >= 80):
    grade = "O"
elif(total_mk >= 70 < 80):
    grade ="A+"
elif(total_mk >= 60 < 70):
    grade = "A"
elif(total_mk >= 50 < 60):
    grade = "B"
elif(total_mk >= 40 < 50):
    grade = "C"
else:
    grade = "Fail"


#Printing out the result
print(f"----------------------------------")
print(f"Roll no: \t {roll_no} " )
print(f"Name: \t\t {name} " )
print(f"Student_class:\t{student_class}")


#Printing out the table
print(f"----------------------------------")
print(f"Subject \t Full_marks \t Obtained_marks")
print(f"English \t\t 100 \t\t {eng_mk}")
print(f"Maths \t\t\t 100 \t\t {math_mk}")
print(f"Science \t\t 100 \t\t {sci_mk}")
print(f"Social Science \t\t 100 \t\t {sst_mk}")
print(f"Computer \t\t 100 \t\t {com_mk}")
print(f"----------------------------------")
print(f"Total_marks \t\t 500 \t\t {total}")
print(f"Grade: {grade}")
print(f"Percentage: {total_mk}%")
print(f"----------------------------------")

print("Written and demonstrated by Harshit Sidher (0221BCA054)")
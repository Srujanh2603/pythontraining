#Read marks of student >80 Distinction 60 to 80 pass below 60 fail and others invalid
marks=int(input("Enter marks: "))
print(marks)
if marks>=80:
    print("Distinction")
elif marks >= 60 and marks<80:
    print("Pass")
elif marks<60:
    print("Fail")
else:
    print("Invalid")
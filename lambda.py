def sumofmarks(a,b,c):
    x=a+b+c         
    return x

stud1_maths= 90                 
stud1_science = 100
stud1_social=120

total_marks = sumofmarks(stud1_maths,stud1_science,stud1_social)
print("Result of the normal function")
print(total_marks)
tot_marks =lambda a,b,c:a+b+c
print("Result of the lambda function")
print(tot_marks(stud1_maths,stud1_science,stud1_social))
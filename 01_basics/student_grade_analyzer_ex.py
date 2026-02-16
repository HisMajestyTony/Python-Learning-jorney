students = {
    'Anna': 85,
    'Mark': 72,
    'John': 90,
    'Sophie': 60,
    'Mike': 45
}

students_passed = []
students_failed = []
grades = 0.0
counter = 0

for student in students :
    if students.get(student) >= 60 :
        students_passed.append(student)
        grades+=students.get(student)
        counter+=1
        
    else :
        students_failed.append(student)
        grades+=students.get(student)
        counter+=1
        
        

print(students_passed)
print(students_failed)
print(grades / counter)

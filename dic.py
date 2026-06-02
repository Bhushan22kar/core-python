#creating a dictionary

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

# Print dictionary values
print("Student Details")

for key, value in student.items():
    print(key, ":", value)

#using if-elif-else

student = {
    "name": "bhushan",
    "marks": 75
}

# Check grade using if elif else
if student["marks"] >= 90:
    print("Grade A")

elif student["marks"] >= 60:
    print("Grade B")

else:
    print("Grade C")

    
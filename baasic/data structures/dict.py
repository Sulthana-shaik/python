student = {
    "name": "Sadiya",
    "age": 22,
    "course": "CSE"
}

print(student)
#Accessing Values
print(student["name"])   # Ramya
print(student.get("age"))  # 22
# Adding / Updating Values
student["age"] = 23          # update
student["college"] = "ABC"   # add new key
#Keys must be unique
#Keys must be immutable (string, number, tuple)
#Values can be any type
#Dictionary is mutable (can change)
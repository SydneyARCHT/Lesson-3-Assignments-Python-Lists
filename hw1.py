#Lesson 3: Assignments | Python Lists

#1. Python List Transformation
#Task 1:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

print()
# #Task 2:

# Provided two answers because I wasn't sure if I was supposed to provide
# the decimal point or nearest to whole number :P
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grade_sum = sum(grades)
grade_length = len(grades)
grade_average = grade_sum / grade_length
print(grade_average)

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grade_sum = sum(grades)
grade_length = len(grades)
grade_average = grade_sum // grade_length
print(grade_average)


# print()

# #2. Advanced Slicing Techniques
# #Task 1:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14:])

# print()

# #Task 2:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[23::])

# print()

# #Task 3:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[6:12:])


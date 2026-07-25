import numpy as np

# Starter Code
marks = np.array([75, 82, 90, 68, 55, 79, 88, 95, 60, 72])

# 1. Display the Marks

print("1. Complete Marks Array")
print(marks)

# 2. Check Array Properties

print("\n2. Array Properties")
print("Number of Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Data Type:", marks.dtype)

# 3. Indexing & Slicing

print("\n3. Indexing & Slicing")
print("First Student Marks:", marks[0])
print("Last Student Marks:", marks[-1])
print("Marks from Index 2 to 6:", marks[2:7])
print("First Five Students Marks:", marks[:5])


# 4. Reshape the Array

marks_matrix = marks.reshape(2, 5)

print("\n4. Reshaped Array (2 x 5)")
print(marks_matrix)


# 5. Arithmetic Operations

grace_marks = marks + 5
double_marks = marks * 2

print("\n5. Arithmetic Operations")
print("Marks after Adding 5 Grace Marks:")
print(grace_marks)

print("\nMarks after Multiplying by 2:")
print(double_marks)

# 6. Aggregate Functions

print("\n6. Aggregate Functions")
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))


# 7. Boolean Indexing

print("\n7. Boolean Indexing")

print("Students Scoring Above 80:")
print(marks[marks > 80])

print("Students Scoring Below 70:")
print(marks[marks < 70])


# 8. Matrix Operations

print("\n8. Matrix Transpose")
print(marks_matrix.T)


# 9. Random Numbers

new_marks = np.random.randint(50, 101, 5)

print("\n9. Random Marks for 5 New Students")
print(new_marks)


# 10. Bonus Challenge

print("\n10. Bonus Challenge")

print("Students Scoring Above 75:", np.sum(marks > 75))

print("Students Failed (Below 35):", np.sum(marks < 35))

print("Topper's Marks:", np.max(marks))

print("Average of Students Scoring Above 70:",
      np.mean(marks[marks > 70]))

updated_marks = marks.copy()
updated_marks[updated_marks < 60] = 60
print("\nMarks After Replacing Below 60 with 60:")
print(updated_marks)

print("\nMarks Sorted in Ascending Order:")
print(np.sort(marks))
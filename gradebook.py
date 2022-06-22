# Old gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# New gradebook
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

# Add compsci score
gradebook.append(["computer science", 100])
print(gradebook)

# Add visual arts score
gradebook.append(["visual arts", 93])
print(gradebook)

# Add 5 points to visual arts score
gradebook[-1][-1] = 98
print(gradebook)

# Make poetry pass/fail using methods
gradebook[2].remove(85)
gradebook[2].append("Pass") 
print(gradebook)

# Combine old and new gradebooks
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

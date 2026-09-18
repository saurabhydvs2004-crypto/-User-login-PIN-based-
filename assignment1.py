def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(num_subjects):
    score = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(score)

average = sum(marks) / len(marks)
grade = calculate_grade(average)

print(f"\nAverage Marks: {average:.2f}")
print(f"Assigned Grade: {grade}")
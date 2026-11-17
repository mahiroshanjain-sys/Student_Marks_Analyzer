import csv
import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "English", "Physics", "Chemistry"]
students = []

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

# 1. Read data from students.csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the first header row
    for row in reader:
        if row:
            name = row[0]
            marks = [float(score) for score in row[1:6]]
            total = sum(marks)
            percentage = round(total / 5, 2)
            grade = get_grade(percentage)
            students.append({
                "name": name,
                "marks": marks,
                "total": total,
                "percentage": percentage,
                "grade": grade
            })

# 2. Print student report and topper in terminal
print("===== STUDENT MARKS REPORT =====")
for student in students:
    print(f"{student['name']} | Total: {student['total']} | Percentage: {student['percentage']}% | Grade: {student['grade']}")

topper = max(students, key=lambda student: student["percentage"])
print(f"\nTopper: {topper['name']} with {topper['percentage']}% (Grade {topper['grade']})")

# 3. Prepare data for Matplotlib dashboard
names = [student["name"] for student in students]
percentages = [student["percentage"] for student in students]

subject_averages = []
for i in range(5):
    average = sum(student["marks"][i] for student in students) / len(students)
    subject_averages.append(average)

# 4. Create and show the dashboard
figure, (chart1, chart2) = plt.subplots(1, 2, figsize=(14, 5))
figure.suptitle("Student Marks Dashboard", fontsize=14, fontweight="bold")

# Left Chart: Each Student's Percentage
chart1.bar(names, percentages, color="skyblue")
chart1.set_title("Student Percentages")
chart1.set_ylabel("Percentage (%)")
chart1.set_ylim(0, 100)
chart1.tick_params(axis="x", rotation=90)

# Right Chart: Class Average per Subject
chart2.bar(subjects, subject_averages, color="lightgreen")
chart2.set_title("Subject Averages")
chart2.set_ylabel("Average Marks")
chart2.set_ylim(0, 100)

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

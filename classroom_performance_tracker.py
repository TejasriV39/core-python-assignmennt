class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

def calculate_performance(students):
    averages = {name: student.average_marks() for name, student in students.items()}
    top_performer = max(averages, key=averages.get)
    return averages, top_performer

#input
students = {}
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    name = input("Enter student name: ")
    marks = list(map(float, input(f"Enter marks for {name} separated by spaces: ").split()))
    students[name] = Student(name, marks)

averages, top_performer = calculate_performance(students)
print(f"Average Marks: {averages}")
print(f"Top Performer: {top_performer}")
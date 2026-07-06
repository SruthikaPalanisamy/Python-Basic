class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}   # Dictionary to store subject and score

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def report(self):
        print("----- Student Report Card -----")
        print("Name:", self.name)
        print("Student ID:", self.student_id)

        print("\nSubjects and Scores:")
        for subject, score in self.grades.items():
            print(f"{subject}: {score}")

        print(f"\nAverage Score: {self.get_average():.2f}")


# Driver Code
s1 = Student("Sruthika", 101)

s1.add_grade("Math", 95)
s1.add_grade("Science", 88)
s1.add_grade("English", 92)

s1.report()
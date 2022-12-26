class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Classroom:
    def __init__(self, students):
        self.students = students

    def find_average(self):
        total_score = 0
        for student in self.students:
            total_score += student.score
        return total_score / len(self.students)

    def find_median(self):
        scores = []
        for student in self.students:
            scores.append(student.score)
        scores.sort()
        median_index = len(scores) // 2
        median = scores[median_index]
        students_with_median = []
        for student in self.students:
            if student.score == median:
                students_with_median.append(student.name)
        return median, students_with_median[0]


student1 = Student("Alice", 80)
student2 = Student("Bob", 90)
student3 = Student("Charlie", 70)
classroom = Classroom([student1, student2, student3])

average = classroom.find_average()
median = classroom.find_median()

print(f"Average score: {average}")
print(f"Median score: {median[0]} ({median[1]})")

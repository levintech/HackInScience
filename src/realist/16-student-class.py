class Student:
    
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_exam(self, grade):
        self.grades.append(grade)
    
    def get_mean(self) -> float:
        return sum(self.grades) / len(self.grades)

class School:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def get_mean(self) -> float:
        return sum([student.get_mean() for student in self.students]) / len(self.students)
    
    def get_best_student(self) -> Student:
        return sorted(self.students, key=lambda x: x.get_mean(), reverse=True)[0]

class City:

    def __init__(self, name):
        self.name = name
        self.schools = []
    
    def add_school(self, school: School):
        self.schools.append(school)

    def get_mean(self) -> float:
        return sum([school.get_mean() for school in self.schools]) / len(self.schools)

    def get_best_school(self) -> School:
        return sorted(self.schools, key=lambda x: x.get_mean(), reverse=True)[0]
    
    def get_best_student(self) -> Student:
        return sorted([school.get_best_student() for school in self.schools], key=lambda x: x.get_mean(), reverse=True)[0]
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def average_rate_lecturer(self):
        for key, value in cool_lecturer.grades:

        return

    def __str__(self):
        res = f'Имя: {cool_lecturer.name}\nФамилия: {cool_lecturer.surname}\nСредняя оценка за лекцию:{Lecturer.average_rate_lecturer(cool_lecturer)}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}'
        return res
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)

print(f'Оценка лучшего студента:{best_student.name} {best_student.surname}\n {best_student.grades}')

cool_lecturer = Lecturer('Harry', 'Kane')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Java', 9)

print(f'Оценка лектора: {cool_lecturer.name} {cool_lecturer.surname}\n {cool_lecturer.grades}')
print(cool_reviewer)
print(cool_lecturer)
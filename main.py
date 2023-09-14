class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grad = ()
        self.total = ()

    def rate_work_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return ('Ошибка')
    def average_score_student(self,student):
        if isinstance(student, Student):
            len = 0
            sum = 0
            for row in list(self.grades.values()):
                for num in row:
                    len += 1
                    sum += num
            student.total = sum/len
        else:
            'Error'

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.total}\n'
               f'Курсы в процессе изучения:{self.courses_in_progress}\n'
               f'Завершенные курсы:{self.finished_courses}\n')
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.total = ()

class Lecturer(Mentor):
    def average_score_lector(self,lecturer):
        if isinstance(lecturer, Lecturer):
            len = 0
            sum = 0
            for row in list(self.grades.values()):
                for num in row:
                    len += 1
                    sum += num
            lecturer.total = sum/len
        else:
            'Error'

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.total}\n')
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
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n')
        return res



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Знакомство с IT']



some_lecturer = Lecturer('name Lecturer', 'surname Lecture')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
# Оценки Лектору от Студента
best_student.rate_work_lect(some_lecturer, 'Python', 10)
best_student.rate_work_lect(some_lecturer, 'Git', 8)


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
# Оценки Студенту от Рецензира
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 10)
some_reviewer.rate_hw(best_student, 'Python', 8)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)

# Подсчет средней Оценки у Студента
best_student.average_score_student(best_student)
# Подсчет средней Оценки у Лектора
some_lecturer.average_score_lector(some_lecturer)

print(best_student)
print(some_lecturer)
print(some_reviewer)
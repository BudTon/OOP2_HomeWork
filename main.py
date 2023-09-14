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
            student.total = round(sum/len,1)
        else:
            'Error'

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.total}\n'
               f'Курсы в процессе изучения:{self.courses_in_progress}\n'
               f'Завершенные курсы:{self.finished_courses}\n')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        if int(self.total < other.total) == 0:
            return f'Средний балл у Студента {self.name} {self.surname} больше чем у Студента {other.name} {other.surname}\n'
        else:
            return f'Средний балл у Студента {other.name} {other.surname} больше чем у Студента {self.name} {self.surname}\n'

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
            lecturer.total = round(sum/len,1)
            'Error'

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.total}\n')
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        if int(self.total < other.total) == 0:
            return f'Средний балл у Лектора {self.name} {self.surname} больше чем у Лектора {other.name} {other.surname}\n'
        else:
            return f'Средний балл у Лектора {other.name} {other.surname} больше чем у Лектора {self.name} {self.surname}\n'



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


# СТУДЕНТЫ
student1 = Student('Максим', 'Федоров', 'мужской')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Знакомство с IT']

student2 = Student('Ксения', 'Гусева', 'женский')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Знакомство с IT']


# ЛЕКТОРЫ
lecturer1 = Lecturer('Елена', 'Никитина')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Олег', 'Булыгин')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

# Оценки Лектору от Студента
student1.rate_work_lect(lecturer1, 'Python', 5)
student1.rate_work_lect(lecturer1, 'Python', 9)
student1.rate_work_lect(lecturer1, 'Python', 8)
student2.rate_work_lect(lecturer2, 'Git', 8)
student2.rate_work_lect(lecturer2, 'Git', 9)
student2.rate_work_lect(lecturer2, 'Git', 8)

# РЕЦЕНЗЕНТ
reviewer1 = Reviewer('Александр', 'Бардин')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Алёна', 'Батицкая')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

# Оценки Студенту от Рецензера
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Git', 5)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer1.rate_hw(student1, 'Python', 3)
reviewer1.rate_hw(student1, 'Python', 4)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Git', 6)
reviewer1.rate_hw(student2, 'Git', 8)
reviewer1.rate_hw(student2, 'Python', 3)
reviewer1.rate_hw(student2, 'Python', 5)

reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student1, 'Git', 4)
reviewer2.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student1, 'Python', 4)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Git', 6)
reviewer2.rate_hw(student2, 'Git', 7)
reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Python', 9)

# Подсчет средней Оценки у Студента
student1.average_score_student(student1)
student2.average_score_student(student2)

# Подсчет средней Оценки у Лектора
lecturer1.average_score_lector(lecturer1)
lecturer2.average_score_lector(lecturer2)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(student1.__lt__(student2))
print(lecturer2.__lt__(lecturer1))
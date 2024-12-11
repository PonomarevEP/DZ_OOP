class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result_list = []
        for k, v in self.grades.items():
            result_list.append(sum(v) / len(v))
        result_list = sum(result_list) / len(result_list)
        list_of_courses = ", ".join(self.courses_in_progress)
        list_of_finished_courses = ", ".join(self.finished_courses) 
        return f"""Имя: {self.name} \nФамилия: {self.surname} 
Средняя оценка за домашние задания: {result_list} 
Курсы в процессе изучения: {list_of_courses} 
Курсы завершенные: {list_of_finished_courses}"""

    def rate_lecture(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.assessment_for_lectures:
                    lecturer.assessment_for_lectures[course] += [grade]
                else:
                    lecturer.assessment_for_lectures[course] = [grade]
            else:
                return 'Ошибка'
            
    def show_rating_students(self):
        result_list = []
        for k, v in self.grades.items():
            result_list.append(sum(v) / len(v))
        result_list = sum(result_list) / len(result_list)
        return result_list
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    assessment_for_lectures = {}

    def __str__(self):
        result_list = []
        for k, v in self.assessment_for_lectures.items():
            result_list.append(sum(v) / len(v))
        result_number = sum(result_list) / len(result_list)

        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {result_number}'

    def add_grade(self, reviewer, grade):
        if isinstance(reviewer, Reviewer):
            self.assessment_for_lectures += grade

    def show_rating(self):
        result_list = []
        for k, v in self.assessment_for_lectures.items():
            result_list.append(sum(v) / len(v))
        result_number = sum(result_list) / len(result_list)
        return result_number


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
            
def students_reating(students_list, string):
    result_list = []

    for student in students_list:
        for k, v in student.grades.items():
            if k == string:
                result_list.append(sum(v) / len(v))
    result_list = sum(result_list) / len(result_list)   
    return result_list

def lecturers_reating(lecturers_list, string):
    result_list = []

    for student in lecturers_list:
        for k, v in student.assessment_for_lectures.items():
            if k == string:
                result_list.append(sum(v) / len(v))
    result_list = sum(result_list) / len(result_list)   
    return result_list
    
 

best_student = Student('Ruoy', 'Eman', 'men')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Rubi', 'Royse', 'women')
best_student2.courses_in_progress += ['Git']

# Как понял менторов объявлять не нужно, но сделал на всякий случай 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Mentor('Ilya', 'Poperechnii')
cool_mentor2.courses_attached += ['Git']

# Задание 1. Наследование
some_lecturer = Lecturer('Vasya', 'Pupkin')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_lecturer2= Lecturer('Nikita', 'Vsevolod')
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Git']

some_reviewer = Reviewer('Sasha', 'Mishutkin')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer2 = Reviewer('Misha', 'Sashutkin')
some_reviewer2.courses_attached += ['Git']

# Задание 2. Атрибуты и взаимодействие классов
best_student.rate_lecture(some_lecturer, 'Python', 8)
best_student.rate_lecture(some_lecturer, 'Python', 10)
best_student.rate_lecture(some_lecturer, 'Python', 10)
best_student.rate_lecture(some_lecturer, 'Git', 8)
best_student.rate_lecture(some_lecturer, 'Git', 7)
best_student.rate_lecture(some_lecturer2, 'Python', 3)
best_student.rate_lecture(some_lecturer2, 'Python', 2)
best_student.rate_lecture(some_lecturer2, 'Python', 5) 

 
print(some_lecturer.assessment_for_lectures)
 
some_reviewer.rate_hw(best_student, 'Python', 7)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 9)
some_reviewer.rate_hw(best_student, 'Git', 10)
some_reviewer.rate_hw(best_student, 'Git', 8)
some_reviewer2.rate_hw(best_student2, 'Git', 8)
some_reviewer2.rate_hw(best_student2, 'Git', 3)
some_reviewer2.rate_hw(best_student2, 'Git', 6)
 
print(best_student.grades)

# Задание 3.1 Полиморфизм
print(some_reviewer)
print(some_lecturer)
print(best_student)

# Задание 3.2 Полиморфизм
print(some_lecturer.show_rating() == some_lecturer2.show_rating())
print(best_student.show_rating_students() == best_student2.show_rating_students())

# Задание 4.1 Полевые испытания 
print(students_reating([best_student, best_student2], "Git"))

# Задание 4.2 Полевые испытания
print(lecturers_reating([some_lecturer, some_lecturer2], "Python"))

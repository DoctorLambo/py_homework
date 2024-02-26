class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):

        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        return str(f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}\n'
                   f'Курсы в процессе изучения: {courses_in_progress}\n'
                   f'Завершенные курсы:{finished_courses}')

    def rate_lecture(self, lecture, course, grade):

        has_error = False
        if not 1 <= grade <= 10:
            print(
                f'Оценивать лектора можно по десятибальной шкале. Ваша оценка: {grade}')
            has_error = True

        if not course in self.courses_in_progress and not course in self.finished_courses:
            print(f'Вы не закреплены за курсом "{course}"')
            has_error = True

        if not isinstance(lecture, Lecturer):
            print(f'Оценивать можно только лектора')
            has_error = True

        if not course in lecture.courses_attached:
            print(f'Лектор "{lecture.name} {
                  lecture.surname}" не читает данный курс')
            has_error = True

        if has_error:
            return 'Ошибка'

        if course in lecture.grades:
            lecture.grades[course].append(grade)
        else:
            lecture.grades[course] = [grade]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        pass

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = dict()

    def __str__(self):
        sum_grade = 0
        len_grade = 0
        for course in self.grades:
            list_grades = self.grades[course]
            sum_grade += sum(list_grades)
            len_grade += len(list_grades)

        average_grade = sum_grade / len_grade

        # average_grade = sum(self.)
        return str(f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}\n'
                   f'Средняя оценка за лекции: {average_grade}')

    def rate_hw(self, student, course, grade):
        print('Лекторы не могут выставлять оценки')
        return 'Ошибка'


class Reviewer(Mentor):

    def __str__(self):
        return str(f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}')


best_student = Student('Ivanov', 'Ivan', 'man')
best_student.courses_in_progress += ['Python']

cool_lecture = Lecturer('Mr', 'Lecture')
cool_lecture.courses_attached += ['Python']

cool_mentor = Reviewer('Mr', 'Reviewer')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'Python', 10)

best_student.rate_lecture(cool_mentor, 'Python1', 100)
print('--------------------')
print(cool_lecture)
print('--------------------')
print(cool_mentor)
print('--------------------')
print(best_student)
print('--------------------')

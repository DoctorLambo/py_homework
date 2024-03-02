class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
        self.grades_average_grade = {}

    def __str__(self):

        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        return str(f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}\n'
                   f'Курсы в процессе изучения: {courses_in_progress}\n'
                   f'Завершенные курсы:{finished_courses}')

    def __eq__(self, person: object):
        if isinstance(person, Student):
            return self.average_grade == person.average_grade

    def __lt__(self, person: object):
        if isinstance(person, Student):
            return self.average_grade < person.average_grade

    def __gt__(self, person: object):
        if isinstance(person, Student):
            return self.average_grade > person.average_grade

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

        lecture.get_average_grade(course)

    def count_average_grade(self, course):
        list_grades = self.grades[course]
        sum_grade = sum(list_grades)
        len_grade = len(list_grades)
        grade = sum_grade / len_grade
        if course in self.grades_average_grade:
            self.grades_average_grade[course].append(grade)
        else:
            self.grades_average_grade[course] = [grade]

    def get_average_grade(self, course=''):

        if course == '':
            for course in self.grades:
                self.count_average_grade(course)
        elif course in self.grades:
            self.count_average_grade(course)
        else:
            print(f'У студента ещё нет оценок за курс {course}')
            return 'Предупреждение'
        self.calculate_total_average()

    def calculate_total_average(self):
        sum_grade = 0
        len_grade = 0
        for course in self.grades_average_grade:
            list_grades = self.grades_average_grade[course]
            sum_grade += sum(list_grades)
            len_grade += len(list_grades)
        self.average_grade = sum_grade / len_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        pass

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            return 'Ошибка'

        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
        student.get_average_grade(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = dict()
        self.average_grade = 0
        self.grades_average_grade = {}

    def __str__(self):
        # average_grade = sum(self.)
        return str(f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}\n'
                   f'Средняя оценка за лекции: {self.average_grade}')

    def __eq__(self, person: object):
        if isinstance(person, Lecturer):
            return self.average_grade == person.average_grade

    def __lt__(self, person: object):
        if isinstance(person, Lecturer):
            return self.average_grade < person.average_grade

    def __gt__(self, person: object):
        if isinstance(person, Lecturer):
            return self.average_grade > person.average_grade

    def rate_hw(self, student, course, grade):
        print('Лекторы не могут выставлять оценки')
        return 'Ошибка'

    def count_average_grade(self, course):
        list_grades = self.grades[course]
        sum_grade = sum(list_grades)
        len_grade = len(list_grades)
        grade = sum_grade / len_grade
        if course in self.grades_average_grade:
            self.grades_average_grade[course].append(grade)
        else:
            self.grades_average_grade[course] = [grade]

    def get_average_grade(self, course=''):

        if course == '':
            for course in self.grades:
                self.count_average_grade(course)
        elif course in self.grades:
            self.count_average_grade(course)
        else:
            print(f'У лектора ещё нет оценок за курс {course}')
            return 'Предупреждение'

        self.calculate_total_average()

    def calculate_total_average(self):
        sum_grade = 0
        len_grade = 0
        for course in self.grades_average_grade:
            list_grades = self.grades_average_grade[course]
            sum_grade += sum(list_grades)
            len_grade += len(list_grades)
        self.average_grade = sum_grade / len_grade


class Reviewer(Mentor):

    def __str__(self):
        return str(f'Имя: {self.name}\n'
                   f'Фамилия: {self.surname}')


def count_list_averege(list_count, couse=''):
    for person in list_count:
        person.get_average_grade(couse)


best_student = Student('Ivanov', 'Ivan', 'man')
best_student.courses_in_progress += ['Python']

best_student2 = Student('Petrov', 'Petr', 'man')
best_student2.courses_in_progress += ['Python']

cool_lecture = Lecturer('Mr', 'Lecture')
cool_lecture.courses_attached += ['Python']

cool_lecture2 = Lecturer('Mr', 'Lecture2')
cool_lecture2.courses_attached += ['Python']

cool_mentor = Reviewer('Mr', 'Reviewer')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 10)

best_student.rate_lecture(cool_lecture, 'Python', 10)
best_student.rate_lecture(cool_lecture, 'Python', 10)

best_student2.rate_lecture(cool_lecture2, 'Python', 9)
best_student2.rate_lecture(cool_lecture2, 'Python', 10)

list_person = [best_student, best_student2]


best_student.rate_lecture(cool_mentor, 'Python1', 100)
print('--------------------')
print(cool_lecture)
print('--------------------')
print(cool_lecture2)
print('--------------------')
print(cool_mentor)
print('--------------------')
print(best_student)
print('--------------------')
print(best_student2)
print('--------------------')

if best_student == best_student2:
    sign = '='
elif best_student < best_student2:
    sign = '<'
elif best_student > best_student2:
    sign = '>'
else:
    sign = 'undefinit'

print(f'{best_student.surname} {best_student.name} {
      sign} {best_student2.surname} {best_student2.name}')

if cool_lecture == cool_lecture2:
    sign = '='
elif cool_lecture < cool_lecture2:
    sign = '<'
elif cool_lecture > cool_lecture2:
    sign = '>'
else:
    sign = 'undefinit'

print(f'{cool_lecture.surname} {cool_lecture.name} {
      sign} {cool_lecture2.surname} {cool_lecture2.name}')

count_list_averege([cool_lecture, cool_lecture2], 'Python')
count_list_averege([best_student, best_student2], 'Python2')

from random import randint
from typing import Optional


def generate_student_id():
    return randint(10, 100000)


class Student:
    def __init__(self, name: str, age: int, program: str, student_id: Optional[int] = None):
        self.name = name
        self.age = age
        self.program = program
        self.student_id = student_id if student_id is not None else generate_student_id()

    def study_program(self):  # method
        return f'{self.name} is studying {self.program}'

    def increase_age(self):
        self.age += 1


class MasterStudent(Student):
    def __init__(self, name: str, age: int, program: str, topic: str, student_id: Optional[int] = None):
        super().__init__(name, age, program, student_id)
        self.thesis_topic = topic

    def master_thesis_topic_is(self):
        return f'Student {self.name} writes Master Degree project on the topic {self.thesis_topic}'


student_1 = Student('Mike', 23, 'Chemistry')
student_2 = Student('Jane', 25, 'Philosophy')
student_3 = MasterStudent('Alex', 25, 'Chemistry', 'Photosynthesis', 64)
# print(student_1.study_program())
# print(student_1.age)
# student_1.increase_age()
# print(student_1.age)
print(student_1.student_id)
print(student_2.student_id)
print(student_3.student_id, student_3.thesis_topic)
print(student_3.master_thesis_topic_is())
print(student_2.master_thesis_topic_is())
print(student_3.study_program())

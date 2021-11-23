class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50: return True
        else: return False


student_1 = Student('Adam',64)
student_2 = Student('Jan',31)

student_1.is_passed()
student_2.is_passed()
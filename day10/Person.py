class Human:
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return "name: %s age: %d sex: %s" % (self.name, self.age, self.sex)


class Student(Human):
    def __init__(self, name, age, sex, number, grade) -> None:
        super().__init__(name, age, sex)
        self.number = number
        self.grade = grade

    def __str__(self) -> str:
        return super().__str__() + " number: %d grade: %s" % (self.number, self.grade)


if __name__ == '__main__':
    student1 = Student('John', 18, '男', 1, '一年級')
    student2 = Student('Mary', 19, '女', 2, '二年級')
    student3 = Student('Bobo', 20, '女', 3, '三年級')

    students = [student1, student2, student3]

    for student in students:
        print(student.name, student.age)

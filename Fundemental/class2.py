from class1 import Person

class Student(Person):
    def __init__(self,name,age,gender):
        super().__init__(name, age, gender)

p1 = Student("Jen",22,'male')
print("Name",p1.name)
print("Age",p1.age)
print("Gender",p1.gender)


#Parent
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    pass


class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = 'I am a parent'


# Create instance of child
child = Child()

# Show attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()
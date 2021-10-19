class ParentClass:
    def __init__(self):
        self.a = 1
        print("Parent Class Object Created")
    def someMethod(self):
        print("Hello")

class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Object Created")

parent = ParentClass()
child = ChildClass()

print(isinstance(parent, ParentClass))
print(isinstance(5, int))
print(isinstance(child, ParentClass))
print(isinstance(parent, (ParentClass, int)))
print(isinstance(parent, ChildClass))
try:
    print(isinstance(parent, MyClass))
except NameError:
    print("No such class")

print(issubclass(ChildClass, ParentClass))
print(issubclass(ParentClass, ParentClass))
print(issubclass(ChildClass, int))
print(issubclass(ChildClass, (ParentClass, int)))

print(hasattr(parent, 'a'))
print(hasattr(parent, 'someMethod'))
print(hasattr(parent, 'b'))
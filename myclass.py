class SomeClass:
    def __init__(self, position=''):
        self._position = position
        print("This is SomeClass")
    def someMethod(self, a):
        print('The value of a is', a)
        self.b = 5
    @property
    def position(self):
        print("Getter method")
        return self._position
    @position.setter
    def position(self, value):
        print("Setter method")
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No change made.')

class SomeOtherClass:
    def __init__(self):
        print('This is SomeOtherClass')
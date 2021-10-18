import myclass

sc = myclass.SomeClass()
sc.someMethod(100)
print('Position 1', sc.position)
sc.position = 'Basic'
print('Position 2', sc.position)
sc.position = 'One'
print('Position 3', sc.position)
soc = myclass.SomeOtherClass()
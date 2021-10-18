class Methoddemo:

    a = 1

    @classmethod
    def classM(cls):
        print("Class Method. cls.a = ", cls.a)

    @staticmethod
    def staticM():
        print("Static method")

Methoddemo.classM()
md1 = Methoddemo()
md1.classM()

md1.staticM()
Methoddemo.staticM()
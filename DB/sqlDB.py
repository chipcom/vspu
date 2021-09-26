file_DB = 'learn.db'

class Sql_db:
    """Данный класс позволяет создавать SQL соединение для файла БД"""
    count = 0

    def __new__(cls, *args, **kwargs):
        # print("__new__ called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name = None, driver =None)->None:
        # print("__init__ called")
        self.name = name or "learn.db"
        self.driver = driver or "sqlite3"
        Sql_db.count += 1

    def __del__(self):
        # print("__del__ called")
        Sql_db.count -= 1

    def __str__(self) -> str:
        return f"База данных: {self.name}, драйвер: {self.driver}"

    def __repr__(self) -> str:
        return f"База данных: {self.name}, драйвер: {self.driver}"

# print(Sql_db)
# print(dir(Sql_db))
# print(Sql_db.__doc__)

# obj = Sql_db()
# print(obj.name)
# print(obj.__doc__)
# obj = Sql_db("competence.db", "MySQL")
# print(obj.name)
# print(obj)

# print(Sql_db.count)
# print(obj.__dict__)
# del obj
# print(Sql_db.count)

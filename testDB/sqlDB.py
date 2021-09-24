import sqlite3

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

file_DB = 'learn.db'
str_error = "An error occurred:"

def get_module_by_id(id):
    """возвращает модуль по переданному ID"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM modules WHERE ModuleID = ?", (id, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_module_by_code(code):
    """возвращает модуль по переданному коду"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM modules WHERE ModuleCode = ?", (code, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_subject_by_id(id):
    """возвращает дисциплину по переданному ID"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE SubjectID = ?", (id, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_subject_by_code(code):
    """возвращает дисциплину по переданному коду"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE SubjectCode = ?", (code, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_competence_by_id(id):
    """возвращает компетенцию по переданному ID"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM competences WHERE CompetenceID = ?", (id, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_competence_by_code(code):
    """возвращает компетенцию по переданному коду"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM competences WHERE CompetenceCode = ?", (code, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_indicator_by_id(id):
    """возвращает идикатор компетенции по переданному ID"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE IndicatorID = ?", (id, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_indicator_by_code(code):
    """возвращает идикатор компетенции по переданному коду"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE IndicatorCode = ?", (code, ))
        ret = c.fetchone()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_list_subjects_module_by_id_module(id):
    """возвращает список дисциплин модуля по переданному ID модуля"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE ModuleID = ?", (id, ))
        ret = c.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_list_subjects_module_by_code_module(code):
    """возвращает список дисциплин модуля по переданному коду модуля"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE ModuleID = (SELECT ModuleID FROM modules WHERE ModuleCode = ?)", (code, ))
        ret = c.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_list_indicators_by_id_competence(id):
    """возвращает список индикаторов компетенции по переданному ID компетенции"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE CompetenceID = ?", (id, ))
        ret = c.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

def get_list_indicators_by_code_competence(code):
    """возвращает список индикаторов компетенции по переданному коду компетенции"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE CompetenceID = (SELECT CompetenceID FROM competences WHERE CompetenceCode = ?)", (code, ))
        ret = c.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print(str_error, e.ar)
    return ret

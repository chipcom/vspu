import sqlite3
from sqlite3 import Error
from .program import Program

from . import file_DB

class open_db:  # rонтекстный менеджер
    def __init__(self, name):
        self.f = sqlite3.connect(name)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()

def fill_array(array):
    ret = []
    for record in array:
        ret.append(Program(record[0], record[1], record[2], record[3]))
    return ret

def get_by_id(id):
    """возвращает учебную программу по переданному ID"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            sqlite_query = "SELECT ID, Code, Name, Level FROM programs WHERE ID = ?"
            c.execute(sqlite_query, (id, ))
            ret_fetch = c.fetchone()
            if not ret_fetch == None:
                return Program(
                    id = ret_fetch[0],
                    code = ret_fetch[1],
                    name = ret_fetch[2],
                    level = ret_fetch[3]
                    )
            else:
                return None
    except Error:
        print(Error)

def get_by_code(code):
    """возвращает учебную программу по переданному коду"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            sqlite_query = "SELECT ID, Code, Name, Level FROM programs WHERE Code = ?"
            c.execute(sqlite_query, (code.upper(), ))
            ret_fetch = c.fetchone()
            if not ret_fetch == None:
                return Program(
                    id = ret_fetch[0],
                    code = ret_fetch[1],
                    name = ret_fetch[2],
                    level = ret_fetch[3]
                    )
            else:
                return None
    except Error:
        print(Error)

def add(obj):
    """добавляет учебную программу в БД"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            sqlite_query = "INSERT INTO programs(Code, Name, Level) VALUES (?, ?, ?)"
            c.execute(sqlite_query, (obj.code,obj.name,obj.level))
            conn.commit()
            return True
    except Error:
        print(Error)
        return False

def delete_by_id(obj):
    """удаляет учебную программу из БД"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON") # Внешние ключи SQLite отключены в целях совместимости. Их нужно включать вручную сразу после каждого подключения к базе данных.
            sqlite_query = """DELETE FROM programs WHERE ID = ?"""
            c.execute(sqlite_query, (obj.id, ))
            conn.commit()
            return True
    except Error:
        print(Error)
        return False

def update(obj):
    """обновляет учебную программу в БД"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            sqlite_query = """UPDATE programs SET Code = ?, Name = ?, Level = ? WHERE ID = ?"""
            c.execute(sqlite_query, (obj.code, obj.name, obj.level, obj.id ))
            conn.commit()
            return True
    except Error as err:
        print(Error)
        return False

def get_list():
    """возвращает список программ"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            sqlite_query = "SELECT ID, Code, Name, Level FROM programs"
            c.execute(sqlite_query)
            ret_fetchall = c.fetchall()
            if not ret_fetchall == None:
                return fill_array(ret_fetchall) #ret
            else:
                return []
    except Error:
        print(Error)
        return []

def get_list_by_level(level):
    """возвращает список программ определенного уровня"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            sqlite_query = "SELECT ID, Code, Name, Level FROM programs WHERE Level = ?"
            c.execute(sqlite_query, (level,))
            ret_fetchall = c.fetchall()
            if not ret_fetchall == None:
                return fill_array(ret_fetchall)
            else:
                return []
    except Error:
        print(Error)
        return []

def get_list_modules_program_by_id(id):
    """возвращает список модулей программы с переданным ID"""
    try:
        with open_db(file_DB) as conn:
            c = conn.cursor()
            sqlite_query = """SELECT ID FROM programs_modules WHERE ID = ?"""
            c.execute(sqlite_query, (id, ))
            ret_fetchall = c.fetchall()
            if not ret_fetchall == None:
                return fill_array(ret_fetchall)
            else:
                return []
    except Error:
        print(Error)
        return []


def test():
    print(sqlite3.__file__)
    print('Прямой вызов запрещен!')

if __name__ == '__main__':
    test()

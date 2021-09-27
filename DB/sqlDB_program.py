import sqlite3
from sqlite3 import Error

from . import file_DB

class open_db:  # rонтекстный менеджер
    def __init__(self, name):
        self.f = sqlite3.connect(name)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()

def get_by_id(obj):
    """возвращает учебную программу по переданному ID"""
    try:
        with open_db(file_DB) as conn:
        # with sqlite3.connect(file_DB) as conn:
            # conn = sqlite3.connect(file_DB)
            c = conn.cursor()
            sqlite_query = "SELECT ID, Code, Name FROM programs WHERE ID = ?"
            c.execute(sqlite_query, (obj.id, ))
            ret_fetch = c.fetchone()
            if not ret_fetch == None:
                ret = obj
                obj.code = ret_fetch[1]
                obj.name = ret_fetch[2]
            else:
                ret = None
    except Error:
        print(Error)
    # finally:
    #     if conn:
    #         conn.close()
    return ret

def get_by_code(obj):
    """возвращает учебную программу по переданному коду"""
    try:
        with sqlite3.connect(file_DB) as conn:
            # conn = sqlite3.connect(file_DB)
            c = conn.cursor()
            sqlite_query = "SELECT ID, Code, Name FROM programs WHERE Code = ?"
            c.execute(sqlite_query, (obj.code.upper(), ))
            ret_fetch = c.fetchone()
            if not ret_fetch == None:
                ret = obj
                obj.id = ret_fetch[0]
                obj.name = ret_fetch[2]
            else:
                ret = None
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def add(obj):
    """добавляет учебную программу в БД"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        sqlite_query = "INSERT INTO programs(Code, Name) VALUES (?, ?)"
        c.execute(sqlite_query, (obj.code,obj.name))
        conn.commit()
        ret = True
    except Error:
        print(Error)
        ret = False
    finally:
        if conn:
            conn.close()
    return ret

def delete_by_id(obj):
    """удаляет учебную программу из БД"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON") # Внешние ключи SQLite отключены в целях совместимости. Их нужно включать вручную сразу после каждого подключения к базе данных.
        sqlite_query = """DELETE FROM programs WHERE ID = ?"""
        c.execute(sqlite_query, (obj.id, ))
        conn.commit()
        ret = True
    except Error:
        print(Error)
        ret = False
    finally:
        if conn:
            conn.close()
    return ret

def update(obj):
    """обновляет учебную программу в БД"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        sqlite_query = """UPDATE programs SET Code = ?, Name = ? WHERE ID = ?"""
        c.execute(sqlite_query, (obj.code, obj.name, obj.id ))
        conn.commit()
        ret = True
    except Error as err:
        print(Error)
        ret = False
    finally:
        if conn:
            conn.close()
    return ret

def get_list():
    """возвращает список программ"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        sqlite_query = "SELECT ID, Code, Name FROM programs"
        c.execute(sqlite_query)
        ret_fetchall = c.fetchall()
        if not ret_fetchall == None:
            ret = []
            for record in ret_fetchall:
                ret.append([
                    record[0],
                    record[1],
                    record[2]
                    ]
                )
        else:
            ret = None
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_list_modules_program_by_id(id):
    """возвращает список модулей программы с переданным ID"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        sqlite_query = """SELECT ID FROM programs_modules WHERE ID = ?"""
        c.execute(sqlite_query, (id, ))
        ret_fetchall = c.fetchall()
        if not ret_fetchall == None:
            ret = []
            for record in ret_fetchall:
                ret.append([
                    record[0]
                    # ,
                    # record[1],
                    # record[2]
                    ]
                )
        else:
            ret = None
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret


def test():
    print(sqlite3.__file__)
    print('Прямой вызов запрещен!')

if __name__ == '__main__':
    test()

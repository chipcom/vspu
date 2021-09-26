import sqlite3
from sqlite3 import Error

if __name__ == '__main__':
    print('Прямой вызов запрещен!')

from . import file_DB

def get_by_id(obj):
    """возвращает учебную программу по переданному ID"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT ProgramID, ProgramCode, ProgramName FROM programs WHERE ProgramID = ?", (obj.id, ))
        ret_fetch = c.fetchone()
        if not ret_fetch == None:
            ret = obj
            obj.code = ret_fetch[1]
            obj.name = ret_fetch[2]
        else:
            ret = None
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_by_code(obj):
    """возвращает учебную программу по переданному коду"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT ProgramID, ProgramCode, ProgramName FROM programs WHERE ProgramCode = ?", (obj.code.upper(), ))
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
        c.execute("INSERT INTO programs(ProgramCode, ProgramName) VALUES (?, ?)", (obj.code,obj.name))
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
        sqllite_query = """DELETE FROM programs WHERE ProgramID = ?"""
        c.execute("PRAGMA foreign_keys = ON") # Внешние ключи SQLite отключены в целях совместимости. Их нужно включать вручную сразу после каждого подключения к базе данных.
        c.execute(sqllite_query, (obj.id, ))
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
        sqllite_query = """UPDATE programs SET ProgramCode = ?, ProgramName = ? WHERE ProgramID = ?"""
        c.execute(sqllite_query, (obj.code, obj.name, obj.id ))
        conn.commit()
        ret = True
    except Error:
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
        c.execute("SELECT ProgramID, ProgramCode, ProgramName FROM programs")
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
        sqllite_query = """SELECT ModuleID FROM programs_modules WHERE ProgramID = ?"""
        c.execute(sqllite_query, (id, ))
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
import sqlite3
from sqlite3 import Error

from . import file_DB
# from ..CLASS_APP import program

def get_module_by_id(id):
    """возвращает модуль по переданному ID"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT ModuleID, ModuleCode, ModuleName FROM modules WHERE ModuleID = ?", (id, ))
        ret_fetch = c.fetchone()
        if not ret_fetch == None:
            ret = [ #program.Program(ret_fetch[0], ret_fetch[1], ret_fetch[2])
                    ret_fetch[0],
                    ret_fetch[1],
                    ret_fetch[2]
            ]
        else:
            ret = None
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_module_by_code(code):
    """возвращает модуль по переданному коду"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT ModuleID, ModuleCode, ModuleName FROM modules WHERE ModuleCode = ?", (code.upper(), ))
        ret_fetch = c.fetchone()
        if not ret_fetch == None:
            ret = [
                    ret_fetch[0],
                    ret_fetch[1],
                    ret_fetch[2]
            ]
        else:
            ret = None
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_list_modules():
    """возвращает список модулей"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT ModuleID, ModuleCode, ModuleName FROM modules")
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

def add_module(rec):
    """добавляет модуль в БД"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("INSERT INTO modules(ModuleCode, ModuleName) VALUES (?, ?)", (rec[0],rec[1]))
        conn.commit()
        ret = True
    except Error:
        print(Error)
        ret = False
    finally:
        if conn:
            conn.close()
    return ret

def delete_module(id):
    """удаляет модуль из БД"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        sqllite_query = """DELETE FROM modules WHERE ModuleID = ?"""
        c.execute(sqllite_query, (id, ))
        conn.commit()
        ret = True
    except Error:
        print(Error)
        ret = False
    finally:
        if conn:
            conn.close()
    return ret

def update_module(list):
    """обновляет модуль в БД"""
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        sqllite_query = """UPDATE modules SET ModuleCode = ?, ModuleName = ? WHERE ModuleID = ?"""
        c.execute(sqllite_query, (list[1], list[2], list[0] ))
        conn.commit()
        ret = True
    except Error:
        print(Error)
        ret = False
    finally:
        if conn:
            conn.close()
    return ret
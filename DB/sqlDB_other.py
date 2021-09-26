import sqlite3
from sqlite3 import Error

file_DB = 'learn.db'

def get_subject_by_id(id):
    """возвращает дисциплину по переданному ID"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE SubjectID = ?", (id, ))
        ret = c.fetchone()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_subject_by_code(code):
    """возвращает дисциплину по переданному коду"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE SubjectCode = ?", (code.upper(), ))
        ret = c.fetchone()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_competence_by_id(id):
    """возвращает компетенцию по переданному ID"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM competences WHERE CompetenceID = ?", (id, ))
        ret = c.fetchone()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_competence_by_code(code):
    """возвращает компетенцию по переданному коду"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM competences WHERE CompetenceCode = ?", (code.upper(), ))
        ret = c.fetchone()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_indicator_by_id(id):
    """возвращает идикатор компетенции по переданному ID"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE IndicatorID = ?", (id, ))
        ret = c.fetchone()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_indicator_by_code(code):
    """возвращает идикатор компетенции по переданному коду"""
    ret = ()
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE IndicatorCode = ?", (code.upper(), ))
        ret = c.fetchone()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_list_subjects_module_by_id_module(id):
    """возвращает список дисциплин модуля по переданному ID модуля"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE ModuleID = ?", (id, ))
        ret = c.fetchall()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_list_subjects_module_by_code_module(code):
    """возвращает список дисциплин модуля по переданному коду модуля"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM subjects WHERE ModuleID = (SELECT ModuleID FROM modules WHERE ModuleCode = ?)", (code.upper(), ))
        ret = c.fetchall()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_list_indicators_by_id_competence(id):
    """возвращает список индикаторов компетенции по переданному ID компетенции"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE CompetenceID = ?", (id, ))
        ret = c.fetchall()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

def get_list_indicators_by_code_competence(code):
    """возвращает список индикаторов компетенции по переданному коду компетенции"""
    ret = []
    try:
        conn = sqlite3.connect(file_DB)
        c = conn.cursor()
        c.execute("SELECT * FROM indicators WHERE CompetenceID = (SELECT CompetenceID FROM competences WHERE CompetenceCode = ?)", (code.upper(), ))
        ret = c.fetchall()
    except Error:
        print(Error)
    finally:
        if conn:
            conn.close()
    return ret

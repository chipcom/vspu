import os
import sqlite3
import pprint
from testDB import sqlite3_create_db as db

# pprint.pprint(db.get_name_module('Б1.О.01'))
# pprint.pprint(db.get_name_course('Б1.О.02.01'))
# pprint.pprint(db.get_list_courses_module('Б1.О.01'))
# pprint.pprint(db.get_name_competence('ОПК-1'))
# pprint.pprint(db.get_name_indicator('ИОПК-6.3'))
# pprint.pprint(db.get_list_indicators_competence('УК-1'))
# pprint.pprint(db.get_list_competences_course('Б1.О.01.01'))
# # error
# print(db.get_name_module('Б1.О.10'))
# print(db.get_name_course('Б1.О.02.25'))
# print(db.get_list_courses_module('Б1.О.10'))
# print(db.get_name_competence('ОПК-20'))
# print(db.get_name_indicator('ИОПК-6.23'))
# print(db.get_list_indicators_competence('УК-10'))

file_DB = 'learn.db'
if os.path.exists(file_DB):
    os.remove(file_DB)

conn = sqlite3.connect(file_DB)
c = conn.cursor()

create_table = "CREATE TABLE [modules] ( [ModuleID] INTEGER PRIMARY KEY AUTOINCREMENT, [ModuleCode] TEXT NOT NULL, [ModuleName] TEXT NOT NULL)"
c.execute(create_table)
for row in db.MODULES:
  rec = (row[0], row[1], row[2])
  c.execute("INSERT INTO modules VALUES (?,?,?);", rec)

create_table = "CREATE TABLE [subjects] ( [SubjectID] INTEGER PRIMARY KEY AUTOINCREMENT, [SubjectCode] TEXT NOT NULL, [SubjectName] TEXT NOT NULL, [ModuleID] INTEGER NOT NULL,  FOREIGN KEY(ModuleID) REFERENCES Modules(ModuleID) ON DELETE CASCADE)"
c.execute(create_table)
for row in db.SUBJECTS:
  rec = (row[0], row[1], row[2], row[3])
  c.execute("INSERT INTO subjects VALUES (?,?,?,?);", rec)

create_table = "CREATE TABLE [competences] ( [CompetenceID] INTEGER PRIMARY KEY AUTOINCREMENT, [CompetenceCode] TEXT NOT NULL, [CompetenceName] TEXT NOT NULL)"
c.execute(create_table)
for row in db.COMPETENCES:
  rec = (row[0], row[1], row[2])
  c.execute("INSERT INTO competences VALUES (?,?,?);", rec)

create_table = "CREATE TABLE [indicators] ( [IndicatorID] INTEGER PRIMARY KEY AUTOINCREMENT, [IndicatorCode] TEXT NOT NULL, [IndicatorName] TEXT NOT NULL, [CompetenceID] INTEGER NOT NULL,  FOREIGN KEY(CompetenceID) REFERENCES Competences(CompetenceID) ON DELETE CASCADE)"
c.execute(create_table)
for row in db.INDICATORS:
  rec = (row[0], row[1], row[2], row[3])
  c.execute("INSERT INTO indicators VALUES (?,?,?,?);", rec)

c.execute("SELECT * FROM indicators")
for row in c:
    pprint.pprint(row)

# CREATE TABLE [CustomerCustomerDemo](
#    [CustomerID]TEXT NOT NULL,
#    [CustomerTypeID]TEXT NOT NULL,
#    PRIMARY KEY ("CustomerID","CustomerTypeID"),
#    FOREIGN KEY ([CustomerID]) REFERENCES [Customers] ([CustomerID]) 
#  ON DELETE NO ACTION ON UPDATE NO ACTION,
#  FOREIGN KEY ([CustomerTypeID]) REFERENCES [CustomerDemographics] ([CustomerTypeID]) 
#  ON DELETE NO ACTION ON UPDATE NO ACTION
# );

# c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BAY', 'RHAT', 100, 35.14)")
# c.execute("SELECT * FROM stocks")
# for row in c:
#     print(row)

# user = ('00002', 'Lois', 'Lane', 'Female')
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)

conn.commit()
conn.close()
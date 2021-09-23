# import requests

# url = 'https://portal.vspu.ru/login'

# response = requests.post(url, data={'loginform-username':'baykinaea@mail.ru', 'loginform-password':'vova10021962'})

# if response.status_code == 200:
    # print(response.text)
# else:
    # print(f'Server error: {response.status_code}')

import sqlite3
# import pprint
# from testDB import myDB as db

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

conn = sqlite3.connect('example.db')
c = conn.cursor()


# CREATE TABLE [Categories]
# (      [CategoryID] INTEGER PRIMARY KEY AUTOINCREMENT,
#        [CategoryName] TEXT,
#        [Description] TEXT,
#        [Picture] BLOB
# );
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
c.execute("SELECT * FROM stocks")
for row in c:
    print(row)

# user = ('00002', 'Lois', 'Lane', 'Female')
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)

# conn.commit()
conn.close()
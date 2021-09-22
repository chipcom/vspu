# import requests

# url = 'https://portal.vspu.ru/login'

# response = requests.post(url, data={'loginform-username':'baykinaea@mail.ru', 'loginform-password':'vova10021962'})

# if response.status_code == 200:
    # print(response.text)
# else:
    # print(f'Server error: {response.status_code}')

import pprint
from testDB import myDB as db

pprint.pprint(db.get_name_module('Б1.О.01'))
pprint.pprint(db.get_name_course('Б1.О.02.01'))
pprint.pprint(db.get_list_courses_module('Б1.О.01'))
pprint.pprint(db.get_name_competence('ОПК-1'))
pprint.pprint(db.get_name_indicator('ИОПК-6.3'))
pprint.pprint(db.get_list_indicators_competence('УК-1'))
pprint.pprint(db.get_list_competences_course('Б1.О.01.01'))
# error
print(db.get_name_module('Б1.О.10'))
print(db.get_name_course('Б1.О.02.25'))
print(db.get_list_courses_module('Б1.О.10'))
print(db.get_name_competence('ОПК-20'))
print(db.get_name_indicator('ИОПК-6.23'))
print(db.get_list_indicators_competence('УК-10'))
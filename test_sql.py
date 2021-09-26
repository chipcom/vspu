from DB import sqlDB as db

import pprint

print("Модули:")
pprint.pprint(db.get_module_by_id(3))
pprint.pprint(db.get_module_by_code('б1.О.01'))
pprint.pprint(db.add_module(['К1.О.01', 'Мой модуль']))
pprint.pprint(db.get_list_modules())
# pprint.pprint(db.delete_module(9))
pprint.pprint(db.update_module([10, 'Д1.О.01', 'Мой модуль 10']))
pprint.pprint(db.get_list_modules())

# print("Дисциплины:")
# pprint.pprint(db.get_subject_by_id(2))
# pprint.pprint(db.get_subject_by_code('Б1.О.02.01'))
# print("Дисциплины по модулю:")
# pprint.pprint(db.get_list_subjects_module_by_id_module(3))
# pprint.pprint(db.get_list_subjects_module_by_code_module('Б1.О.01'))
# print("Компетенции:")
# pprint.pprint(db.get_competence_by_id(10))
# pprint.pprint(db.get_competence_by_code('ОПК-1'))
# print("Индикаторы:")
# pprint.pprint(db.get_indicator_by_id(3))
# pprint.pprint(db.get_indicator_by_code('ИОПК-6.3'))
# print("Индикаторы по компетенции:")
# pprint.pprint(db.get_list_indicators_by_id_competence(3))
# pprint.pprint(db.get_list_indicators_by_code_competence('ОПК-7'))

# # error
# print(db.get_name_module('Б1.О.10'))
# print(db.get_name_course('Б1.О.02.25'))
# print(db.get_list_courses_module('Б1.О.10'))
# print(db.get_name_competence('ОПК-20'))
# print(db.get_name_indicator('ИОПК-6.23'))
# print(db.get_list_indicators_competence('УК-10'))
# from DB import sqlDB_program as program_DB
# from DB import sqlDB_module as module
from CLASS_APP import program as program
from CLASS_APP import sql_program as sql
import pprint

# import CLASS_APP

print("Программы обучения:")
obj= program.Program()# program.Program(id=1)
pprint.pprint(obj.type)
# pprint.pprint(program.Program.__mro__)
pprint.pprint(sql.get_by_id(1))
pprint.pprint(sql.get_by_code(code = '44.04.01'))
print()
pprint.pprint(sql.get_list())
print()
pprint.pprint(sql.get_list_by_level(1))
# pprint.pprint(program_DB.add(program.Program(code = '44.04.99',name='Lets go')))
# pprint.pprint(program_DB.get_list())
# print()
# pprint.pprint(program_DB.update(program.Program(id=2, code = '44.04.02', name='nothing')))
# pprint.pprint(program_DB.get_list())
# pprint.pprint(program_DB.get_list_modules_program_by_id(1))
# program_DB.delete_program_by_id(program.Program(id=1))
# pprint.pprint(program_DB.get_list_modules_program_by_id(1))
# pprint.pprint(program_DB.get_by_id(program.Program(id=1)))
# pprint.pprint(program_DB.update(obj))
# pprint.pprint(program_DB.get_by_id(program.Program(id=1)))
# pprint.pprint(program_DB.get_list())

# print("Модули:")
# pprint.pprint(module.get_module_by_id(3))
# pprint.pprint(module.get_module_by_code('б1.О.01'))
# pprint.pprint(module.add_module(['К1.О.01', 'Мой модуль']))
# pprint.pprint(module.get_list_modules())
# pprint.pprint(module.delete_module(9))
# pprint.pprint(module.update_module([10, 'Д1.О.01', 'Мой модуль 10']))
# pprint.pprint(module.get_list_modules())


import sys
import unittest
from main import *

PARAMS1 = (
    ([{'type': 'passport', 'number': '2207 876234','name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2','name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006','name': 'Аристарх Павлов'},
    {'type': 'insurance', 'number': '10007','name': 'Лукойл Павлов'},
    {'type': 'insurance', 'number': '10008','name': 'Собака Павлова'},
    {'type': 'passport', 'number': '23456', 'name': 'Смирнов'}],
    {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': ['10007', '10008', '23456']})
    )

PARAMS2 = (
    ([{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
      {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
      {'type': 'insurance', 'number': '10007', 'name': 'Лукойл Павлов'},
      {'type': 'insurance', 'number': '10008', 'name': 'Собака Павлова'}],
     {'1': ['2207 876234'], '2': ['10006'], '3': ['10007', '10008']})
    )

class MyTestCase(unittest.TestCase):
    def test_give_name_right(self):
        self.assertEqual(give_name(documents_list, '10006'), 'Аристарх Павлов')
    def test_give_name_null(self):
        self.assertEqual(give_name(documents_list, '1006'), 'Документ под номером 1006 нет')
    def test_give_new_doc(self):
        self.assertEqual(give_new_doc(documents_list, directories_dict, 'passport', '23456', 'Смирнов', '3'), PARAMS1)
    def test_delete_doc_dir(self):
        self.assertEqual(delete_doc_dir(documents_list, directories_dict, '11-2'), PARAMS2)

if __name__ == '__main__':
    unittest.main()




import unittest
from parameterized import parameterized
from main import documents, directories, person_name, shelf_number, documents_list, add_doc

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.documents = documents
        self.directories = directories

    def tearDown(self) -> None:
        return super().tearDown()


    def test_person_name(self):
        self.assertEqual(person_name(self.documents, '2207 876234'), 'Василий Гупкин')  # add assertion here

    def test_shelf_number(self):
        self.assertEqual(shelf_number(self.directories, '2207 876234'), 'документ № 2207 876234 лежит на полке № 1')  # add assertion here
        self.assertEqual(shelf_number(self.directories, '2'), 'Такой № документа: 2 не лежит на полке')

    def test_documents_add_doc(self):
         self.assertEqual(add_doc(self.documents, self.directories, 'passport', '2727', 'Василий Ужепупкин', '1'),\
                          {'name': 'Василий Ужепупкин', 'number': '2727', 'type': 'passport'})

    def test_documents_list(self):
         self.assertEqual(documents_list(self.documents), 5)


if __name__ == '__main__':
    unittest.main()

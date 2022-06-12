#https://replit.com/@AngelaLoiko/171DocsInLibrary#main.py
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "invoice", "number": "11-22", "name": "Геннадий Дважды-Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
# for document in documents:
# print(list(document.values()))
# print(list(document.keys()))


def person_name(my_docs=documents, number_doc="2207 876234"):
    #number_doc = input('Введите номер документа: ')
    is_exist_number_doc = False
    for document in my_docs:
        if document['number'] == number_doc:
            return (document['name'])
            is_exist_number_doc = True
    else:
        if not is_exist_number_doc:
            print('Такого номера документа не существует')


def shelf_number(my_dir=directories, number_doc='11-22'):
    # number_doc = input('Введите номер документа: ')
    is_exist_number_doc = False
    for key, values in my_dir.items():
        if number_doc in list(values):
            return(f'документ № {number_doc} лежит на полке № {key}')
            is_exist_number_doc = True
    else:
        if not is_exist_number_doc:
            return(f'Такой № документа: {number_doc} не лежит на полке')


def documents_list(my_docs=documents):
    i = 0
    for document in my_docs:
        need_record = (f'''{document['type']} "{document['number']}" "{document['name']}"''')
        i += 1
        print(need_record)
    return i


def add_doc(my_docs, my_dir, doc_type='passport', doc_number='2727', owner_name='Василий Ужепупкин', shelf_number='1' ):
    #doc_type = input('Введите тип документа: ')
    #doc_number = input('Введите номер документа: ') #задача проверять на уникальность не ставилась
    # owner_name = input('Введите имя владельца: ')
    # shelf_number = input('Введите номер полки: ')
    while my_dir.get(shelf_number) is None:
        print(f'Номера полки {shelf_number} не существует')
        shelf_number = input('Повторите ввод номера полки: ')
    else:
        new_doc = {"type": doc_type, "number": doc_number, "name": owner_name}
        my_docs.append(new_doc)
        new_doc_list = list(my_dir.get(shelf_number))
        new_doc_list.append(doc_number)
        my_dir[shelf_number] = new_doc_list
        print(my_docs)
        print(my_dir)
        return new_doc

def del_doc(my_docs, my_dir):
    doc_number = input('Введите номер документа: ')
    is_doc_exist = False
    for id_rec, my_document in enumerate(my_docs):
        if doc_number in list(my_document.values()):
            del(my_docs[id_rec])
            is_doc_exist = True
    else:
        if is_doc_exist:
            print(f'Документ с номером {doc_number} удален из базы документов')
            # del_from_dir(doc_number) # можем удалять из полки только когда документ присутствует в базе документов
        else:
            print(f'Документа с номером {doc_number} нет в базе документов')
    del_from_dir(doc_number, my_dir)  # почистим полочки в любом случае
    print(my_docs)
    print(my_dir)


def del_from_dir(doc_number, my_dir):
    for key, value in my_dir.items():
        if doc_number in list(value):
            value.remove(doc_number)


def add_dir(my_dir):
    shelf_number = input('Введите номер полки: ')
    my_dir.setdefault(shelf_number, [])
    print(my_dir)


def seek_in_docs(doc_number, my_docs):
    is_exist_number_doc = False
    for document in my_docs:
        if document['number'] == doc_number:
            is_exist_number_doc = True
    return is_exist_number_doc


def get_shelf_from_dir(doc_number, my_dir):
    for key, value in my_dir.items():
        if doc_number in list(value):
            return key
    else:
        return None


def append_to_dir(doc_number, shelf_num, my_dir):
    new_doc_list = list(my_dir.get(shelf_num))
    new_doc_list.append(doc_number)
    my_dir[shelf_num] = new_doc_list


def move_doc(my_docs, my_dir):
    doc_number = input('Введите номер документа: ')
    shelf_number = input('Введите номер полки: ')
    if seek_in_docs(doc_number, my_docs):
        if not (my_dir.get(shelf_number) is None):
            shelf_dir = get_shelf_from_dir(doc_number, my_dir)
            if not (shelf_dir is None):
                if shelf_dir == shelf_number:
                    print(f'Документ № {doc_number} уже лежит на полке № {shelf_number}. Перемещение не требуется')
                else:
                    del_from_dir(doc_number, my_dir)
                    append_to_dir(doc_number, shelf_number, my_dir)
                    print(f'Документ № {doc_number} перемещен с полки № {shelf_dir} на полку № {shelf_number}')
            else:
                append_to_dir(doc_number, shelf_number, my_dir)
                print(f'Документ № {doc_number} помещен на полку № {shelf_number}')
        else:
            print(f'Полки № {shelf_number} не существует')
    else:
        print(f'Документа № {doc_number} нет в базе документов')
   # print(my_docs)
   # print(my_dir)


def main(my_docs, my_dir):
    while True:
        mycommand = input('Введите команду: ')
        if mycommand in('p', 's', 'l', 'a', 'd', 'as', 'm', 'q'):
            if mycommand == 'p':
                person_name(my_docs)

            if mycommand == 's':
                shelf_number(my_dir)

            if mycommand == 'l':
                documents_list(my_docs)

            if mycommand == 'a':
                add_doc(my_docs, my_dir)

            if mycommand == 'd':
                del_doc(my_docs, my_dir)

            if mycommand == 'as':
                add_dir(my_dir)

            if mycommand == 'm':
                move_doc(my_docs, my_dir)

            if mycommand == 'q':
                break
        else:
            print("Такой команды не существует")
            print("p - имя по номеру документа")
            print("s - номер полки по номеру документа")
            print("l - список документов")
            print("a - добавить документ")
            print("d - удалить документ")
            print("m - переместить документ")
            print("as - добавить полку")
            print("q - выход")

if __name__ == '__main__':
    pass
    #main(documents, directories)
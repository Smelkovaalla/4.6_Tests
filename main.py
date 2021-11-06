from pprint import pprint

documents_list = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}, {
    "type": "insurance",
    "number": "10007",
    "name": "Лукойл Павлов"
}, {
    "type": "insurance",
    "number": "10008",
    "name": "Собака Павлова"
}]

directories_dict = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': ['10007', '10008']}


def give_name(doc_list, num):
    result = 0
    for doc in doc_list:
        if num == doc['number']:
            result = doc['name']
    if result == 0:
        return f'Документ под номером {num} нет'
    else:
        return result

def give_new_doc(doc_list, dir_dict, type_new_doc, number_new_doc, name_new_doc, dir_new_doc):
  result = []
  for i in dir_dict.keys():
    result.extend(i)
  if dir_new_doc not in result:
    print(f'Такой полочки у нас нет')
  else:
    dir_dict[dir_new_doc].append(number_new_doc)
    new_doc_dict = {}
    new_doc_dict["type"] = type_new_doc
    new_doc_dict["number"] = number_new_doc
    new_doc_dict["name"] = name_new_doc
    doc_list.append(new_doc_dict)
  return doc_list, directories_dict

def delete_doc_dir(doc_list, dir_dict, num):
    a = 0
    for doc_num in dir_dict.values():
        if num not in doc_num:
            a +=1
    if a < len(dir_dict):
        for doc_num in dir_dict.values():
            if num in doc_num:
                doc_num.remove(num)
                for document in doc_list:
                    if num in document.values():
                        x = 0
                        leeen = len(document.keys())
                        while x < leeen:
                            a = list(document.keys())[0]
                            del document[a]
                            x += 1
    else:
        print(f'Такого документа на полках нет')
    result_list = list(filter(None, doc_list))
    return result_list, dir_dict

if __name__ == '__main__':
    pass
    print(delete_doc_dir(documents_list, directories_dict, '11-2'))

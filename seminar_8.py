# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')


    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice==6:
            new_data = del_user(phone_book)
            write_txt(new_data, phone_book)
        choice = show_menu()

def read_txt(filename):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data   

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)
    print(data)
 
def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def get_search_name():
    return input("Введите фамилию для поиска: ")

def find_by_name(data: list, name):
    for j in data:
        if j.get("Фамилия")==name:
            return j.get("Телефон")
    return ("абонента с такой фамилией не существует")

def get_search_number():
    return input("Введите телефон для поиска: ")

def find_by_number(data: list, number):
    for x in data:
        if x.get("Телефон")==number:
            return x.get("Фамилия")
    return ("Абонента с таким номером не существует")

def get_new_user():
    a = input("Введите фамилию: ")
    b = input("Введите имя: ")
    c = input("Введите номер: ")
    d = input("Введите описание: ")
    return f'{a},{b},{c},{d}'
    
def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as sfile:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            sfile.write(f'{s[:-1]}\n')
        print(phone_book, file=sfile)

def get_file_name():
    file_name = input("введите название: ")
    return file_name


def del_user(data: list):
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    data.pop(number_journal-1)
    print(data)
    
    
work_with_phonebook()













        
#  if number_file == 1:  # Можно сделать нумерацию внутри файла
#          print("Какую именно запись по счету Вы хотите удалить?")
#          number_journal = int(input('Введите номер записи: '))
#          # Можно добавить проверку, чтобы человек не выходил за пределы записи
#          print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
#          data_first = data_first[:number_journal] + data_first[number_journal + 1:]        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
#              file.write(''.join(data_first))
#          print('Изменения успешно сохранены!'

# def sample_data(data:list):
#     sample_data_new = [[key, value] for key, value in data.items()]
#     print(sample_data_new)
#     return sample_data_new 


from datetime import date, datetime
import base
import controller
import view

def all_notes():
    notebook = sorted(base.read_csv(), key=lambda x: datetime.strptime(x['Дата создания'], '%Y-%m-%d'), reverse=False)
    for note in notebook:
        view.print_note(note)
    controller.menu()

def add_note():
    notebook = base.read_csv()
    heading = input('Заголовок: ')
    note_body = input('Заметка: ')

    last_note_id = 0
    for note in notebook:
        last_note_id = int(note["ИД"])

    with open('notebook.csv', 'a', encoding='utf-8') as data:
        data.write(f'{last_note_id + 1 };{heading};{note_body};{date.today()};{date.today()}\n')
    data.close()

    view.save_ok()
    controller.menu()

def redact():
    notebook = base.read_csv()
    id_note = input("Введите ИД заметки для редактирования: ")
    not_search = True

    for note in notebook:
        if note["ИД"] == id_note:
            print(f'Заметка №{note["ИД"]}')
            note["Заголовок"] = input(f'Текущий заголовок: {note["Заголовок"]} -> ')
            note["Заметка"] = input(f'Текущая заметка: {note["Заметка"]} -> ')
            note["Дата изменения"] = date.today()
            base.write_csv(notebook)
            view.save_ok()
            not_search = False
    
    if not_search == True:
        view.not_search()
    controller.menu()

def del_note():
    notebook = base.read_csv()
    id_note = input("Введите ИД заметки для удаления: ")
    not_search = True

    for note in notebook:
        if note["ИД"] == id_note:
            view.print_note(note)
            res = input("Удалить эту заметку? y/n: ")
            if res == "y":
                notebook.remove(note)
                base.write_csv(notebook)
                view.del_ok()
            not_search = False
    
    if not_search == True:
        view.not_search()
    controller.menu()

def search_id():
    notebook = base.read_csv()
    id_note = input("Введите ИД заметки для поиска: ")
    not_search = True

    for note in notebook:
        if note["ИД"] == id_note:
            view.print_note(note)
            not_search = False
    if not_search == True:
        view.not_search()
    controller.menu()

def search_date():
    notebook = base.read_csv()
    date_note = input("Введите дату для поиска заметок (YYYY-MM-DD): ")
    not_search = True

    for note in notebook:
        if note["Дата создания"] == date_note:
            view.print_note(note)
            not_search = False
    if not_search == True:
        view.not_search()
    controller.menu()
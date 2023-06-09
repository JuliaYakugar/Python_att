def show_menu() -> int:
    print("Выберите пункт меню:\n"
    "1. Показать список заметок\n"
    "2. Создать заметку\n"
    "3. Редактировать заметку\n"
    "4. Удалить заметку\n"
    "5. Найти заметку\n"
    "6. Найти заметки по дате\n"
    "7. Завершить")
    return int(input("Введите номер необходимого действия: "))

def exit():
    print('********************\n* Работа завершена *\n********************')

def print_note(note):
    print(f'--------------------------------------------\nЗаметка №{note["ИД"]}\n{note["Заголовок"]}\n{note["Заметка"]}\nДата создания: {note["Дата создания"]}; Дата изменения: {note["Дата изменения"]}\n--------------------------------------------')

def save_ok():
    print("*********************\n* Успешно сохранено *\n*********************")

def del_ok():
    print("*******************\n* Успешно удалено *\n*******************")

def not_search():
    print("!!!!!!!!!!!!!!!!!!!!!!\n! Заметка не найдена !\n!!!!!!!!!!!!!!!!!!!!!!")
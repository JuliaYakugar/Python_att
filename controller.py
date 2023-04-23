import model
import view

def menu():
    num_menu = view.show_menu()

    if num_menu == 1: 
        model.all_notes()
    if num_menu == 2: 
        model.add_note()
    if num_menu == 3:
        model.redact()
    if num_menu == 4:
        model.del_note()
    if num_menu == 5:
        model.search_id()
    if num_menu == 6:
        model.search_date()
    if num_menu == 7:
        view.exit()
        
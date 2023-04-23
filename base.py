def read_csv():
    notes = []
    note = ["ИД", "Заголовок", "Заметка", "Дата создания", "Дата изменения"]
    with open("notebook.csv", 'r', encoding='utf-8') as data:
        for line in data:
            notes.append(dict(zip(note, line.strip().split(';'))))
    return notes

def write_csv(notebook: list):
    with open('notebook.csv', 'w', encoding='utf-8') as data:
        for note in notebook:
	        data.write((f"{note['ИД']};{note['Заголовок']};{note['Заметка']};{note['Дата создания']};{note['Дата изменения']}\n"))


import json
import datetime

NOTES_FILE = 'notes_data.json'

def load_notes():
    try:
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def create_note():
    title = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"title": title, "text": text, "timestamp": timestamp}

def list_notes():
    notes = load_notes()
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']} - {note['timestamp']}")

def edit_note():
    notes = load_notes()
    list_notes()
    note_index = int(input("Выберите номер заметки для редактирования: ")) - 1
    note = notes[note_index]
    note['title'] = input("Введите новое название заметки: ")
    note['text'] = input("Введите новый текст заметки: ")
    save_notes(notes)

def delete_note():
    notes = load_notes()
    list_notes()
    note_index = int(input("Выберите номер заметки для удаления: ")) - 1
    del notes[note_index]
    save_notes(notes)

def main():
    while True:
        print("\n1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            note = create_note()
            notes = load_notes()
            notes.append(note)
            save_notes(notes)
        elif choice == '2':
            list_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
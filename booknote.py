
import datetime
import json
from display import display_menu
from file_load import load_notes_from_file

import colorama
colorama.init()
start = "\033[1;31m"
end = "\033[0;0m"


def error_print():
    print(start + "\"неверный выбор\"" + end)



def note_zero_function():    

    def display_note(note):
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Содержание: {note['body']}")
        print(f"Дата/время создания: {note['created_at']}")
        print(f"Дата/время последнего изменения: {note['updated_at']}")


    def display_notes(notes):
        for note in notes:
            print(
                f"ID: {note['id']}, Заголовок: {note['title']}, Дата/время создания: {note['created_at']}")


    def add_note(notes):
        id = input("Введите ID заметки: ")
        title = input("Введите заголовок заметки: ")
        body = input("Введите содержание: ")
        created_at = datetime.datetime.now().strftime("%d-%m-%Y")
        updated_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        notes.append({"id": id, "title": title, "body": body,
                    "created_at": created_at, "updated_at": updated_at})
        print("Заметка создана")


    def edit_note(notes):
        id = input("Введите ID заметки для редактирования: ")
        for note in notes:
            if note['id'] == " " or note['id'] != id:
                error_print()
                break
            elif note['id'] == id:
                title = input("Введите новый заголовок заметки: ")
                body = input("Введите новое содержание заметки: ")
                note['title'] = title
                note['body'] = body
                note['updated_at'] = datetime.datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S")
                break


    def delete_note(notes):
        id = input("Введите ID заметки для удаления: ")
        for note in notes:
            if note['id'] == id:
                notes.remove(note)
                break
            else:
                error_print()

    

    def save_notes_to_file(notes):
        with open("notes_hw/note_files/notes.json", "w") as file:
            json.dump(notes, file)    
    

    load_notes_from_file()
    notes = load_notes_from_file()

    while True:
        display_menu()
        option = input("Выберите опцию: ")
        if option == "1":
            display_notes(notes)
        elif option == "2":
            id = input("Введите ID заметки: ")
            for note in notes:
                if note['id'] == id:                    
                    display_note(note)                                                                   
        elif option == "3":
            created_at = input("Введите дату заметки в формате dd-MM-YYYY: ")
            for note in notes:
                if note['created_at'] == created_at:                    
                    display_note(note)                      
        elif option == "4":
            add_note(notes)
        elif option == "5":
            edit_note(notes)
        elif option == "6":
            delete_note(notes)
        elif option == "7":
            save_notes_to_file(notes)
            break    
        else:
            error_print()

    

from command import Commands
from note import Note
from datetime import datetime
from typing import List
from model_file import ModelFile


def create_note(id_n, title_n, body_n, date_n):
    """
    Метод создает заметку
    :param id_n: ID заметки
    :param title_n: заголовок заметки
    :param body_n: тело заметки
    :param date_n: дата создания или изменения заметки
    :return: тип данных Note
    """
    note = Note(id_n, title_n, body_n, date_n)
    return note


def create_note_input(notes: List[Note]):
    """
    Метод создания заметки и добавления ее в список заметок введенных из консоли
    :param notes: Список заметок, либо пустой список
    :return: список заметок
    """
    id = int(input("Введите номер заметки: "))
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    note = Note(id, title, body, date)
    notes.append(note)
    return notes


class Controller:
    """
    Класс запуска комманд выполняющих действия над заметками
    """

    def run(self) -> None:
        """
        Метод позволяющий выполнять какие-либо действия с заметками (например выводить все заметки, изменять заметки)
        :return: None
        """
        print('Список комманд:\n'
              'ADD - добавить новую заметку\n'
              'LIST - вывести список заметок\n'
              'UPDATE - обновить заметку\n'
              'DELITE - удалить заметку\n'
              'EXIT - выход из программы')
        file_name = "notes.csv"
        com = Commands.NONE
        flag = True
        while flag:
            command = input("Введите команду: ")
            com = Commands[command.upper()]

            if com == Commands.EXIT:
                flag = False
                print("Выход из программы")

            elif com == Commands.ADD:
                file = ModelFile(file_name)
                # self.notes = self.model.get_notes()
                # self.notes = create_note_input(self.notes)
                notes_file = file.get_notes()
                notes = create_note_input(notes_file)
                file.save_note_to_file(notes)

                print("Заметка успешно создана!")

            elif com == Commands.LIST:
                file = ModelFile(file_name)
                notes_file = file.get_notes()
                print("----- Список всех заметок -----")
                print("id | title | body | date")
                print("___________________________________________")
                for note in notes_file:
                    print(note)

            elif com == Commands.UPDATE:
                file = ModelFile(file_name)
                notes_file = file.get_notes()
                update_id = int(input("Введите ID заметки для обновления: "))

                if update_id not in [i.get_id() for i in notes_file]:
                    print("Нет заметки с таким ID")
                else:
                    for note in notes_file:
                        if note.get_id() == update_id:
                            update_body = note.get_body()
                            print(f"Ваша заметка содержит следующее: {update_body}")
                            update_body = input("Введите новый текст вашей заметки: ")
                            note.set_body(update_body)
                            note.set_date(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

                    file.save_note_to_file(notes_file)
                    print("Изменения внесены успешно")

            elif com == Commands.DELETE:
                file = ModelFile(file_name)
                notes_file = file.get_notes()
                delete_id = int(input("Введите ID заметки для удаления: "))
                if delete_id not in [i.get_id() for i in notes_file]:
                    print("Нет заметки с таким ID")
                else:
                    for i in range(len(notes_file)):
                        if notes_file[i].get_id() == delete_id:
                            idx = i
                            break
                    del_note = notes_file.pop(idx)
                    file.save_note_to_file(notes_file)
                    print(f'Заметка "{del_note}" удалена успешно!')

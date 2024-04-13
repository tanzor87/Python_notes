from typing import List
from note import Note


class ModelFile:
    """
    Класс записи заметок в файл и чтения заметок из файла
    """
    def __init__(self, file_name: str):
        self.file_name = file_name
        try:
            with open(file_name, 'a') as fw:
                fw.flush()
        except Exception as e:
            print(e)

    def save_note_to_file(self, notes: List[Note]) -> None:
        """
        Метод сохранения списка заметок в файл
        :param notes: Список заметок
        :return: None
        """
        try:
            with open(self.file_name, 'w') as fw:
                for note in notes:
                    fw.write(f"{note.get_id()};{note.get_title()};{note.get_body()};{note.get_date()}\n")
                fw.flush()
        except Exception as e:
            print(e)

    def get_notes(self):
        """
        метод получения списка заметок из файла
        :return: список заметок
        """
        notes = []
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                lines = [line.rstrip() for line in lines]
                for line in lines:
                    data = line.split(";")
                    note = Note(int(data[0]), data[1], data[2], data[3])
                    notes.append(note)
        except Exception as e:
            print(e)

        return notes

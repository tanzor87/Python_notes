
class Note:
    def __init__(self, id_note: int, title: str, body: str, date: str):
        self.id = id_note
        self.title = title
        self.body = body
        self.date = date

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title

    def get_body(self) -> str:
        return self.body

    def set_body(self, body: str) -> None:
        self.body = body

    def get_date(self):
        return self.date

    def set_date(self, date: str) -> None:
        self.date = date

    def get_id(self):
        return self.id

    def set_id(self, id_note: int) -> None:
        self.id = id_note

    def __str__(self) -> str:
        return f'{self.id} | {self.title} | {self.body} | {self.date}'

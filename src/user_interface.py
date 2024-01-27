from abc import ABC, abstractmethod
from prettytable import PrettyTable
# from src.classes import AddressBook
# from src.notes import NoteManager


class UserInterface(ABC):

    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass


class ConsoleUserInterface(UserInterface):

    def display_contacts(self, address_book):
        if not address_book.data:
            return "The address book is empty."

        table = PrettyTable(['Name', 'Phones', 'Birthday', 'Email'])
        table.align = 'l'

        total_contacts = len(address_book.data)

        for idx, (name, record) in enumerate(address_book.data.items()):
            phones = "\n".join(map(str, record.phones))
            birthday = record.birthday if record.birthday else ""
            email = record.email if record.email else ""
            table.add_row([name, phones, birthday if birthday != "" else None, email if email != "" else None])

            # Add separator line if it's not the last contact
            if idx < total_contacts - 1:
                table.add_row(["-" * 20, "-" * 20, "-" * 20, "-" * 20])
        
        return str(table)

    def display_notes(self, note_manager):
        if not note_manager.notes:
            print("No notes available.")
        else:
            table = PrettyTable(['Author', 'Title', 'Note', 'Tags', 'Date'])
            table.align = 'l'
            for note in note_manager.notes:
                table.add_row([note.author, note.title, note.note, note.tags, note.date])
            print(table)


class WebUserInterface(UserInterface):

    def display_contacts(self, contacts):
        pass

    def display_notes(self, notes):
        pass
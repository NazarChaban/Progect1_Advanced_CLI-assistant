# Made by P.O.N.D.A.M. team
# CLI Personal Assistant

This is a Command Line Interface (CLI) your personal assistant written in Python. It allows users to manage contact information, including names, phone numbers, and birthdays. Manage notes, including authors, titles, notes and tags. Also it provides function of sorting certain folder.

## Features

### General
- **Help** list by typing `help`
- **Save** the current state of the address book and notes manager.
- **Load** data from a file.
- **Clear** termanil.
- **Exit** by typing key words.

### Addressbook 
- **Add new contacts** with multiple phone numbers and an optional birthday.
- **Find a contact** and display all related information.
- **Find all contacts matching** a particular pattern in their names or phone numbers.
- **Delete a contact** and all associated data.
- **Display all contacts** in the address book.
- **Display contacts** in paginated format, with a custom number of contacts **per page**.
- **Add a phone number** to an existing contact.
- **Remove a phone number** from an existing contact.
- **Edit an existing phone number** of a contact.
- **Set, update or remove a birthday** for a contact.
- **Set, update or remove email** for a contact.
- **Calculate the number of days** until a contact's next birthday.
- **Show list of birthdays** until certain date.

### Note Manager
- **Create** and delete notes.
- **Change** info of notes.
- **Show** all notes or by tags.
- **Delete** all notes

### Sorter
- **Sort** certain folder by command `sort <path/to/folder>`

You can see more info about sorter progect at this page: https://github.com/Vivern0/Sorter.git


## Installation

To use the CLI Assistant, you need to have Python installed on your system. If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

Once Python is installed, clone this repository to your local machine.

## Usage
### Poetry venv
For better experience use `poetry` library. Install to global environment by command:
```sh
pip install poetry
```
and then use this command in project directory to run poetry venv and install dependencies:
```sh
poetry shell
```
```sh
poetry install
```

### Pip
Or if you don't like poetry) just run this command:
```sh
pip install -r requirements.txt
```

### Docker
Also there is an opportunity to run this Assistant with docker
```sh
docker build -t <image_name> .
```
```sh
docker run -it --name <process_name> <image_name>
```

### Start working
To start the application, run the following command in your terminal:
```sh
python main.py
```

or download Assistant as package by command:
```sh
pip install -e .
```
```sh
assistant
```



Once the application is running, you will be able to use the following commands:

- `hello`: Display a welcome message.
- `save`: Save the address book.
- `add <name> <phone>`: Add a new contact to your address book or add a number to an old contact.
- `set email <name> <email>`: Add email for the contact.
- `set birthday <name> <date>`: Set a birthday for a contact.
- `days to birthday <name>`: Calculate the number of days until the next birthday for a contact.
- `show birthday list <date>`: Show a list of birthdays up to a specific date.
- `change phone <name> <old phone> <new phone>`: Change the selected phone.
- `change email/birthday <name> <new data>`: Change the details of an existing contact.
- `remove <name> <<phone>/birthday/email>`: Delete information for the contact.
- `info <name>`: Display information about the contact.
- `delete <name>`: Delete a contact from your address book.
- `show all`: Show all contacts in the address book.
- `search <data>`: Search the address book by character.
- `sort`: Sorts the required folder.
- `create note <author> <title>`: Adds a note.
- `append note tags <title>, <tag_1 tag_2 ...>`: Adds a tag to notes.
- `showing all notes`: Show all notes.
- `deletion note <title>`: Deletes a note.
- `clear notes` : Deletes all notes.
- `searching note by tags <tag_1 tag_2 ...>`: Search by tags.
- `exit/close/good bye`: Exit the app.
- `clear`: Clear the terminal.

## Contributing
Contributions to YOUR_PROJECT_NAME are welcome! Feel free to submit pull requests or open issues to improve the functionality or fix issues within the application.

## License
This project is licensed under the MIT License - see the LICENSE file for details.




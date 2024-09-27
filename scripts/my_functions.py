import csv
from typing import TypeVar

ReaderType = TypeVar('_csv.reader')
WriterType = TypeVar('_csv.writer')

def read_to_list(file: str) -> list[str]:
    with open(file, mode='r') as f:
        reader: ReaderType = csv.reader(f)
        return [row for row in reader]

def print_menu() -> None:
    print("=== Menu ===")
    print("1. Person anlegen")
    print("2. Auto anlegen")
    print("3. People speichern in Datei")
    print("4. Autos speichern in Datei")
    print("5. People auslesen aus der Datei")
    print("6. Autos auslesen aus der Datei")
    print("7. Kunde löschen")
    print("8. Auto löschen")
    print("0. Program beenden")

def print_line(n: int) -> None:
    print(n * "=")


def wait_for_input(key: int) -> None:
    while True:
        wait: int = int(input(f"To continue enter {key}: "))
        if wait == key:
            break

def print_list(l: list[any]) -> None:
    for i in l:
        for j in i:
            print(j, end=' ')
        print()

def write_to_file(file: str, l: list[any]) -> None:
    if l:
        with open(file, 'w', newline='') as f:
            writer: WriterType = csv.writer(f)
            writer.writerows(l)
            print()
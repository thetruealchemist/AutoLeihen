import os
from my_classes import Person, Auto
from my_functions import (print_menu, 
                          print_line, 
                          wait_for_input,
                          read_to_list, 
                          print_list, 
                          write_to_file)

def main() -> None:
     
    people: list[str] = []
    autos: list[str] = []

    autos_datei: str = "../text/autos.txt"
    people_datei: str = "../text/people.txt"

    while True:
        os.system('cls')
        print_menu()

        while True:
            commando: int = int(input("Bitte Auswahl angeben: "))
            if commando == 1:
                print("Person anlegen...")
                print_line(10)
                name: str = input("Name: ")

                people_from_file: list[str] = read_to_list(file=people_datei)

                if people_from_file:
                    geliehene_auto_ids: list[int] = [int(person[2]) for person in people_from_file]

                autos_from_file: list[str] = read_to_list(file=autos_datei)
                ids: list[int] = []
                for auto in autos_from_file:
                    ids.append(int(auto[0]))
                    if int(auto[0]) not in geliehene_auto_ids:
                        for i in auto:
                            print(i, end=' ')
                        print()

                print_line(10)
                while True:
                    provided_id: int = int(input("Welche id? "))
                    if provided_id in ids:                    
                        if provided_id not in geliehene_auto_ids:
                            auto: int = provided_id
                            break
                        else:
                            print("Fehler: Das Auto ist bereits geliehen!")
                    else:
                        print("Fehler: Id nicht in der gegebenen Liste gefunden!")

                person: Person = Person(name, auto=auto)
                people.append(person)

                print(f"Der Kunde {name} wurde angelegt.")
                print_line(10)
                wait_for_input(key=0)
                break
            elif commando == 2:
                print("Auto anlegen...")
                print_line(10)
                modell: str = input("Modelle: ")
                geschw: str = input("Geschwindigkeit: ")
                farbe: str = input("Farbe: ")
                auto: Auto = Auto(modell, geschw, farbe)
                autos.append(auto)
                print(f"Das Auto {auto} wurde angelegt.")
                print_line(10)
                wait_for_input(key=0)
                break
            
            elif commando == 3:
                print("People Liste speichern...")
                print_line(10)

                people_from_file: list[str] = read_to_list(file=people_datei)
    
                if people_from_file[0]:
                    ids: list[int] = [int(person[0]) for person in people_from_file] 
                    id: int = max(ids) + 1

                else:
                    id: int = 0

                with open(people_datei, "a") as f:
                    for person in people:
                        text: str = f"{id},{person.name},{person.auto}\n"
                        f.write(text)
                        id += 1  
                people.clear()                          
                
                print("Speicherung der People durchgeführt")
                print_line(10)
                wait_for_input(key=0)            
                break

            elif commando == 4:
                print("Auto List speichern...")
                print_line(10)
                
                autos_from_file: list[str] = read_to_list(autos_datei)
                
                ids: list[int] = [int(auto[0]) for auto in autos_from_file]

                with open(autos_datei, "a") as f:
                    for auto in autos:
                        text: str = f"{id},{auto.modell},{auto.geschw},{auto.farbe}\n"
                        f.write(text)
                        id += 1
                autos_from_file.clear()                
                print("Speicherung der Autos durchgeführt")
                print_line(10)
                wait_for_input(key=0)
                break            

            elif commando == 5:
                print("Peopleliste lesen...")
                print_line(10)

                people_from_file: list[str] = read_to_list(file=people_datei)
                print_list(l=people_from_file)
                print_line(10)
                wait_for_input(key=0)
                break
            
            elif commando == 6:
                print("Autoliste lesen...")
                print_line(10)
                autos_from_file: list[str] = read_to_list(file=autos_datei)
                print_list(l=autos_from_file)
                print_line(10)
                wait_for_input(key=0)
                break

            elif commando == 7:
                print("Kundelöschen...")
                print_line(10)

                people_from_file: list[str] = read_to_list(file=people_datei)

                print_list(l=people_from_file)

                person_id_to_delete: int = int(input("Kunden Id zu loeschen: "))

                rows_to_keep: list[str] = []

                for kunde in people_from_file:
                    if int(kunde[0]) != person_id_to_delete:
                        rows_to_keep.append(kunde)


                write_to_file(file=people_datei, l=rows_to_keep)

                print(f"Der Kunde {person_id_to_delete} wurde geloescht.")

                print_line(10)
                wait_for_input(key=0)
                break
            
            elif commando == 8:
                print("Autolöschen...")
                print_line(10)
                autos_from_file: list[str] = read_to_list(file=autos_datei)

                print_list(l=autos_from_file)

                auto_id_to_delete: int = int(input("Welche id? "))

                rows_to_keep: list[str] = []
                for auto in autos_from_file:
                    if int(auto[0]) != auto_id_to_delete:
                        rows_to_keep.append(auto)

                write_to_file(file=autos_datei, l=rows_to_keep)    

                print(f"Das Auto {auto_id_to_delete} wurde geloescht.")
                print_line(10)
                wait_for_input(key=0)
                break

            else:
                break

        if commando not in [x for x in range(1, 9)]:
            break

if __name__ == '__main__':
    main()
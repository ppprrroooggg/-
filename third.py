import csv

with open("student_new.csv") as input_file:
    data = list(csv.reader(input_file, delimiter=";"))[1:]

    id = input()
    flag = False

    while id != "СТОП":
        for el in data:
            if el[2] == id:
                surname, name = el[1].split()
                print(f"Проект №{id} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el[4]}")
                flag = True
                break

        if not flag:
            print("Ничего не найдено")

        id = input()
        flag = False
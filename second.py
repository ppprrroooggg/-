import csv

with open("student_new.csv") as file:
    data = list(csv.reader(file, delimiter=";"))[1:]

    #print(data)

    for el in data:
        if el[4] == "":
            print(el)

    #сортировка вставками
    for i in range(len(data)):
        temp = data[i]
        j = i - 1

        while (j >= 0 and float(temp[4]) > float(data[j][4])):
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = temp

    grade = 10
    n = 0

    for el in data:
        if el[3][:2] == str(grade):
            surname, name = el[1].split()
            print(f"{n + 1} место: {name[0]}. {surname}")
            n += 1

        if n == 3:
            break
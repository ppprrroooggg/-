import csv

with open("students.csv") as file, open("student_new.csv", "a", newline="") as res_file:
    data = list(csv.reader(file, delimiter=";"))

    #print(data)

    selected_name = "Боткин Денис"
    summ, count = 0, 0

    for el in data[1:]:
        if el[4] != "":
            summ += int(el[4])
            count += 1

        if el[1] == selected_name:
            print(f"Ты получил: {el[4]}, за проект - {el[2]}")

    average = round(summ / count, 3)
    #print(average)

    res_writer = csv.writer(res_file, delimiter=";")

    '''for el in data:
        #res_writer.writerow(el if el[4] != "" else el[:4] + [str(average)])

        if el[4] != "":
            res_writer.writerow(el)
        else:
            res_writer.writerow(el[:4] + [str(average)])
            print(el[:4] + [str(average)])'''

    for i in range(len(data)):
        el = data[i]

        if el[4] == "":
            el[4] = str(average)

        res_writer.writerow(el)

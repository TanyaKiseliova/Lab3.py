def task1():
    with open("F1.txt", "w") as f1:
        while True:
            line = input("Введите строку (пустая строка для завершения ввода): ")
            if not line:
                break
            f1.write(line + "\n")

    with open("F2.txt", "w") as f2:
        with open("F1.txt", "r") as f1:
            for line in f1:
                if not any(char.isdigit() for char in line):
                    f2.write(line)

    with open("F2.txt", "r") as f2:
        lines = f2.readlines()
        if lines:
            last_line = lines[-1].strip()
            word_count = len(last_line.split())
            print("Количество слов в последней строке файла F2: ", word_count)
        else:
            print("Файл F2 пуст.")

def task2():
    try:
        with open("Клиент банка.txt", "w") as file:
            file.write("Киселёва 100000 25.09.2023\n")
            file.write("Воронович 1281 02.09.2021\n")
            file.write("Иовчик 0 15.08.2022\n")
            file.write("Молоткова 5000 01.07.2023\n")
            file.write("Луферчик 150 20.07.2022\n")
            file.write("Жданов 0 21.08.2023\n")

        total_investment = 0

        with open("Клиент банка.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split()

                if len(parts) == 3:
                    last_name, balance, _ = parts
                    balance = int(balance)

                    if balance == 0:
                        print(last_name)

                    total_investment += balance

        print("Общая сумма вложений всех клиентов: ", total_investment)

    except IOError:
        print("Произошла ошибка")


def task3():
    subject_dict = {}

    try:
        with open("subjects.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(":")
            if len(parts) == 2:
                subject_name = parts[0].strip()
                lessons_info = parts[1].strip().split()

                total_lessons = 0

                for lesson_info in lessons_info:
                    lesson_count = lesson_info.split("(")[0]
                    if lesson_count.isdigit():
                        total_lessons += int(lesson_count)

                subject_dict[subject_name] = total_lessons

        print(subject_dict)

    except IOError:
        print("Произошла ошибка")

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def inputInt(description):
    str = input(description)
    while not isInt(str):
        print("Некорректный ввод, введите только числа из диапазона")
        str = input()
    return int(str)

def main():
    isWork = True

    while isWork:
        print("1. 1 задание, F1, F2")
        print("2. 2 задание, вложения клиентов банка")
        print("3. 3 задание, учебные предметы")
        print("4. Выход")

        match (inputInt("Выберите вариант: ")):
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                isWork = False
            case _:
                print("Некорректный ввод")

main()
from typing import List
import numpy as np
from copy import deepcopy

BIT_SIZE = 16


def find_l(prev_g: int, prev_l: int, digit_a: int, digit_S: int) -> int:
    if prev_l:
        return int(prev_l)
    return int(digit_a and not digit_S and not prev_g)


def find_g(prev_g: int, prev_l: int, digit_a: int, digit_S: int) -> int:
    if prev_g:
        return int(prev_g)
    return not digit_a and digit_S and not prev_l


def sort_by_second_index(item):
    return item[1]


def sumBinaryNumbers(firstBinaryNumber: str, secondBinaryNumber: str) -> List:
    remainingBit = 0
    binaryNumberResult = []
    if len(firstBinaryNumber) > len(secondBinaryNumber):
        secondBinaryNumber[len(firstBinaryNumber)] = 0
    elif len(firstBinaryNumber) < len(secondBinaryNumber):
        firstBinaryNumber[len(secondBinaryNumber)] = 0

    firstBinaryNumber = list(reversed(firstBinaryNumber))
    secondBinaryNumber = list(reversed(secondBinaryNumber))

    for bits in range(len(firstBinaryNumber)):

        if (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 0 and remainingBit == 0)\
                or (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 0 and remainingBit == 1)\
                or (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 0 and remainingBit == 1)\
                or (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 1 and remainingBit == 0)\
                or (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 1 and remainingBit == 1):
            binaryNumberResult.append(0)
        elif (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 1 and remainingBit == 0)\
                or  (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 0 and remainingBit == 0):
            binaryNumberResult.append(1)
        elif firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 1 and remainingBit == 1:
            binaryNumberResult.append(1)
            remainingBit = 1
        elif firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 0 and remainingBit == 1:
            binaryNumberResult.append(1)
            remainingBit = 0

    binaryNumberResult = list(reversed(binaryNumberResult))    
    return binaryNumberResult    


def get_second_item(item):
    return item[1]


class AssociativeMemorySolver:

    def __init__(self, data: List, address: int):
        self.matrix = data
        self.address = address
        self.g = self.l = 0
        self.diagonal = False

    def search_pattern(self) -> None:
        self.g = self.l = 0
        tick_of_matching = {}
        print("Введите строку(0,1): ")
        example_data = input()
        for literal in example_data:
            if literal not in ('0', '1'):
                print("Ошибка. Неверные данные")
                return

        if len(example_data) > BIT_SIZE:
            example_data = example_data[0:BIT_SIZE]
        elif len(example_data) < BIT_SIZE:
            example_data = example_data.zfill(BIT_SIZE)

        print("Строка для поиска по соотвествию :")
        print(example_data)

        matrix_copy, diagonal_data = deepcopy(self.matrix), self.diagonal

        if diagonal_data:
            self.convert_to_straight(0)

        for num in range(self.matrix.shape[0]):
            tick_of_matching[f"{self.matrix[num]}"] = self.algorithm_of_accordance(matrix_copy[num], example_data, num)

        if diagonal_data:
            self.convert_to_diagonal(0)
            
        print("Строки с максимальным совпадением символов :")
        print(sorted(tick_of_matching.items(), key=get_second_item)[-3:])

    def convert_to_straight(self, key: int = 0) -> None:

        matrix_copy = deepcopy(self.matrix)
        self.matrix = []
        for str_number, string in enumerate(matrix_copy):
            string = list(string)
            self.matrix.append(string[str_number:] + string[:str_number])

        self.matrix = np.array(self.matrix)
        self.diagonal = False
        if key:
            print(self.matrix)
        
    def convert_to_diagonal(self, key: int) -> None:
        matrix_copy = deepcopy(self.matrix)
        self.matrix = []
        for str_number, string in enumerate(matrix_copy):
            string = list(string)
            self.matrix.append(string[(len(string) - str_number):] + string[:(len(string) - str_number)])
        self.matrix = np.array(self.matrix)
        self.diagonal = True
        if key:
            print(self.matrix)

    def logic_operations(self) -> None:
        type_list = [
            "Выберите тип операции:",
            "1 - константа 1",
            "2 - константа 0",
            "3 - Новый аргумент",
            "4 - Отрицание нового аргумента"
        ]
        print("\n".join(type_list))
        type_of_operations = int(input())
        print("Выберите столбец : ")
        column_number = int(input())
        match type_of_operations:
            case 1:
                for digit in range(len(self.matrix[column_number])):
                    self.matrix[column_number][digit] = 1
                print(self.matrix.T)
            case 2:
                for digit in range(len(self.matrix[column_number])):
                    self.matrix[column_number][digit] = 0
                print(self.matrix.T)
            case 3:
                self.positive_arg(column_number)
            case 4:
                self.negative_arg(column_number)

    def positive_arg(self, column_number: int) -> None:
        diagonal_data = self.diagonal
        if diagonal_data:
            self.convert_to_straight()
        print("Входящее значение : ")
        argument = input()
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        for str_number, digit in enumerate(self.matrix[column_number]):
            self.matrix[column_number][str_number] = argument[str_number]
        if diagonal_data:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

    def negative_arg(self, column_number: int) -> None:
        diagonal_data = self.diagonal
        if diagonal_data:
            self.convert_to_straight(0)
        print("Входящее значение: ")
        argument = input()
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        argument = argument.replace("1", "2").replace("0", "1").replace("2", "0")
        for str_number, digit in enumerate(self.matrix[column_number]):
            self.matrix[column_number][str_number] = argument[str_number]
        if diagonal_data:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

    def sum_of_fields(self) -> None:
        print("Введите слово ")
        example_data = input()[:3]
        if self.diagonal:
            self.convert_to_straight(0)
        for str_number, string in enumerate(self.matrix):
            if np.array2string(string, separator='')[1:-1].replace(' ', '')[:3] == example_data:
                self.matrix[str_number][11:16] = Associative_memory_solver.sum_or_diff_nums(
                    self.matrix[str_number][3:7], self.matrix[str_number][7:11])
            if self.diagonal:
                self.convert_to_diagonal(0)
        result = self.matrix.T        
        print(result)

    def write_word(self):
        print("Строка:")
        word = np.array(list(input().zfill(16)[:16]), dtype=int)
        print(word)
        num_of_word = int(input())
        diagonal_info = self.diagonal
        if self.diagonal:
            self.convert_to_straight(0)
        self.matrix[num_of_word] = word
        if diagonal_info:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

    def algorithm_of_accordance(self, matrix_string: List, data: List, str_number: int) -> int:

        tick = pos_of_break = 0

        if not self.diagonal:
            for digit, value_of_digit in enumerate(data):
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
        elif self.diagonal:
            for digit, value_of_digit in enumerate(data[str_number:]):
                pos_of_break = digit
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
            for digit, value_of_digit in enumerate(data[:str_number]):
                if value_of_digit == str(matrix_string[pos_of_break + digit]):
                    tick += 1
        return tick

    def read_word(self) -> None:
        print("Введите номер строки:")
        num_of_word = int(input())
        diagonal_info = self.diagonal
        if self.diagonal:
            self.convert_to_straight(0)
        print(self.matrix[num_of_word])
        if diagonal_info:
            self.convert_to_diagonal(0)


    def read_write_operations(ams_solver: AssociativeMemorySolver) -> None:
        print('\n'.join(["Выберите задачу:", "0 - Чтение слова", "1 - Запись слова"]))
        if int(input()):
            ams_solver.write_word()
        else:
            ams_solver.read_word()

def choosing_task(ams_solver: AssociativeMemorySolver, matrix) -> None:

    task_list = (
        "Выберите действие :",
        "1 - поиск по соответствию",
        "2 - преобразование в диагональную",
        "3 - преобразование в прямую",
        "4 - логические операции",
        "5 - сумма цифр",
        "6 - Чтение или запись столбца",
        "Выход на любую другую кнопку"
    )

    while 424233423 == 424233423:
        print("\n".join(task_list))
        task = int(input())
        if task == 1:
            ams_solver.search_pattern()
        elif task == 2:
            ams_solver.convert_to_diagonal(1)
        elif task == 3:
            ams_solver.convert_to_straight(1)
        elif task == 4:
            ams_solver.logic_operations()
        elif task == 5:
            ams_solver.sum_of_fields()
        elif task == 6:
            read_write_operations(ams_solver)
        else:
            return
            
def main():
    rows = columns = 16
    matrix = np.random.randint(2, size=(rows, columns))
    address_of_searching = np.random.randint(2, size=rows)
    ams_solver = AssociativeMemorySolver(matrix, address_of_searching)
    result = matrix.T
    print(result)
    choosing_task(ams_solver, matrix)

main()            
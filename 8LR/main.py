from copy import deepcopy
import numpy as np
from typing import List

task_list = [
    "Выберите действие :",
    "1 - поиск по соответствию",
    "2 - преобразование в диагональную",
    "3 - преобразование в прямую",
    "4 - логические операции",
    "5 - сумма цифр",
    "6 - Чтение или запись столбца"
]

BIT_SIZE = 16

def find_g(prev_g:int, prev_l:int, digit_a:int, digit_S:int) ->int:
    g = int(prev_g or (not digit_a and digit_S and not prev_l))
    return g


def find_l(prev_g:int, prev_l:int, digit_a:int, digit_S:int) ->int:
    l = int(prev_l or (digit_a and not digit_S and not prev_g))
    return l

 
def sum_or_diff_nums(num1 :int, num2 :int) ->List: 
    summ = ""
    carry = 0
    for i in reversed(range(0, len(num1))):
        if (int(num1[i]) + int(num2[i]) == 1) and (carry == 0):
            summ = "1" + summ
        elif (int(num1[i]) + int(num2[i]) == 1) and (carry > 0):
            summ = "0" + summ
        elif (int(num1[i]) + int(num2[i]) == 2) and (carry > 0):
            summ = "1" + summ
        elif (int(num1[i]) + int(num2[i]) == 0) and (carry > 0):
            summ = "1" + summ
            carry -= 1
        elif (int(num1[i]) + int(num2[i]) == 0) and (carry == 0):
            summ = "0" + summ
        elif (int(num1[i]) + int(num2[i]) == 2) and (carry == 0):
            summ = "0" + summ
            carry += 1
    if carry > 0:
        summ = "1" + summ
    elif carry == 0:
        summ = "0" + summ
    summ = np.array([num for num in summ])
    return summ
class Associative_memory_solver:
    def __init__(self, data :List, address:int):
        self.matrix = data
        self.address = address
        self.g, self.l = 0, 0
        self.diagonal = False
        

   
    def search_pattern(self):
        self.g, self.l = 0, 0
        tick_of_matching = {}
        example_data = input("Введите строку(0,1): ")
        for char in str(example_data):
            if char != '0' and char != '1':
                print("Ошибка.Неверные данные \n")
                return 0
        if len(example_data) > BIT_SIZE:
            example_data = example_data[0:BIT_SIZE]
        elif len(example_data) < BIT_SIZE:
            example_data = example_data.zfill(BIT_SIZE)
        print(f"Строка для поиска по соотвествию : {example_data}")
        matrix_copy, diagonal_data = deepcopy(self.matrix), self.diagonal
        if diagonal_data is True:
            self.convert_to_straight()
        for num in range(self.matrix.shape[0]):
            tick_of_matching.update(
                {f"{self.matrix[num]}": self.reccure_algorithm_for_accordance(matrix_copy[num], example_data, num)})
        if diagonal_data is True:
            self.convert_to_diagonal()
        print(
            f"Строки с максимальным совпадением символов : \n{sorted(tick_of_matching.items(), key=lambda item: item[1])[-3:]}\n")

    def convert_to_straight(self,key:int):
        matrix_copy = deepcopy(self.matrix)
        self.matrix = []
        for num_of_string, string in enumerate(matrix_copy):
            string = list(string)
            self.matrix.append(string[num_of_string:] + string[:num_of_string])
        self.matrix = np.array(self.matrix)
        self.diagonal = False
        if key == 1:
            print(self.matrix)
        
    def convert_to_diagonal(self,key:int):
        matrix_copy = deepcopy(self.matrix)
        self.matrix = []
        for num_of_string, string in enumerate(matrix_copy):
            string = list(string)
            self.matrix.append(string[(len(string) - num_of_string):] + string[:(len(string) - num_of_string)])
        self.matrix = np.array(self.matrix)
        self.diagonal = True
        if key == 1:
            print(self.matrix)

    def logic_operations(self):
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
        num_of_column = int(input())
        match type_of_operations:
            case 1:
                for digit in range(len(self.matrix[num_of_column])):
                    self.matrix[num_of_column][digit] = 1
                print(self.matrix.T)
            case 2:
                for digit in range(len(self.matrix[num_of_column])):
                    self.matrix[num_of_column][digit] = 0
                print(self.matrix.T)
            case 3:
                self.positive_arg(num_of_column)
            case 4:
                self.negative_arg(num_of_column)

    def positive_arg(self, num_of_column:int):
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight()
        argument = input("Входящее значение : ")
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        for num_of_string, digit in enumerate(self.matrix[num_of_column]):
            self.matrix[num_of_column][num_of_string] = argument[num_of_string]
        if diagonal_data is True:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

    def negative_arg(self, num_of_column:int):
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight(0)
        argument = input("Входящее значение: ")
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        argument = argument.replace("1", "2").replace("0", "1")
        argument = argument.replace("2", "0")
        for num_of_string, digit in enumerate(self.matrix[num_of_column]):
            self.matrix[num_of_column][num_of_string] = argument[num_of_string]
        if diagonal_data is True:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

   

    def sum_of_fields(self):
        example_data = input("Введите слово ")[:3]
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight(0)
        for num_of_string, string in enumerate(self.matrix):
            if np.array2string(string, separator='')[1:-1].replace(' ', '')[0:3] == example_data:
                self.matrix[num_of_string][11:16] = Associative_memory_solver.sum_or_diff_nums(
                    self.matrix[num_of_string][3:7], self.matrix[num_of_string][7:11])
            if diagonal_data is True:
                self.convert_to_diagonal(0)
        print(self.matrix.T)

    def reccure_algorithm_for_accordance(self, matrix_string :List, data : List, num_of_string:int) ->int:
        tick, pos_of_break = 0, 0
        if self.diagonal is False:
            for digit, value_of_digit in enumerate(data):
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
        if self.diagonal is True:
            for digit, value_of_digit in enumerate(data[num_of_string:]):
                pos_of_break = digit 
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
            for digit, value_of_digit in enumerate(data[:num_of_string]):
                if value_of_digit == str(matrix_string[pos_of_break + digit]):
                    tick += 1
        return tick

    def read_write_operations (self):
        menu_options = [
            "1 - Чтение слова",
            "2 - Чтение столбца",
            "3 - Запись слова",
            "4 - Запись столбца"
        ]

        print("Выберите задачу:")
        for option in menu_options:
            print(option)
        
        type_of_operation = int(input())
        match type_of_operation:
            case 1:
                self.read_word()
            case 2:
                self.read_column()
            case 3:
                self.write_word()
            case 4:
                self.write_column()

    def read_word(self):
        num_of_word = int(input("Номер строки : "))
        diagonal_info = self.diagonal
        if self.diagonal is True:
            self.convert_to_straight(0)
        print(self.matrix[num_of_word])
        if diagonal_info is True:
            self.convert_to_diagonal(0)

    def read_column(self):
        num_of_col = int(input("Номер столбца : "))
        print(self.matrix[num_of_col])

    def write_word(self):
        word = np.array(list(input("Строка:").zfill(16)[:16]), dtype=int)
        num_of_word = int(input("Номер строки : "))
        diagonal_info = self.diagonal
        if self.diagonal is True:
            self.convert_to_straight(0)
        self.matrix[num_of_word] = word
        if diagonal_info is True:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

    def write_column(self):
        column = np.array(list(input("Столбец:").zfill(16)[:16]), dtype=int)
        num_of_col = int(input("Номер столбца: "))
        self.matrix[num_of_col] = column
        print(self.matrix.T)



def main():
    rows, columns = 16, 16
    matrix = np.random.randint(2, size=(rows, columns))
    address_of_searching = np.random.randint(2, size=16)
    ams_solver = Associative_memory_solver(matrix, address_of_searching)
    
    print(matrix.T)
    choosing_task(ams_solver,matrix)
    
def choosing_task(ams_solver,matrix):
    while True:
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
            ams_solver.read_write_operations()
            
        else:
            break
            
main()            
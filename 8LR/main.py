from copy import deepcopy
import numpy as np
from typing import List


word = "Номер строки : "

BIT_SIZE = 16

def find_g(prev_g:int, prev_l:int, digit_a:int, digit_S:int) ->int:
    if prev_g:
        g = int(prev_g)
    else:
        if not digit_a and digit_S and not prev_l:
            g = 1
        else:
            g = 0
    return g


def find_l(prev_g:int, prev_l:int, digit_a:int, digit_S:int) ->int:
    if prev_l:
        l = int(prev_l)
    else:
        l = int(digit_a and not digit_S and not prev_g)
    return l

def sort_by_second_index(item):
    return item[1]

def sumBinaryNumbers( firstBinaryNumber :str, secondBinaryNumber :str) ->List :
    remainingBit = 0
    binaryNumberResult = []
    if len(firstBinaryNumber) > len(secondBinaryNumber):
        secondBinaryNumber[len(firstBinaryNumber)] = 0
    elif len(firstBinaryNumber) < len(secondBinaryNumber):
        firstBinaryNumber[len(secondBinaryNumber)] = 0
    firstBinaryNumber = list(reversed(firstBinaryNumber))
    secondBinaryNumber = list(reversed(secondBinaryNumber))
    for bits in range(len(firstBinaryNumber)):
          
        if(firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 0 and remainingBit == 0):
            binaryNumberResult.append(0)
        elif (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 1 and remainingBit == 0):
            binaryNumberResult.append(1)
        elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 0 and remainingBit == 0):
            binaryNumberResult.append(1)
        elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 1 and remainingBit == 0):
            binaryNumberResult.append(0)
            remainingBit = 1
        elif (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 0 and remainingBit == 1):
            binaryNumberResult.append(1)
            remainingBit = 0
        elif (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 1 and remainingBit == 1):
            binaryNumberResult.append(0)
            remainingBit = 1
        elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 0 and remainingBit == 1):
            binaryNumberResult.append(0)
            remainingBit = 1
        elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 1 and remainingBit == 1):
            binaryNumberResult.append(1)
            remainingBit = 1

    binaryNumberResult = list(reversed(binaryNumberResult))    
    return binaryNumberResult    

def get_second_item(item):
    return item[1]

class Associative_memory_solver:
    def __init__(self, data :List, address:int):
        self.matrix = data
        self.address = address
        self.g, self.l = 0, 0
        self.diagonal = False
        

   
    def search_pattern(self):
        self.g, self.l = 0, 0
        tick_of_matching = {}
        print("Введите строку(0,1): ")
        example_data = input()
        for literal in str(example_data):
            if literal is not '0' and literal is not '1':
                print("Ошибка.Неверные данные ")
                return 0
        if len(example_data) > BIT_SIZE:
            example_data = example_data[0:BIT_SIZE]
        elif len(example_data) < BIT_SIZE:
            example_data = example_data.zfill(BIT_SIZE)

        print("Строка для поиска по соотвествию :")
        print(example_data)

        matrix_copy, diagonal_data = deepcopy(self.matrix), self.diagonal

        if diagonal_data is True:
            self.convert_to_straight(0)

        for num in range(self.matrix.shape[0]):
            tick_of_matching.update(
                {f"{self.matrix[num]}": self.algorithm_of_accordance(matrix_copy[num], example_data, num)})
        if diagonal_data is True:
            self.convert_to_diagonal(0)
            
        print(
            f"Строки с максимальным совпадением символов : \n{sorted(tick_of_matching.items(),key=get_second_item )[-3:]}\n")
        

    def convert_to_straight(self,key:int):
        matrix_copy = deepcopy(self.matrix)
        self.matrix = []
        for str_number, string in enumerate(matrix_copy):
            string = list(string)
            self.matrix.append(string[str_number:] + string[:str_number])
        self.matrix = np.array(self.matrix)
        self.diagonal = False
        if key == 1:
            print(self.matrix)
        
    def convert_to_diagonal(self,key:int):
        matrix_copy = deepcopy(self.matrix)
        self.matrix = []
        for str_number, string in enumerate(matrix_copy):
            string = list(string)
            self.matrix.append(string[(len(string) - str_number):] + string[:(len(string) - str_number)])
        self.matrix = np.array(self.matrix)
        self.diagonal = True
        if key == 1:
            print(self.matrix)

    def logic_operations(self):
        
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

    def positive_arg(self, column_number:int):
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight()
        print("Входящее значение : ")
        argument = input()
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        for str_number, digit in enumerate(self.matrix[column_number]):
            self.matrix[column_number][str_number] = argument[str_number]
        if diagonal_data is True:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

    def negative_arg(self, column_number:int):
        diagonal_data = self.diagonal
        if diagonal_data is True:
            self.convert_to_straight(0)
        print("Входящее значение: ")    
        argument = input()
        if len(argument) > BIT_SIZE:
            argument = argument[0:BIT_SIZE]
        elif len(argument) < BIT_SIZE:
            argument = argument.zfill(BIT_SIZE)
        argument = argument.replace("1", "2").replace("0", "1")
        argument = argument.replace("2", "0")
        for str_number, digit in enumerate(self.matrix[column_number]):
            self.matrix[column_number][str_number] = argument[str_number]
        if diagonal_data is True:
            self.convert_to_diagonal(0)
        print(self.matrix.T)

   

    def sum_of_fields(self):
        print("Введите слово ")
        example_data = input()[:3]
        diagonal_data = self.diagonal
        pattern = np.array2string(string, separator='')[1:-1].replace(' ', '')[0:3]
        if diagonal_data is True:
            self.convert_to_straight(0)
        for str_number, string in enumerate(self.matrix):
            if  pattern == example_data:
                self.matrix[str_number][11:16] = Associative_memory_solver.sum_or_diff_nums(
                    self.matrix[str_number][3:7], self.matrix[str_number][7:11])
            if diagonal_data is True:
                self.convert_to_diagonal(0)
        result = self.matrix.T        
        print(result)

    def algorithm_of_accordance(self, matrix_string :List, data : List, str_number:int) ->int:

        tick, pos_of_break = 0, 0

        if self.diagonal is False:
            for digit, value_of_digit in enumerate(data):
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
        elif self.diagonal is True:
            for digit, value_of_digit in enumerate(data[str_number:]):
                pos_of_break = digit 
                if value_of_digit == str(matrix_string[digit]):
                    tick += 1
            for digit, value_of_digit in enumerate(data[:str_number]):
                if value_of_digit == str(matrix_string[pos_of_break + digit]):
                    tick += 1
        else:
            print("Ошибка счетчика ")            
        return tick


    def read_word(self):
      
        print(word)
        num_of_word = int(input())
        diagonal_info = self.diagonal
        if self.diagonal is True:
            self.convert_to_straight(0)
        matrix_word = self.matrix[num_of_word]    
        print(matrix_word)
        if diagonal_info is True:
            self.convert_to_diagonal(0)

    def write_word(self):
        word_print = "Строка:"
        print(word_print)
        word = np.array(list(input().zfill(16)[:16]), dtype=int)
        print(word)
        num_of_word = int(input())
        diagonal_info = self.diagonal
        if self.diagonal is True:
            self.convert_to_straight(0)
        self.matrix[num_of_word] = word
        if diagonal_info is True:
            self.convert_to_diagonal(0)
        result = self.matrix.T    
        print(result)

  
type_list = [
            "Выберите тип операции:",
            "1 - константа 1",
            "2 - константа 0",
            "3 - Новый аргумент",
            "4 - Отрицание нового аргумента"
        ]

task_list = [
    "Выберите действие :",
    "1 - поиск по соответствию",
    "2 - преобразование в диагональную",
    "3 - преобразование в прямую",
    "4 - логические операции",
    "5 - сумма цифр",
    "6 - Чтение или запись столбца"
]

menu_options = [
            "1 - Чтение слова",
            "2 - Запись слова"
        ]


def main():
    rows, columns = 16, 16
    matrix = np.random.randint(2, size=(rows, columns))
    address_of_searching = np.random.randint(2, size=rows )
    ams_solver = Associative_memory_solver(matrix, address_of_searching)
    result =  matrix.T
    print(result)
    choosing_task(ams_solver,matrix)

def read_write_operations (ams_solver):
        

        print("Выберите задачу:")
        for option in menu_options:
            print(option)
        
        type_of_operation = int(input())
        
        if type_of_operation == 1:
            ams_solver.read_word()
        elif type_of_operation == 2:
            ams_solver.write_word()
        
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
            read_write_operations(ams_solver)
            
        else:
            break
            
main()            
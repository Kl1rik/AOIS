'''121702 Шершень'''
import itertools
from itertools import product
from kmap import k_map
from quine import main as calculate_tabular
dictionary = {0: [], 1: []}
b_dictionary = {0: [], 1: []}


def sum_binary(x,y,z):
    expression_result = 0
    buffer = 0
    if x == 0 and y == 0 and z == 0 :
        expression_result = 0
        buffer = 0
    elif x == 0 and y == 0 and z == 1 :
        expression_result = 1
        buffer = 0
    elif x == 0 and y == 1 and z == 0 :
        expression_result = 1
        buffer = 0
    elif x == 0 and y == 1 and z == 1 :
        expression_result = 0
        buffer = 1
    elif x == 1 and y == 0 and z == 0 :
        expression_result = 1
        buffer = 0
    elif x == 1 and y == 0 and z == 1 :
        expression_result = 0
        buffer = 1          
    elif x == 1 and y == 1 and z == 0 :
        expression_result = 0
        buffer = 1
    elif x == 1 and y == 1 and z == 1 :
        expression_result = 1
        buffer = 1  
    return expression_result,buffer       
  
def sumBinaryNumbers( firstBinaryNumber, secondBinaryNumber):
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

def intToBin(num):
    if num > 0:
        flag = 0
    elif num < 0:
        flag = 1
    num = str(num)    
    num = num.replace("-","")
    num = int(num)
    bin = []
    while num > 0:
        bin.append(num % 2)
        num //= 2
    bin.reverse()
    l = len(bin) -1 
    if flag == 0:
        addition_sign_bit =  [0]
        bin = addition_sign_bit + bin
    elif flag == 1:
        for bits in range(len(bin)):
            if bin[bits] == 0:
                bin[bits] = 1
            elif bin[bits] == 1:
                bin[bits] = 0

        if bin[l] == 0:        
            one = [0]*(len(bin) - 1) + [1]
            bin = sumBinaryNumbers(bin,one)    
        addition_sign_bit =  [1]
        bin = addition_sign_bit + bin   
        bin = [str(i) for i in bin]
    return bin      

def solve_summator(dictionary1,dictionary2):    
    s = 'A+B+C' 
    buffer = "П"
    variables = list(sorted(set([c for c in s if c.isalpha()])))
    n = ['!', '']
    print(*variables,s,buffer,sep = ' ')

    k = ""
    k1 = "" 
    sknf = []
    sdnf = []
    sknf_buffer = []
    sdnf_buffer = [] 
    for num, combination in enumerate(itertools.product([0, 1], repeat=len(variables))):
        values = list(combination)
        
        variables_dict = dict(zip(variables, values))
        
        expression_result , buffer = sum_binary(values[0],values[1],values[2])
        
        dictionary1[expression_result].append(num)
        dictionary2[buffer].append(num)
        if expression_result == 0:
            sknf.append(f"{n[values[0]]}A+{n[values[1]]}B+{n[values[2]]}C")
        elif expression_result == 1:
            sdnf.append(f"{n[values[0]]}A*{n[values[1]]}B*{n[values[2]]}C")
            
        if  buffer == 0:
            sknf_buffer.append(f"{n[values[0]]}A+{n[values[1]]}B+{n[values[2]]}C")
        elif buffer == 1:
            sdnf_buffer.append(f"{n[values[0]]}A*{n[values[1]]}B*{n[values[2]]}C")  
            
        print(values, expression_result,buffer)


        

    

    sknf = '*'.join(sknf)
    sdnf = '+'.join(sdnf)
    sknf_buffer = '*'.join(sknf_buffer)
    sdnf_buffer = '+'.join(sdnf_buffer)
    print(dictionary1)
    print(dictionary2)
    print("Полученная СКНФ для суммы :" )
    print(sknf)
    print("Полученная СДНФ для суммы :")
    print(sdnf)
    print("Полученная СКНФ для переноса :" )
    print(sknf_buffer)
    print("Полученная СДНФ для переноса : ")
    print(sdnf_buffer)

    print("Минимизируем полученные функции :")
    mt0 = dictionary1.get(0)
    mt1 = dictionary2.get(0)
    k =  k_map(mt0,1,0)

    k1 = k_map(mt1,1,0)

def solve_bcd():
    string_bcd = 'A+B+C+D'
    result =[] 
    variables_bcd = list(sorted(set([c for c in string_bcd if c.isalpha()])))
    n = ['!', '']
    matrix = []
    nine = [1,0,0,1]
    matrix_bcd = []
    sknf = []
    sdnf = []
    for num, combination in list(enumerate(itertools.product([0, 1], repeat=len(variables_bcd))))[:10]:
        values_bcd = list(combination)
        matrix_bcd.append(values_bcd)
        variables_dict_bcd = dict(zip(variables_bcd, values_bcd))
        
        expression_result = sumBinaryNumbers(values_bcd,nine)
        matrix.append(expression_result)
        print(values_bcd,expression_result)
        
    print('*'.join(sknf))
    print('+'.join(sdnf))
    d1, d2, d3, d4 = ({0: [], 1: []} for _ in range(4))
    l = [d1, d2, d3, d4]
    for i in range(0, 10):
        for j in range(len(matrix[i])):
            l[j][matrix[i][j]].append(i)


    dicts = []
    print("Полученные числовые формы СКНФ и СДНФ :")
    print(*l,sep= '\n')
    for dic in l:
        d = {}
        for k, v in dic.items():          
            for elem in v:
                d[elem] = k
        else:
            dicts.append(d)    

    # print(*dicts, sep='\n')


    for val, d, num in zip(list(zip(*matrix)), dicts, range(1, 10)):
        sknf = []
        sdnf = []
        for i in range(10):
            if val[i] == 0: 
                sknf.append(f"{n[d[0]]}A+{n[d[1]]}B+{n[d[2]]}C+{n[d[3]]}D")
            else:
                sdnf.append(f"{n[d[0]]}A*{n[d[1]]}B*{n[d[2]]}C*{n[d[3]]}D")

        print()
        print(f"Y{num}")
        print("Полученная СКНФ:")
        print('*'.join(sknf))
        print("Полученная СДНФ:")
        print("+".join(sdnf))
    print("Y1")    
    calculate_tabular(d1.get(0),0)
    calculate_tabular(d1.get(1),1)
    print("Y2")   
    calculate_tabular(d2.get(0),0)
    calculate_tabular(d2.get(1),1)
    print("Y3")   
    calculate_tabular(d3.get(0),0)
    calculate_tabular(d3.get(1),1)
    print("Y4")   
    calculate_tabular(d4.get(0),0)
    calculate_tabular(d4.get(1),1)

solve_summator(dictionary,b_dictionary)
'''         Задание 2           '''
print("Получим минимизироанные функции для преобразователя 8421(BCD) кодов")
solve_bcd()
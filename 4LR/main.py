'''121702 Шершень'''

import itertools
from itertools import product
from kmap import k_map
s = 'A+B+C'

string_bcd = 'A+B+C+D'
result =[] 
variables = list(sorted(set([c for c in s if c.isalpha()])))
variables_bcd = list(sorted(set([c for c in string_bcd if c.isalpha()])))
buffer = "П"
print(*variables, s, buffer , sep=' ')

k = ""
k1 = "" 
sknf = []
sdnf = []
sknf_buffer = []
sdnf_buffer = [] 
n = ['!', '']
dictionary = {0: [], 1: []}
b_dictionary = {0: [], 1: []}
bcd_dictionary_pt1 = {0:[],1:[]}
bcd_dictionary_pt2 = {0:[],1:[]}
d_lf ={0:["000"] , 1:["001"] , 2:["010"] , 3:["011"] , 4:["100"] ,5:["101"],6:["110"],7:["1 1 1"]}

def sum_binary(x:int,y:int,z:int):
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

     
for num, combination in enumerate(itertools.product([0, 1], repeat=len(variables))):
    values = list(combination)
    
    variables_dict = dict(zip(variables, values))
    
    expression_result , buffer = sum_binary(values[0],values[1],values[2])
    
    
    dictionary[expression_result].append(num)
    b_dictionary[buffer].append(num)
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
print(dictionary)
print(b_dictionary)
print("Полученная СКНФ для суммы" )
print(sknf)
print("Полученная СДНФ для суммы")
print(sdnf)
print("Полученная СКНФ для переноса" )
print(sknf_buffer)
print("Полученная СДНФ для переноса")
print(sdnf_buffer)
print("Минимизируем полученные функции")
mt0 = dictionary.get(0)
mt1 = b_dictionary.get(0)
k =  k_map(mt0,1,0)

k1 = k_map(mt1,1,0)

# nine = intToBin(9)
nine = [1,0,0,1]
for num, combination in enumerate(itertools.product([0, 1], repeat=len(variables_bcd))):
    values_bcd = list(combination)
    
    variables_dict_bcd = dict(zip(variables_bcd, values_bcd))
    
    
    expression_result = sumBinaryNumbers(values_bcd,nine)
    
    # expression_result , buffer = sum_binary(values[0],values[1],values[2])
    
    if num not in range(10,16):
        bcd_dictionary_pt1[expression_result[0]].append(num)
        bcd_dictionary_pt1[expression_result[1]].append(num)
        bcd_dictionary_pt2[expression_result[2]].append(num)
        bcd_dictionary_pt2[expression_result[3]].append(num)
    # b_dictionary[buffer].append(num)
    # if expression_result == 0:
    #     sknf.append(f"{n[values[0]]}A+{n[values[1]]}B+{n[values[2]]}C+{n[values[3]]}D")
    # elif expression_result == 1:
    #     sdnf.append(f"{n[values[0]]}A*{n[values[1]]}B*{n[values[2]]}C")
        
    # if  buffer == 0:
    #     sknf_buffer.append(f"{n[values[0]]}A+{n[values[1]]}B+{n[values[2]]}C")
    # elif buffer == 1:
    #     sdnf_buffer.append(f"{n[values[0]]}A*{n[values[1]]}B*{n[values[2]]}C")  
          
    print(values_bcd,expression_result)

print(bcd_dictionary_pt1)
print(bcd_dictionary_pt2)

# print(sumBinaryNumbers(nine,eight))
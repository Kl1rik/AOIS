from functools import reduce
import struct

def intToBin32(i):
    return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)

    

def iterationCounter(i):
    count = 0
    if abs(i) < 4 :
        count = 2
    elif 4 <= abs(i) < 8:
        count = 3
    elif 8 <= abs(i) < 16:
        count = 4
    elif 16 <= abs(i) < 32:
        count = 5
     
    return count
def intToBin(i):
    count = 0
    if abs(i) < 4:
        count = 2
    elif 4 <= abs(i) < 8:
        count = 3
    elif 8 <= abs(i) < 16:
        count = 4
    elif 16 <= abs(i) < 32:
        count = 5

    return (bin(((1 << count+1) - 1) & i)[2:]).zfill(count+1)
def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]
def intFloatPointtoBin(i):

    return format(struct.unpack('!I', struct.pack('!f', i))[0], '032b')

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

def intToBin32SW(n):
    if n > 0:
        flag = 0
    elif n < 0:
        flag = 1
   
    n = str(n)    
    n = n.replace("-","")
    n = int(n)
    print(n)
    bin = []
   
    while n > 0:
        bin.append(n % 2)
        n //= 2
    bin.reverse()
    l = len(bin) -1 
    if flag == 0:
        addition_to_32_bit = (32 - len(bin)) * [0]
        bin = addition_to_32_bit + bin
    elif flag == 1:
        
        for bits in range(len(bin)):
            if bin[bits] == 0:
                bin[bits] = 1
            elif bin[bits] == 1:
                bin[bits] = 0

        if bin[l] == 0:        
            one = [0]*(len(bin) - 1) + [1]
            bin = sumBinaryNumbers(bin,one)    
        addition_to_32_bit = (32 - len(bin)) * [1]
        bin = addition_to_32_bit + bin    
    return bin
def intToBinSW(n):
    if n > 0:
        flag = 0
    elif n < 0:
        flag = 1
   
    n = str(n)    
    n = n.replace("-","")
    n = int(n)
    print(n)
    bin = []
   
    while n > 0:
        bin.append(n % 2)
        n //= 2
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
    return bin
def intFloatPointtoBinSW(i):
    str_i = str(i)
    list_i = str_i.split(".")
    a = list_i[0] 
    b = list_i[1]
    b = int(b)
    a = int(a)
    a = intToBinSW(a)
    b = intToBinSW(b)
    two_binary = [0]*(len(b) - 2) + [1,0]
    b = divideBinaryNumbers(b,two_binary)
    res = [a,b]
    return res   
def multiplicationBinaryNumbers(firstBinaryNumber,secondBinaryNumber,counter):

    buffer = [[0]*counter for i in range(counter)]
    print(buffer)
    for bits in range(len(secondBinaryNumber)):
        if secondBinaryNumber[bits] == 1:
          
            buffer[bits] = firstBinaryNumber + [0]*bits 
        elif secondBinaryNumber[bits] == 0:
           print("") 
    buffer = [[0]*(9-len(a))+a for a in buffer]
    
    return buffer            

def divideBinaryNumbers(firstBinaryNumber,secondBinaryNumber,secondBinaryNegativeNumber,counter):
    divideResult = []
    if(len(firstBinaryNumber)>len(secondBinaryNumber)):
        secondBinaryNumber = [0]*(len(firstBinaryNumber)-len(secondBinaryNumber)) + secondBinaryNumber
        secondBinaryNegativeNumber = [1] * (len(firstBinaryNumber) - len(secondBinaryNegativeNumber)) + secondBinaryNegativeNumber
    elif (len(firstBinaryNumber)<len(secondBinaryNumber)):
        firstBinaryNumber = [0]*(len(secondBinaryNumber)-len(firstBinaryNumber)) + firstBinaryNumber
    print("First",firstBinaryNumber)
    print("Second",secondBinaryNumber)
    partSolution = sumBinaryNumbers(firstBinaryNumber,secondBinaryNegativeNumber)
    print(partSolution)
    if partSolution[0] == 0 :
        print("знак +")
    elif partSolution[0] == 1 :
        print("знак +")
    for bits in range(counter+1):
        if partSolution[0] == 1:
            partSolution.append(0)
            partSolution.pop(0)
            partSolution = sumBinaryNumbers(partSolution,secondBinaryNumber)
            divideResult.append(0)
        elif partSolution[0] != 1:
            partSolution.append(0)
            partSolution.pop(0)
            partSolution = sumBinaryNumbers(partSolution,secondBinaryNegativeNumber)
            divideResult.append(1)
        
    return divideResult

def sumFloatingPointBinaryNumbers(firstBinaryNumber ,secondBinaryNumber  ):
    firstBinaryNumber = list(map(int,firstBinaryNumber))
    secondBinaryNumber = list(map(int, secondBinaryNumber))
    print("127",intToBin32(127))
    exponent1 = []
    exponent2 =[]
    mantissa1 = []
    mantissa2 = []
    for bits in range(0,8):
        exponent1.append(firstBinaryNumber[bits])
        exponent2.append(secondBinaryNumber[bits])
    for bits in range(10,len(firstBinaryNumber)):
        mantissa1.append(firstBinaryNumber[bits])
    for bits in range(10, len(firstBinaryNumber)):
        mantissa2.append(secondBinaryNumber[bits])
    print()
    count = 0
    negone = [1,1,1,1,1,1,1,1]
    null =[0,0,0,0,0,0,0,0]
    exponentResult = sumBinaryNumbers(exponent1,exponent2)
    exponentResult = sumBinaryNumbers(exponentResult,negone)
    exponentResult_for_cycle = exponentResult
    while exponentResult_for_cycle != null:
        count += 1
        exponentResult_for_cycle = sumBinaryNumbers(exponentResult_for_cycle, negone)
    if exponentResult[0] == 0:
        exponentResult = exponent1
        while count != 0:
            mantissa2.append(0)
            mantissa2.pop(0)
            count -= 1
    elif exponentResult[0] == 1:
        exponentResult = exponent2
        while count != 0:
            mantissa1.append(0)
            mantissa1.pop(0)
            count -= 1
    mantissaResult = sumBinaryNumbers(mantissa1,mantissa2)
    print(exponentResult)
    Res = [exponentResult,mantissaResult]
    return Res

print("Введите первое число :")
a = int(input())
print("Введите второе  число :")
b = int(input())

def menu():
    print("Выберите нужную операцию(латиница)")
    print("a) Сложение ,b) Умножение , c) Деление , d) Сложение чисел с плавающей запятой , e) Выход")
    menu = str(input())

    match menu:
        case "a":
            print("Выберите сочетание знаков(число):")
            print("1) +/+ , 2) -/+ , 3) +/- , 4) -/- 5) Выход")
            sub_menu = str(input())
            if sub_menu == "1":
                print("Результат сложения")
                FirsBinNum  = list(map(int,intToBin32(a)))
                SecondBinNum = list(map(int,intToBin32(b)))
            elif sub_menu == "2":
                print("Результат сложения")
                FirsBinNum  = list(map(int,intToBin32(-1 * a)))
                SecondBinNum = list(map(int,intToBin32(b)))
            elif sub_menu == "3":
                print("Результат сложения")
                FirsBinNum  = list(map(int,intToBin32(a)))
                SecondBinNum = list(map(int,intToBin32(-1 * b)))
            elif sub_menu == "4":
                print("Результат сложения")
                FirsBinNum  = list(map(int,intToBin32(-1 * a)))
                SecondBinNum = list(map(int,intToBin32(-1 * b)))
            elif sub_menu == "5":
                print("exit")
            print("Первое число :",FirsBinNum,"Второе число :",SecondBinNum)
            print(sumBinaryNumbers(FirsBinNum, SecondBinNum))
        case "b":
            print("Результат умножения")
            iterator = iterationCounter(b)+3
            FirstBin = list(map(int, intToBin(abs(a))))
            SecondBin = list(map(int, intToBin(abs(b))))
            bufferResult = multiplicationBinaryNumbers(FirstBin,SecondBin,iterator)
            result = reduce(sumBinaryNumbers,bufferResult)
            return result
        case "c":
            iterator = iterationCounter(b)
            FirstBin = list(map(int, intToBin(abs(a))))
            SecondBin = list(map(int, intToBin(abs(b))))
            SecondNegBin = list(map(int, intToBin(abs(b))))
            one = [0] * (len(SecondNegBin) - 1) + [1]
            
            print("SecondNegBinInput",SecondNegBin)
            print("one",one)
            for bits in range(len(SecondNegBin)):
                if SecondNegBin[bits] == 0:
                    SecondNegBin[bits] = 1
                elif SecondNegBin[bits] == 1:
                    SecondNegBin[bits] = 0
            print(SecondNegBin)
            SecondNegBin =sumBinaryNumbers(SecondNegBin,one)
            print("createNegBin",SecondNegBin)

            return divideBinaryNumbers(FirstBin,SecondBin,SecondNegBin,iterator)
        case "d":
            print("Введите первое вещественное  число :")
            c = float(input())
            print("Введите второе  вещественное  число :")
            d = float(input())
            c1 = intFloatPointtoBin(c)
            d1 = intFloatPointtoBin(d)
            print(intFloatPointtoBin(c))
            print(intFloatPointtoBin(d))
            res = sumFloatingPointBinaryNumbers(c1,d1)
            print(res)
            if res[1][0] != 1:
                while res[1][0] != 1:
                    res[1].append(0)
                    res[1].pop(0)

            print(res[0])
            result = [0] + res[0] + [0] + res[1]
            result = str(result)
            decimal_prog_res = float(c+d)
            print(decimal_prog_res)
            decimal_prog_res = intFloatPointtoBin(decimal_prog_res)
            decimal_prog_res = list(map(int,decimal_prog_res))
            print("Встроенная функция")
            print(decimal_prog_res)
            print("Результат программы")
            print(decimal_prog_res)
            print("Результат в представлении ЭВМ",decimal_prog_res)
# print(menu())  
print(intToBinSW(a))             
print(intFloatPointtoBinSW(4.5))          







                    # while abs(n) > 0:
    #     bin = str(n % 2) + bin
    #     n //= 2
    #     print(bin)
    #     
    # else:
    #     bin = 32 * [0]        
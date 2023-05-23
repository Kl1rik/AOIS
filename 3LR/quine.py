
def compare_string(string1, string2):

    l1 = list(string1)
    l2 = list(string2)
    count = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count += 1
            l1[i] = "_"
    if count > 1:
        return -1
    else:
        return "".join(l1)
 
 
def check(binary):

    pi = []
    while 1:
        check1 = ["$"] * len(binary)
        temp = []
        for i in range(len(binary)):
            for j in range(i + 1, len(binary)):
                k = compare_string(binary[i], binary[j])
                if k != -1:
                    check1[i] = "*"
                    check1[j] = "*"
                    temp.append(k)
        for i in range(len(binary)):
            if check1[i] == "$":
                pi.append(binary[i])
        if len(temp) == 0:
            return pi
        binary = list(set(temp))
 
 
def decimal_to_binary(no_of_variable, minterms):
  
    temp = []
    s = ""
    for m in minterms:
        for i in range(no_of_variable):
            s = str(m % 2) + s
            m //= 2
        temp.append(s)
        s = ""
    return temp
 
 
def is_for_table(string1, string2, count):
   
    l1 = list(string1)
    l2 = list(string2)
    count_n = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count_n += 1
    if count_n == count:
        return True
    else:
        return False
 
 
def selection(chart, prime_implicants):
    
    temp = []
    select = [0] * len(chart)
    for i in range(len(chart[0])):
        count = 0
        rem = -1
        for j in range(len(chart)):
            if chart[j][i] == 1:
                count += 1
                rem = j
        if count == 1:
            select[rem] = 1
    for i in range(len(select)):
        if select[i] == 1:
            for j in range(len(chart[0])):
                if chart[i][j] == 1:
                    for k in range(len(chart)):
                        chart[k][j] = 0
            temp.append(prime_implicants[i])
    while 1:
        max_n = 0
        rem = -1
        count_n = 0
        for i in range(len(chart)):
            count_n = chart[i].count(1)
            if count_n > max_n:
                max_n = count_n
                rem = i
 
        if max_n == 0:
            return temp
 
        temp.append(prime_implicants[rem])
 
        for i in range(len(chart[0])):
            if chart[rem][i] == 1:
                for j in range(len(chart)):
                    chart[j][i] = 0
 
 
def prime_implicant_chart(prime_implicants, binary):
   
    chart = [[0 for x in range(len(binary))] for x in range(len(prime_implicants))]
    for i in range(len(prime_implicants)):
        count = prime_implicants[i].count("_")
        for j in range(len(binary)):
            if is_for_table(prime_implicants[i], binary[j], count):
                chart[i][j] = 1
 
    return chart
 
 
def main(minterms,key):
    no_of_variable = 3
    
    binary = decimal_to_binary(no_of_variable, minterms)
 
    prime_implicants = check(binary)
    print("Полученные импликанты в численном виде:")
    print(prime_implicants)
    chart = prime_implicant_chart(prime_implicants, binary)
 
    essential_prime_implicants = selection(chart, prime_implicants)
    
    new_list = []
    for implicant in essential_prime_implicants:
        implicant = list(implicant)
        
        if implicant[0] == '1':
            implicant[0] = 'A'
        elif implicant[0] == '0':
            implicant[0] = '!A'
        elif implicant[0] == '_':
            implicant[0] = ''    
        if implicant[1] == '1':
            implicant[1] = 'B'
        elif implicant[1] == '0':
            implicant[1] = '!B'
        elif implicant[1] == '_':
            implicant[1] = ''   
        if implicant[2] == '1':
            implicant[2] = 'C'
        elif implicant[2] == '0':
            implicant[2] = '!C'
        elif implicant[2] == '_':
            implicant[2] = ''  
        convertList = ''.join(map(str,implicant))
        new_list.append(convertList)
        implicant = str(implicant)    
        
    if key == 0:    
        print("Полученная СКНФ")
        new_list= '*'.join(map(str,new_list))     
    elif key == 1:
        print("Полученная СДНФ")  
        new_list= '+'.join(map(str,new_list))    
    print(new_list)    
    


 
 
if __name__ == "__main__":
    main()

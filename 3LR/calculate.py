def convert_into_digit_form(any_sdnf):
    new_any_sdnf = any_sdnf
    new_any_sdnf_list=[]
    for iterator in range(len(any_sdnf)):
        if any_sdnf[iterator] in '*+':
            new_any_sdnf = new_any_sdnf.replace(any_sdnf[iterator], "")
    def rewrite_variables_to_nums(string):
        string = string.replace('!A', '4')
        string = string.replace('!B', '5')
        string = string.replace('!C', '6')
        string = string.replace('A', '1')
        string = string.replace('B', '2')
        string = string.replace('C', '3')
        return string
    new_any_sdnf = rewrite_variables_to_nums(new_any_sdnf)
    counter=0
    temp=''
    for iterator in range(len(new_any_sdnf)):
        counter+=1
        temp+=str(new_any_sdnf[iterator])
        if counter==3:
            counter=0
            new_any_sdnf_list.append(temp)
            temp=''

    return new_any_sdnf,new_any_sdnf_list

def rewrite_num_to_variables(string):
        string = string.replace('1', 'A')
        string = string.replace('2', 'B')
        string = string.replace('3', 'C')
        string = string.replace('4', '!A')
        string = string.replace('5', '!B')
        string = string.replace('6', '!C')
        return string
    

def reduced_dnf(any_sdnf):
    new_any_sdnf=[]
    counter = 0
    temp = ''
    for literal in any_sdnf:
        counter += 1
        if int(literal) <= 3:
            temp += '1'
        else:
            temp += '0'
        if counter == 3:
            counter = 0
            new_any_sdnf.append(temp)
            temp = ''
            
    any_sdnf = ''
    
    for iterator in range(len(new_any_sdnf)):
        
        for val in range(iterator + 1, len(new_any_sdnf)):
            if new_any_sdnf[iterator][0] == new_any_sdnf[val][0] and new_any_sdnf[iterator][1] == new_any_sdnf[val][1]:
                any_sdnf += (new_any_sdnf[iterator][0] + new_any_sdnf[iterator][1] + '_')
                
                
            elif new_any_sdnf[iterator][1] == new_any_sdnf[val][1] and new_any_sdnf[iterator][2] == new_any_sdnf[val][2]:
                any_sdnf += ('_' + (new_any_sdnf[iterator])[1] + (new_any_sdnf[iterator])[2])
                
                
            elif new_any_sdnf[iterator][0] == new_any_sdnf[val][0] and new_any_sdnf[iterator][2] == new_any_sdnf[val][2]:
                any_sdnf += (new_any_sdnf[iterator][0] + '_' + new_any_sdnf[iterator][2])
    rxnf = []
    for iterator in range(len(any_sdnf)):
        if any_sdnf[iterator] == '0':
            rxnf.append(str(iterator % 3 + 1 + 3))
        elif any_sdnf[iterator] == '1':
            rxnf.append(str(iterator % 3 + 1))

    return rxnf

def quine_method(any_sdnf_list, rxnf,key):
    
    any_sdnf=''
    implikant = []
    for i in range(0, len(rxnf)):
        implikant.append(rxnf[i])
    constituent = any_sdnf_list
    string_in_table = ''
    table = []
    for i in range(0, len(implikant), 2):
        for val in range(len(constituent)):
            if implikant[i] in constituent[val] and implikant[i + 1] in constituent[val]:
                string_in_table += '1'
            else:
                string_in_table += '0'
        table.append(string_in_table)
        string_in_table = ''

    sum = 0
    counter = 0
    tempo='' 
    for val in range(4):
        for i in (table):
            counter += 1
            sum += int(i[val])
            if i[val] == '1':
                column = counter
        counter = 0
        
            
        if sum == 1:
            if key == 1:
                tempo = (implikant[column * 2 - 2] + '*' + implikant[column * 2 - 1] + '+')
            elif key == 0:
                tempo = ('('+implikant[column * 2 - 2] + '+' + implikant[column * 2 - 1] + ')' '*')
            else:
                print("error",key)    
            any_sdnf += tempo
        sum = 0
        
        
        
        
        
    new_any_sdnf=any_sdnf

    
    new_any_sdnf = rewrite_num_to_variables(new_any_sdnf)
    
    
    
    return new_any_sdnf[:len(new_any_sdnf)-1:]
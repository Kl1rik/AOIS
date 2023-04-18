import math as mt
list_pdnf = []
list_pknf = [] 
x1 = "x1"
x2 = "x2"
x3 = "x3"
inverse = "!"

def logicalExpressionEvaluation(string):
 
    arr = list()
    n = len(string)
    for i in range(n - 1, -1, -1):
        if (string[i] == "("):
 
            s = list()
            

            while (arr[-1] != ")"):
                s.append(arr[-1])
                arr.pop()
 
            arr.pop()
 
            # for NOT operation
            if (len(s) == 3):
                if s[2] == "1":
                    arr.append("0")
                else:
                    arr.append("1")
                
            # for or or OR operation
            elif (len(s) == 5):
                a = int(s[0]) - 48
                b = int(s[4]) - 48
                c = 0
                if s[2] == "&":
                    c = a & b
                elif s[2] == "|":
                    c = a | b
                elif s[2] == "*":
                    c = a * b    
                arr.append((c) + 48)
                
        else:
            arr.append(string[i])
         
    return arr[-1]

def num_form(list_pdnf,list_pknf):
    print("Index PDNF",list_pdnf)
    print("Index PKNF",list_pknf)

def build_pdnf(list_pdnf):
    print(list_pdnf)
    pdnf_print = "PDNF form : "
    for index in list_pdnf:
        if index == 0:
            pdnf_print = pdnf_print +  inverse +  x1 + "∧"+ inverse + x2 + "∧"+ inverse + x3 + " ∨ "
        elif index == 1:
            pdnf_print = pdnf_print +  inverse +  x1 + "∧"+ inverse + "∧" + x2 + "∧"+  x3 + " ∨ "
        elif index == 2:
            pdnf_print = pdnf_print +  inverse +  x1 + "∧"+  x2 + inverse + x3 + " ∨ "
        elif index == 3:
            pdnf_print = pdnf_print +  inverse + x1 + "∧"+  x2 +  x3 + " ∨ "
        elif index == 4:
            pdnf_print = pdnf_print +   x1 + "∧"+ inverse + x2 + "∧" + inverse + x3 + " ∨ "
        elif index == 5:
            pdnf_print = pdnf_print +  x1 + "∧"+ inverse + x2 + "∧" +  x3 + " ∨ "
        elif index == 6:
            pdnf_print = pdnf_print +   x1 + "∧"+ x2 + "∧" + inverse + x3 + " ∨ "
        elif index == 7:
            pdnf_print = pdnf_print +  x1 + "∧"+  x2 + "∧"+  x3  
    print(pdnf_print)

def build_pknf(list_pknf):
    print(list_pknf)
    pknf_print = "PKNF form : "
    for index in list_pknf:
        if index == 0:
            pknf_print = pknf_print + inverse + x1 + "∨"+ inverse + x2 + "∨"+ inverse + x3 + " ∧ "
        elif index == 1:
            pknf_print = pknf_print + inverse + x1 + "∨"+ inverse + x2 + "∨"+  x3 + " ∧ "
        elif index == 2:
            pknf_print = pknf_print + inverse + x1 + "∨"+  x2 + inverse + "∨"+ x3 + " ∧ "
        elif index == 3:
            pknf_print = pknf_print + inverse + x1 + "∨"+  x2 + "∨"+  x3 + " ∧ "
        elif index == 4:
            pknf_print = pknf_print +  x1 + inverse + x2 + inverse + x3 + " ∧ "
        elif index == 5:
            pknf_print = pknf_print  + x1 + inverse + x2 +  x3 + " ∧ "
        elif index == 6:
            pknf_print = pknf_print +  x1 + x2 + inverse + x3 + " ∧ "
        elif index == 7:
            pknf_print = pknf_print + x1 +  x2 +  x3 
    print(pknf_print)

string_list = ["((0,&,0),|,(!,0))","((0,&,0),|,(!,1))","((0,&,1),|,(!,0))","((0,&,1),|,(!,1))","((1,&,0),|,(!,0))","((1,&,0),|,(!,1))","((1,&,1),|,(!,0))","((1,&,1),|,(!,1))"]
input_string = "((0&0)|(!0))"
# test_str = input_string.split("|")
# test_str.insert(1,"|")
# test_str.insert()
# test_str = ",".join(test_str)
test_list = list(input_string)
for index in range(len(test_list)):
    if test_list[index] == "0" or "1" or "&" or "|" or "!" and test_list[index + 1] == ")"  :
        test_list.insert(index+1,",")
print(test_list)
for string in range(len(string_list)):
    result = logicalExpressionEvaluation(string_list[string])
    if result == 1:
        list_pdnf.append(string)
    elif result == 0:
        list_pknf.append(string)    
    if string > 3:
        print(bin(string).replace("0b","") ,result)
    elif string == 0:
        print("000" ,result)
    elif string == 1:
        print("001" ,result)
    elif string == 2:
        print("010" ,result)
    elif string == 3:
        print("011" ,result)
num_form(list_pdnf,list_pknf)    
build_pdnf(list_pdnf)
build_pknf(list_pknf)


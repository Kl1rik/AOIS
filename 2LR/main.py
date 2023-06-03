'''121702 Шершень'''
import itertools
from itertools import product

s = '(A|B)&C'

result =[] 
variables = list(sorted(set([c for c in s if c.isalpha()])))
print(*variables, s, sep=' ')
k = ""
k1 = "" 
sknf = []
sdnf = []
 
n = ['!', '']
n_sknf = ['', '!']
d = {0: [], 1: []}
d_lf ={0:["000"] , 1:["001"] , 2:["010"] , 3:["011"] , 4:["100"] ,5:["101"],6:["110"],7:["1 1 1"]}

def rewrite_variables_to_index_form_sdnf(string):
        string = string.replace('!A', '0')
        string = string.replace('!B', '0')
        string = string.replace('!C', '0')
        string = string.replace('A', '1')
        string = string.replace('B', '1')
        string = string.replace('C', '1')
        return string

def rewrite_variables_to_index_form_sknf(string):
        string = string.replace('!A', '1')
        string = string.replace('!B', '1')
        string = string.replace('!C', '1')
        string = string.replace('A', '0')
        string = string.replace('B', '0')
        string = string.replace('C', '0')
        return string    
    
for num, combination in enumerate(itertools.product([0, 1], repeat=len(variables))):
    values = list(combination)
    variables_dict = dict(zip(variables, values))
    
    s = s.replace('!', ' not ').replace('&', ' and ').replace('|', ' or ')
    expression_result = eval(s, variables_dict)
    d[expression_result].append(num)
    if expression_result == 0:
        sknf.append(f"({n_sknf[values[0]]}A+{n_sknf[values[1]]}B+{n_sknf[values[2]]}C)")
    if expression_result == 1:
        sdnf.append(f"({n[values[0]]}A*{n[values[1]]}B*{n[values[2]]}C)")
    print(values, expression_result)
 

sknf = '*'.join(sknf)
sdnf = '+'.join(sdnf)
print(d)
print("Полученная СКНФ")
print(sknf)
print("Полученная СДНФ")
print(sdnf)
sknf = rewrite_variables_to_index_form_sknf(sknf)
sdnf = rewrite_variables_to_index_form_sdnf(sdnf)
print("Полученная индексная форма СКНФ")
print(sknf)
print("Полученная индексная форма СДНФ")
print(sdnf)
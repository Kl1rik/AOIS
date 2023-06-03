'''121702 Шершень'''
import itertools
from itertools import product
from calculate import quine_method,reduced_dnf
from calculate import convert_into_digit_form as convert
from quine import main as calculate_tabular
from kmap import k_map 
# s = '(!A∨B)∧C'
# s = '(A∨!B)∧(!C)'
s = '(A∨B)∧C'
'''Код из 2ЛР,необходим для получения СКНФ СДНФ'''
result =[] 



s = s.replace("∧","&")
s = s.replace("∨","|")
variables = list(sorted(set([c for c in s if c.isalpha()])))
print(*variables, s, sep=' ')

sknf = []
sdnf = []
k = ""
k1 = "" 
n_sdnf = ['!', '']
n_sknf = ['', '!']
d = {0: [], 1: []}
d_lf ={0:["0 0 0"] , 1:["0 0 1"] , 2:["0 1 0"] , 3:["0 1 1"] , 4:["1 0 0"] ,5:["1 0 1"],6:["1 1 0"],7:["1 1 1"]}


    
    
for num, combination in enumerate(itertools.product([0, 1], repeat=len(variables))):
    values = list(combination)
    variables_dict = dict(zip(variables, values))
    s = s.replace('!', ' not ').replace('&', ' and ').replace('|', ' or ')
    expression_result = eval(s, variables_dict)
    d[expression_result].append(num)
    if expression_result == 0:
        sknf.append(f"{n_sknf[values[0]]}A+{n_sknf[values[1]]}B+{n_sknf[values[2]]}C")
    if expression_result == 1:
        sdnf.append(f"{n_sdnf[values[0]]}A*{n_sdnf[values[1]]}B*{n_sdnf[values[2]]}C")
    # print(values, expression_result)
 
print("Получаем СДНФ и СКНФ с помощью ЛР2")   
sknf = '*'.join(sknf)
sdnf = '+'.join(sdnf)
print(d)
print("Полученная СКНФ")
print(sknf)
print("Полученная СДНФ")
print(sdnf)
'''Конец кода'''
    


print("ЛР3")
key_sdnf = 1
key_sknf = 0

print("Метод с помощью карты Карно(Расчетный метод)")
def kmap_method(k,k1):
    mima = 1
    nfinp = 3
 

    if mima==1:
        mt1= d.get(1)
        mt0 = d.get(0)
    
    if nfinp==3:
        print("МКНФ")
        k =  k_map(mt0,mima,1)
        print("МДНФ")
        k1 = k_map(mt1,mima,0)
    print()    
    return k,k1
    
k,k1 = kmap_method(k,k1)    

print("Метод с помощью Квайна Макласски")
print("МДНФ")
calculate_tabular(minterms= d.get(1),key=1,)
print("МКНФ")
calculate_tabular(minterms = d.get(0),key=0)

print("Методом склеивания")

sdnf_edit,sdnf_list = convert(sdnf)
rdnf = reduced_dnf(sdnf_edit)

sknf_edit,sknf_list = convert(sknf)

rknf = reduced_dnf(sknf_edit)



result = quine_method(sdnf_list,rdnf,key_sdnf)
print("МДНФ")
result = k
print(result)
print("МКНФ")
result = quine_method(sknf_list,rknf,key_sknf)
result = k1
print(result)
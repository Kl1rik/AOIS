'''Шершень 121702'''
from AOIS1lab import sumBinaryNumbers,intToBin32,intToBin
from quine import main as calculate_tabular
negone = intToBin32(-1)
bin_254 = intToBin32(254)
bin_14 = intToBin32(14)
null_eight_digit = [0,0,0,0,0,0,0,0]
null_four_digit = [0,0,0,0]
null_two_digit = [0,0]
bin_6 = intToBin(6)
negtwo = intToBin32(-2)
bin_75 = intToBin(75)

def group_list(any_list, length):
    return [any_list[i:i + length] for i in range(0, len(any_list), length)]

def list_to_string(list):
    string = ''
    for bit in list:
        string += bit
    return string

def build_inp_truth_table(key :int):
    row_1 = 16*[1]+16*[0]
    row_2 = (8*[1]+8*[0])*2
    row_3 = (4*[1]+4*[0])*4
    row_4 = (2*[1]+2*[0])*8
    row_5 = ([1]+[0])*16

    truth_table_inp = [row_1,row_2,row_3,row_4,row_5]
    truth_table_inp_reversed = []
   
    for signals_list in truth_table_inp:  
        
        el_index = truth_table_inp.index(signals_list)  
        if key == 0:
            if el_index == 4:
                print("-"*67)   
                print("V  ",*list(reversed(signals_list)),sep = ' ')    

            else:
                print(f"q{el_index+1} ",*list(reversed(signals_list)),sep = ' ')
             
        elif key == 1:
            signals_list = list(reversed(signals_list))
            truth_table_inp_reversed.append(signals_list)
        
    return truth_table_inp_reversed   
       

def build_post_truth_table(key : int):
    truth_table_inp = build_inp_truth_table(1)
    temp_row = []
    merged_list = []
    truth_table_post = []
    digit_four_convert = bin_75 

    for signals_list in truth_table_inp:

        neg_one = list(map(int,negone))
       
        el_index = truth_table_inp.index(signals_list)  

        if el_index == 0 :
            signals_list = signals_list[16:]
            neg_one = neg_one[16:]

            row = sumBinaryNumbers(signals_list,neg_one)
            row = sumBinaryNumbers(row,neg_one)
            row = null_eight_digit*2 + list(reversed(row))
            row[1] = row[31]

        elif el_index == 1:

            slice_eight_digit = signals_list[24:]
            slice_neg_one_eight_digit = neg_one[:8]

            sub_row_0 = sumBinaryNumbers(slice_eight_digit,slice_neg_one_eight_digit)
            sub_row_0 = sumBinaryNumbers(sub_row_0,slice_neg_one_eight_digit)
            
            row = null_eight_digit  + list(reversed(sub_row_0)) +[0] + [1]+ null_two_digit * 3 + sub_row_0
            row[1] = row[31]

        elif el_index == 2:

            slice_four_digit = signals_list[28:]
            slice_neg_one_four_digit = neg_one[:4]

            sub_row_four = sumBinaryNumbers(slice_four_digit,slice_neg_one_four_digit)
            sub_row_four = sumBinaryNumbers(sub_row_four,slice_neg_one_four_digit)
            row = digit_four_convert * 4

        elif el_index == 3:
            row = bin_6 * 8

        truth_table_post.append(row)

    del_unused_row =truth_table_post.pop(4) 

    if key == 0:
        for signals in truth_table_post:
            sig_index = truth_table_post.index(signals)
            print(f"q{sig_index+1}*",*signals,sep = ' ')

    if key == 1:
        return truth_table_post  

def compare_list(list1,list2):
    temp_list = []
    for bit in range(len(list1)):
        if list1[bit] == list2[bit]:
            temp_list.append(0)
        elif list1[bit] != list2[bit]:
            temp_list.append(1)    
           
    return temp_list

def build_activity_truth_table(key:int):
    inp_table = build_inp_truth_table(1)
    post_table = build_post_truth_table(1)
    
    h1 = compare_list(inp_table[0],post_table[0])
    h2 = compare_list(inp_table[1],post_table[1])
    h3 = compare_list(inp_table[2],post_table[2])
    h4 = compare_list(inp_table[3],post_table[3])
    activity_table = [h1,h2,h3,h4]
    if key == 0:
        for row in activity_table:
            sig_index = activity_table.index(row)
            print(f"h{sig_index+1} ",*row,sep = ' ')
    elif key == 1:
        return activity_table  
          
def binary_to_decimal(binary_number):
    decimal_number = 0
    power = len(binary_number) - 1

    for digit in binary_number:
        if digit == '1':
            decimal_number += 2 ** power
        power -= 1

    return decimal_number

def minimize_table():
    inp_table = build_inp_truth_table(1)
    active_table = build_activity_truth_table(1)

    for signal in range(len(inp_table)):
        inp_table[signal] = list(map(str,inp_table[signal]))

    h1_index = []
    h2_index = []
    h3_index = []
    h4_index = []
    for signal in range(len(active_table)):
        for bit in range(len(active_table[signal])):
            if active_table[0][bit] == 1:
                temp = inp_table[0][bit]+inp_table[1][bit]+inp_table[2][bit]+inp_table[3][bit]+inp_table[4][bit]
                h1_index.append(temp)
            elif active_table[1][bit] == 1:
                temp = inp_table[0][bit]+inp_table[1][bit]+inp_table[2][bit]+inp_table[3][bit]+inp_table[4][bit]
                h2_index.append(temp)
            elif active_table[2][bit] == 1:
                temp = inp_table[0][bit]+inp_table[1][bit]+inp_table[2][bit]+inp_table[3][bit]+inp_table[4][bit]
                h3_index.append(temp)
            elif active_table[3][bit] == 1:
                temp = inp_table[0][bit]+inp_table[1][bit]+inp_table[2][bit]+inp_table[3][bit]+inp_table[4][bit]
                h4_index.append(temp)

    h1_index_new = h1_index[:2]       
    h2_index_new = h1_index[:2] + h2_index[:2]
    h3_index_new = h1_index[:2] + h2_index[:1] + h3_index[:5]
    h4_index_new = h1_index[:2] + h2_index[:1] + h3_index[:5] + h4_index[:8]     
    
    h1_index_new = list(map(binary_to_decimal,h1_index_new))
    h2_index_new = list(map(binary_to_decimal,h2_index_new))
    h3_index_new = list(map(binary_to_decimal,h3_index_new))
    h4_index_new = list(map(binary_to_decimal,h4_index_new))

    print("H1*")
    calculate_tabular(h1_index_new,1,1)
    print("H2*")
    calculate_tabular(h2_index_new,1,2)
    print("H3*")
    calculate_tabular(h3_index_new,1,3)
    print("H4*")
    calculate_tabular(h4_index_new,1,4)

print("Построим таблицу переходов")
print("-"*67)
build_inp_truth_table(0)  
print("-"*67)
build_post_truth_table(0)    
print("-"*67)   
build_activity_truth_table(0)
print("-"*67) 
print("Получим минизированные функции")
minimize_table()
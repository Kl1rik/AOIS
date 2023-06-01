
data = ["".join([str(__import__("random").randint(0, 1)) for _ in range(3)]) for _ in range(10)]

def find(s):
    max_match = 0
    match_indices = []
    
    for i, item in enumerate(data):
        match_count = 0
        
        for j in range(len(s)):
            if s[j] == item[j]:
                match_count += 1
            
        if match_count > max_match:
            max_match = match_count
            match_indices = [i]
        elif match_count == max_match:
            match_indices.append(i) 
    return [data[i] for i in match_indices]

def find_down(s):
    res = ''  
    for elem in sorted(data):
        if elem < s:
            res = elem
    return res

def find_up(s):
    res = ''
    print(data)
    for elem in sorted(data, reverse=True):
        if elem > s:
            res = elem
    return res
       
def find_flags(word_1, word_2):
    cur_g, cur_l = 0, 0
    for ind, word in enumerate(data):
        digit_1, digit_2 = list(map(lambda x: bool(int(x)), [word_1[ind], word_2[ind]] ))
        next_g = cur_g or (not digit_2 and digit_1 and not cur_l)
        next_l = cur_l or (digit_2 and not digit_1 and not cur_g)
        cur_g, cur_l = next_g, next_l
    return bool(cur_g), bool(cur_l)


def compare(word_1, word_2):
    match find_flags(word_1, word_2):
        case (True, False): return 1
        case (False, True): return -1
        case (False, False): return 0
    raise KeyError()

def get_max():
    return max(data)


print(f'Поиск по соответствию: {find("111")}')  
print(f'Поиск по соответствию: {find("101")}')  
print(f'Поиск по соответствию: {find("0x0")}')  
print(f'Поиск по соответствию: {find("x10")}')  
print("Число для Поиск ближайшего сверху (снизу)значения 101")
print("Наибольшее ближайшее число",find_up('101'))
print("Наименьшее ближайшее  число",find_down('101'))


                
        
    
'''121702 Шершень'''
# Хэш функция
def hash_function(key, size):
    hash_value = 0
    
    for element in key:
        
        hash_value += ord(element)
        
    return hash_value % size
# Добавление пары ключ значение в таблицу
def insert(table, key, value):
    
    index = hash_function(key, len(table))
    for pair in table[index]:
        
        if pair[0] == key:
            pair[1] = value
            return
        
    table[index].append([key, value])
# Получение значения по ключу
def get(table, key):
    index = hash_function(key, len(table))
    
    for pair in table[index]:
        
        if pair[0] == key:
            return pair[1]
        
    raise KeyError(key)
# Удалени пары ключ значение из таблицы
def remove(table, key):
    index = hash_function(key, len(table))
    
    for i, pair in enumerate(table[index]):
        
        if pair[0] == key:
            del table[index][i]
            return
        
    raise KeyError(key)

def beautiful_print(table):
    for element in table:
        print(element)


size = 10
hash_table = [[] for _ in range(size)]

insert(hash_table, "graph", "ostis")
insert(hash_table, "banana", "fruit")
insert(hash_table, "python", "program")
insert(hash_table, "int", "number")
insert(hash_table, "list", "element")
insert(hash_table, "c", "program")

print(beautiful_print(hash_table))

print(get(hash_table, "graph"))  # Вывод: ostis
print(get(hash_table, "banana"))  # Вывод: fruit
print(get(hash_table, "python"))  # Вывод: program

insert(hash_table, "bose", "headphone")
print(get(hash_table, "bose"))  # Вывод: headphone

remove(hash_table, "banana")

print(beautiful_print(hash_table))

print(get(hash_table, "banana"))  # Вызовет KeyError: 'banana'
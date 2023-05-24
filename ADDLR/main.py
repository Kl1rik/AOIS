'''121702 Шершень Вариант 15'''
from skiplist import SkipList

value_list = SkipList(4, 0.5)

value_list.insert(2)
value_list.insert(8)
value_list.insert(16)
value_list.insert(21)
value_list.insert(34)
value_list.insert(18)
value_list.insert(15)
value_list.insert(1)
value_list.insert(19)
value_list.insert(41)

value_list.displayList()

value_list.searchElement(19)
value_list.deleteElement(8)

value_list.displayList()           
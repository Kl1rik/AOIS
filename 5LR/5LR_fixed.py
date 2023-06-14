def build_truth_table():
    row_1 = 16*[1]+16*[0]
    row_2 = (8*[1]+8*[0])*2
    row_3 = (4*[1]+4*[0])*4
    row_4 = (2*[1]+2*[0])*8
    row_5 = ([1]+[0])*16
    row_6 = 16*[1]+15*[0] + [1]
    
    truth_table = [row_1,row_2,row_3,row_4,row_5,row_6]
    
   
    for element in truth_table:    
        print(element)
        
build_truth_table()    
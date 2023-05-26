
qrd_var_2_2=["B' ","C ","B ","C' "]
qrd_var_1_4=["A' ","A "]
dul_vert=["B'C' ","B'C ","BC ","BC' "]
dul_horz=[["A'B' ","A'C ","A'B ","A'C' "],["AB' ","AC ","AB ","AC'"]]
sngl_val=[["A'B'C' ","A'B'C ","A'BC ","A'BC' "],["AB'C' ","AB'C ","ABC ","ABC' "]]
def rewrite_value(string):    
   
    string=string.replace("A'","!A")
    string=string.replace("B'","!B")
    string=string.replace("C'","!C")
    return string

def k_map(mt,nip,key):
    
    print()
    var_re=["A","B","C"]
    literal = ''
    karno_value=[[0,0,0,0],[0,0,0,0]]
    karno_valuemx=[[0,0,0,0],[0,0,0,0]]
    result=''
    flag=0
    qrd=[]
    dul=[]
    sngl=[]
   
        
    for i in range(2):
        for j in range(4):
            p=int('0b'+bin(i)[2:]+bin(j)[2:],2)
            if (i==1) and (j==0 or j==1):
                p=int('0b'+bin(i)[2:]+'0'+bin(j)[2:],2)
            if p in mt:
                karno_value[i][j]=1


    for i in range(2):
        (karno_value[i][2],karno_value[i][3])=(karno_value[i][3],karno_value[i][2])
   
    
    print("Полученная карта: ")
    if nip==1:
        for each in karno_value:print(*each)
    elif nip==2:
        for i in range(2):
            for j in range(4):
                if karno_value[i][j]==1:
                    karno_valuemx[i][j]=0
                else:
                    karno_valuemx[i][j]=1
        for each in karno_valuemx:print(*each)

    if karno_value==[[1]*4,[1]*4]:
        result=result+'1'
        flag=1
    if flag==0:
        for j in range(-1,3):
            if karno_value[0][j]==1 and karno_value[-1][j]==1 and karno_value[0][j+1]==1 and karno_value[-1][j+1]==1:
                qrd.append([(0,j),(-1,j)])
                if j<2:
                    qrd.append([(0,j+1),(-1,j+1)])
                    qrd.append([(0,j),(0,j+1)])
                    qrd.append([(-1,j),(-1,j+1)])
                else:
                    qrd.append([(0,-1),(-1,-1)])
                    qrd.append([(0,j),(0,-1)])
                    qrd.append([(-1,j),(-1,-1)])
                result=result+qrd_var_2_2[j]
    if flag==0:
        for i in range(-1,1):
            if karno_value[i]==[1,1,1,1]:
                qrd.append([(i,-1),(i,0)])
                qrd.append([(i,0),(i,1)])
                qrd.append([(i,1),(i,2)])
                qrd.append([(i,2),(i,-1)])
                result=result+qrd_var_1_4[i]
    if flag==0:
        for j in range(-1,3):
            if karno_value[0][j]==1 and karno_value[1][j]==1:
                temp=0
                if [(0,j),(-1,j)] in qrd:
                    temp=1
                elif [(-1,j),(0,j)] in qrd:
                    temp=1
                if temp==0:
                    dul.append([(0,j),(-1,j)])
                    result=result+dul_vert[j]
                
    if flag==0:
        for i in range(-1,1):
            for j in range(-1,3):
                if karno_value[i][j]==1 and karno_value[i][j+1]==1:
                    temp=0
                    if j==2:
                        if [(i,j),(i,-1)] in qrd:
                            temp=1
                        elif [(i,-1),(i,j)] in qrd:
                            temp=1
                    else:
                        if [(i,j),(i,j+1)] in qrd:
                            temp=1
                        elif [(i,j+1),(i,j)] in qrd:
                            temp=1
                    if temp==0:
                        if j==2:
                            dul.append([(i,2),(i,-1)])
                        else:
                            dul.append([(i,j),(i,j+1)])
                        result=result+dul_horz[i][j]

    result=result.rstrip(" ")
    resultl=result.split(" ")
    for i in range(len(resultl)):
        resultl[i]=resultl[i]+" "
    
    for each in dul:
        d1cnt=0
        d2cnt=0
        (d1,d2)=(each[0],each[1])
        for each1 in dul:
            if d1 in each1:
                d1cnt+=1
            if d2 in each1:
                d2cnt+=1
        if d1cnt>1 and d2cnt>1:
            (d1i,d1j)=d1
            (d2i,d2j)=d2
            if d1i==d2i:
                p=dul_horz[d1i][d1j]
                resultl.remove(p)
            else:
                p=dul_vert[d1j]
                resultl.remove(p)
            dul.remove([d1,d2])
    result="".join(resultl)

    for _ in qrd:
        for each in _:
            sngl.append(each)
    for _ in dul:
        for each in _:
            sngl.append(each)

    if flag==0:
        for i in range(-1,1):
            for j in range(-1,3):
                if karno_value[i][j]==1:
                    if (i,j) not in sngl:
                        result=result+sngl_val[i][j]

    result=result.rstrip(" ")
    if nip==1 and key == 1:
        result=result.replace(' ','+')
    elif nip == 1 and key == 0:
        result=result.replace(' ','*')
    result=result.replace("A",var_re[0])
    result=result.replace("B",var_re[1])
    result=result.replace("C",var_re[2])
    result = rewrite_value(result)
    print("Полученное решение :",result)
    
    print()
    return result
   


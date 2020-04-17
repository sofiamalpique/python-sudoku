def sudoku(G):
    lst=[]
    #verificar as linhas
    for i in range(len(G)):
        for j in range(len(G[i])):
            s=(G[i][j])
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
           

                
    #verificar as colunas
    for i in range(len(G)):
        for j in range(len(G[i])):
            s=(G[j][i])
            lst.append(s)
            sorted(lst)    
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
                

    #verificar grelhas 3x3
    for i in range(3):
        for j in range(3):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
        for j in range(3,6):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
        for j in range(6,9):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]


    for i in range(3,6):
        for j in range(3):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
        for j in range(3,6):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
        for j in range(6,9):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]

    for i in range(6,9):
        for j in range(3):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
        for j in range(3,6):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
        for j in range(6,9):
            s=G[i][j]
            lst.append(s)
            sorted(lst)
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]:
                return False
        lst=[]
    return True

import numpy as np

# Standard matrix used for AES MixColumn operation
MIX_COL = np.array([[2, 3, 1, 1],
                    [1, 2, 3, 1],
                    [1, 1, 2, 3],
                    [3, 1, 1, 2]])

#print(MIX_COL[:,0:1])

# function to perform row shift operation
# parameter parameter is state matrix
def row_shift(mat):
    list1 = []
    for i in range(4):
        list2 = [] 
        for j in range(4):
            if i==0:
                list2.append(mat[i][j])
            elif i==1:
                list2.append(mat[i][(j+3)%4])
            elif i==2:
                list2.append(mat[i][(j+2)%4])
            else:
                list2.append(mat[i][(j+1)%4])
        list1.append(list2)
    return list1

# galois multiplication operation (GF2)
def galois_col(mat):
    col_ = []
    for i in range(4):
        S = MIX_COL[i:i+1,:]
        list1 = []
        for j in range(4):
            list1 = reduce_list(list1 , multPoly(S[0,j], mat[j,0]))
        num = 0
        for i in range(len(list1)):
            num = num ^ (1<<list1[i])
        while(len(bin(num))>10):
            num = num ^ int('0b100011011',2)
        col_.append(hex(int(bin(num), 2)))
        #print(hex(int(bin(num), 2)))
        #print(bin(num))
    #print(col_)
    
    return col_

# function to perform MixColumn operation
def col_mix(mat):
    mat = np.array(mat)
    col_mix_list = []
    col_ = []
    for i in range(4):
        col_ = galois_col(mat[:,i:i+1])
        # adding the result from galois multiplication column wise
        # if list is empty, concatenate the result 
        # else if list is not empty add the result column wise, not row wise
        if len(col_mix_list)==0:
            col_mix_list = col_mix_list + col_
        else:
            col_mix_list = np.column_stack((col_mix_list, col_)) 
    # print (col_mix_list)
    return col_mix_list

# removes the elements which occur in both lists
# same element pair during galois multiplication cancel each other
def reduce_list(list1, list2):
    return list(set(list(set(list1).union(set(list2))))  - set(list(set(list1).intersection(set(list2)))))   

# function to perform polynomial multiplication
# eg. x^7 + x^6 + x^3 + x^1 + 1 = [7, 6, 3, 1, 0]
def multPoly(p, q):
    list1 = []
    list2 = []
    if p==1:
        list1.append(0)
    elif p==2:
        list1.append(1)
    else:
        list1.append(0)
        list1.append(1)
    # eg : convert string like 'A1' to binary string 
    # '0b11010111'[2:0] = 11010111
    q_bin = bin(int(q, 16))[2:]
    size = len(q_bin)
    for i in range(size):
        if q_bin[i]=='1':
            list2.append(size-i-1)
    # Multiplication of two polynomials
    # check if the elements obtained after multiplication is already in the 'res' list then they cancel each other...
    res = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if res.count(list1[i]+list2[j])==0:
                res.append(list1[i]+list2[j])
            else:
                res.remove(list1[i]+list2[j])
    return res
            
           

state_matrix = [['61','65','69','6d'], 
                ['62','66','6a','6e'], 
                ['63','67','6b','6f'], 
                ['64','68','6c','70']]
#print(state_matrix)
rs_mat = row_shift(state_matrix)
cm_mat = col_mix(rs_mat)
print (cm_mat)







    

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 00:30:27 2018

@author: anubhav singh
"""
'''
import numpy as np
np.set_printoptions(formatter={'int':hex})
mat1 = np.array([[1,2,3,4,5],
                 [4,5,6,7,8],
                 [23,56,43,4,34]])
mat2 = np.array([[2], [23], [32], [12], [1]])

res = np.matmul(mat1, mat2)
print (res)
np.set_printoptions(formatter={'int':bin})
print (res)
print (hex(3))

np.set_printoptions(formatter={'int':hex})
mat = [[2, 3, 1, 1],
       [1, 2, 3, 1],
       [1, 1, 2, 3],
       [3, 1, 1, 2]]
#test = []

'''



import numpy as np
MIX_COL = np.array([[2, 3, 1, 1],
                    [1, 2, 3, 1],
                    [1, 1, 2, 3],
                    [3, 1, 1, 2]])

#print(MIX_COL[:,0:1])
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
        #list2.clear()
    return list1
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

def col_mix(mat):
    mat = np.array(mat)
    col_mix_list = []
    col_ = []
    for i in range(4):
        col_ = galois_col(mat[:,i:i+1])
        if len(col_mix_list)==0:
            col_mix_list = col_mix_list + col_
        else:
            col_mix_list = np.column_stack((col_mix_list, col_))
    # print (col_mix_list)
    return col_mix_list

# removes the elements which occur in both lists
def reduce_list(list1, list2):
    return list(set(list(set(list1).union(set(list2))))  - set(list(set(list1).intersection(set(list2)))))   
 
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
    q_bin = bin(int(q, 16))[2:]
    size = len(q_bin)
    for i in range(size):
        if q_bin[i]=='1':
            list2.append(size-i-1)
    # Multiplication
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



    
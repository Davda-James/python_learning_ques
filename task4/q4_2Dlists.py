# a. making matrix and finding element in it
# importing numpy module for making arrays
import numpy as np
rows=int(input("enter rows of array:"))
columns=int(input("enter columns of array:"))
#make an array 
array=[]
for j in range(rows):
    list1=[]
    for i in range(columns):
        x=int(input(f"enter {j+1,i+1} element:"))
        list1.append(x)
    array.append(list1)
arr=np.array(array)
#printing an array
for i in range(rows):
    for j in range(columns):
        print(arr[i][j],end="  ")
    print()

# taking input k from user and checking whether the element exist in array or not
k=int(input("enter k:"))
c=False
for i in range(rows):
    for j in range(columns):
        if arr[i][j]==k:
            print(f"index of k is:{i,j}")
            c=True
if c==False:
    print("sorry element not found in matrix")

#b. checking whether the square matrix is symmetric and skew-symmetric
#i. defining a function to check whether the matrix is symmetric or not
def symmetric(rows1,columns1,matrix):
    for i in range(0,rows1):
        for j in range(0,columns1):
            if i!=j:
                if matrix[i][j]==matrix[j][i]:
                    bool=True
                else:
                    bool=False
            else:
                continue
            if bool==False:
                break
        if bool==False:
            break
    # printing matrix is symmetric or not
    if bool==False: 
        print("matrix is not symmetric")
    else:
        print("matrix is symmetric")

#ii. defining a function to check whether the matrix is skew symmetir
condition=True
def skew_symmetric(rows1,columns1,matrix):
    for i in range(rows1):
        if matrix[i][i]==0:
            for k in range(rows1):
                for j in range(columns1):
                    if matrix[i][j]==-matrix[j][i]:
                        condition=True
                    else:
                        condition=False
                        break
        else:
            break
        if condition==False:
            break
     # printing whether the matrix is skew-symmetric or not   
    if condition==False:
        print("matrix is not skew-symmetric")
    else:
        print(("matrix is skew-symmetric"))


#please enter equal rows1 and columns1 
rows1=int(input("enter rows of array:"))
columns1=int(input("enter columns of array:"))
while rows1!=columns1:
    print("enter rows and column again as it is not square matrix")
    rows1=int(input("enter rows of array:"))
    columns1=int(input("enter columns of array:"))
matrix=[]
for j in range(rows1):
    list2=[]
    for i in range(columns1):
        y=int(input(f"enter {j,i} element:"))
        list2.append(y)
    matrix.append(list2)
ARRAY=np.array(matrix)
#printing an array
for i in range(rows1):
    for j in range(columns1):
        print(ARRAY[i][j],end="  ")
    print()
symmetric(rows1,columns1,matrix)
skew_symmetric(rows1,columns1,matrix)




        


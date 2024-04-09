#importing required modules
import sys
import os
import numpy as np
f1=sys.argv[1]
f2=sys.argv[2]
fname=1
#declaring array
arr1=[]
arr2=[]
#processing the input files
while fname<=2:
    with open(sys.argv[fname]) as f:
        l=f.readlines()
        l.remove(l[0])
    if fname==1:    
        for i in l:
            i=i.replace('\n','')
            if " " in i:
                t=i.split(" ")
                temp=[]
                for j in t:
                    temp.append(int(j))
                arr1.append(temp)
            else:
                arr1.append([int(i)])
        arr1=np.matrix(arr1)
    elif fname==2:    
        for i in l:
            i=i.replace('\n','')
            if " " in i:
                t=i.split(" ")
                temp=[]
                for j in t:
                    temp.append(int(j))
                arr2.append(temp)
            else:
                arr2.append([int(i)])
        arr2=np.matrix(arr2)
    fname+=1
#checking whether the dimensions are equal of input arrays
if arr1.shape!=arr2.shape:
    with open("addOp.txt","w") as f:
        f.write("Addition cannot be performed! matrices does not have similar dimension")
#if follows then add two arrays
else:
    add=arr1+arr2
    add=np.array(add)
    #writing the addition in textfile
    with open("addOp.txt","w") as addout:
        addout.write(f"{add.shape[0]} {add.shape[1]}\n")
        for row in add:
            addout.write(" ".join(str(a) for a in row))
            addout.write("\n")
#checking whether the cols of array1 and row of array2 is equal or not  
if arr1.shape[1]!=arr2.shape[0]:
    with open("multOp.txt","w") as f:
        f.write("Multiplication cannot be done as col of matrixA is not equal to row of matrixB")
# if follows then multiplying it
else:
    mul=arr1*arr2
    mul=np.array(mul)
    #writing the multiplication array in text
    with open("multOp.txt","w") as mulout:
        mulout.write(f"{mul.shape[0]} {mul.shape[1]}\n")
        for row in mul:
            mulout.write(" ".join(str(a) for a in row))
            mulout.write("\n")















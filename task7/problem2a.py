import sys
import numpy as np
import os
lA=[]
lB=[]
with open(sys.argv[1]) as f1:
    l=f1.readlines()   
    l.remove(l[0])
for i in l:
    i=i.replace('\n','')
    if " " in i:
        t=i.split(" ")
        temp=[]
        for j in t:
            temp.append(int(j))
        lA.append(temp)
    else:
        lA.append([int(i)])
arrA=np.matrix(lA)    
with open(sys.argv[2]) as f2:
    m=f2.readlines()
for i in m:
    i=i.replace('\n','')
    lB.append([int(i)])
arrB=np.matrix(lB)
n=arrA.shape[0]
#condition 1 when n=0
if n==0:
    print("Sorry matrix is empty")
    exit()
#condition 2 when n=1
elif n==1: 
    if lA[0][0]!=0:
        with open("problem2aOp.txt","w") as f5:
            f5.write("Unique Solution")
    elif lA[0][0]==0 and lB[0][0]!=0:
        with open("problem2aOp.txt","w") as f5:
            f5.write("No Solution")
    elif lA[0][0]==0 and lB[0][0]==0:
        with open("problem2aOp.txt","w") as f5:
            f5.write("Infinite Solution")
        
#condition 3 when n=2
elif n==2:
    # checking if delta is 0 or not
    if np.linalg.det(arrA)!=0.0:
        with open("problem2aOp.txt","w") as f6:
            f6.write("Unique Solution")
    else:
        #obtaining matrix delx
        delx=[]
        for i in range(len(arrA)):
            delx.append(lB[i]+[lA[i][1]])
        delx=np.matrix(delx)
        if np.linalg.det(delx)!=0.0:
            with open("problem2aOp.txt","w") as f6:
                f6.write("No solution")
        else:
            #obtaining matrix dely
            dely=[]
            for i in range(len(arrA)):
                dely.append([lA[i][0]]+lB[i])
            dely=np.matrix(dely)
            if np.linalg.det(dely)!=0.0:
                with open("problem2aOp.txt","w") as f6:
                    f6.write("No solution")
            else:
                with open("problem2aOp.txt","w") as f6:
                    f6.write("Infinite solution")

#condition 4 when n==3
elif n==3:
    if np.linalg.det(arrA)!=0.0:
        with open("problem2aOp.txt","w") as f3:
            f3.write("Unique solution")
    else:
        #obtaining the delx
        delx=[]
        for i in range(len(arrA)):
            delx.append(lB[i]+lA[i][1:])
        delx=np.matrix(delx)
        if np.linalg.det(delx)!=0.0:
            with open("problem2aOp.txt","w") as f6:
                f6.write("No solution")
        else:
            #obtaining the dely
            dely=[]
            for i in range(len(arrA)):
                dely.append([lA[i][0]]+lB[i]+[lA[i][2]])
            dely=np.matrix(dely)
            if np.linalg.det(dely)!=0.0:
                with open("problem2aOp.txt","w") as f6:
                    f6.write("No solution")
            else:
                #obtaining the delz
                delz=[]
                for i in range(len(arrA)):
                    delz.append(lA[:2]+lB[i])
                delz=np.matrix(dely)
                if np.linalg.det(delz)!=0.0:
                    with open("problem2aOp.txt","w") as f6:
                        f6.write("No solution")
                else:
                    with open("problem2aOp.txt","w") as f6:
                        f6.write("Infinite solution")




    






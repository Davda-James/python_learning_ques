#importing different libraries and modules
import sys
import os 
import numpy as np
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
n=np.shape(arrA)[0]
if n==0:
    print("Sorry matrix is empty")
    exit()
#condition 2 when n=1
elif n==1: 
    if arrA[0][0]==0 and arrB[0][0]!=0:
        with open("problem2bOp.txt","w") as f5:
            f5.write("No solution")
    elif arrA[0][0]==0 and arrB[0][0]==0:
        with open("problem2bOp.txt","w") as f5:
            f5.write(f"Infinite solution\n{n} {1}\n{1}")
    elif arrA[0][0]!=0:
        with open("problem2bOp.txt","w") as f5:
            sol=format(arrB[0][0]/arrA[0][0],".2f")
            f5.write(f"Unique solution\n{n} {1}\n{sol}")
#condition 3 when n=2
elif n==2:
    # checking whether the delta is o or not
    if np.linalg.det(arrA)!=0.0:
        with open("problem2bOp.txt","w") as f6:
            sol=np.linalg.solve(arrA,arrB)
            sol=np.array(sol)
            a=format(sol[0][0],".2f")
            b=format(sol[1][0],".2f")
            f6.write(f"Unique solution\n{n} {1}\n{a}\n{b}")
    else:
        #obtaining matrix delx
        delx=[]
        for i in range(len(arrA)):
            delx.append(lB[i]+[lA[i][1]])
        delx=np.matrix(delx)
        if np.linalg.det(delx)!=0.0:
            with open("problem2bOp.txt","w") as f6:
                f6.write("No solution")
        else:
            #obtaining matrix dely
            dely=[]
            for i in range(len(arrA)):
                dely.append([lA[i][0]]+lB[i])
            dely=np.matrix(dely)
            if np.linalg.det(dely)!=0.0:
                with open("problem2bOp.txt","w") as f6:
                    f6.write("No solution")
            else:
                with open("problem2bOp.txt","w") as f6:
                    soly=format((lB[0][0]-lA[0][0])/lA[0][1],".2f")
                    f6.write(f"Infinite solution\n{n} {1}\n{1}\n{soly}")
#condition 4 when n==3
elif n==3:
    if np.linalg.det(arrA)!=0.0:
        with open("problem2bOp.txt","w") as f3:
            sol=np.linalg.solve(arrA,arrB)
            sol=np.array(sol)
            f3.write(f"Unique solution\n{n} {1}\n")
            for row in sol:
                f3.write(" ".join(str(format(a,".2f")) for a in row))
                f3.write("\n")
    else:
        #obtaining the delx
        delx=[]
        for i in range(len(arrA)):
            delx.append(lB[i]+lA[i][1:])
        delx=np.matrix(delx)
        if np.linalg.det(delx)!=0.0:
            with open("problem2bOp.txt","w") as f6:
                f6.write("No solution")
        else:
            #obtaining the dely
            dely=[]
            for i in range(len(arrA)):
                dely.append([lA[i][0]]+lB[i]+[lA[i][2]])
            dely=np.matrix(dely)
            if np.linalg.det(dely)!=0.0:
                with open("problem2bOp.txt","w") as f6:
                    f6.write("No solution")
            else:
                #obtaining the delz
                delz=[]
                for i in range(len(arrA)):
                    delz.append(lA[:2]+lB[i])
                delz=np.matrix(dely)
                if np.linalg.det(delz)!=0.0:
                    with open("problem2bOp.txt","w") as f6:
                        f6.write("No solution")
                else:
                    with open("problem2bOp.txt","w") as f6:
                        soly=format((((arrB[0][0]*arrA[1][2]-arrB[1][0]*arrA[0][2]))-(arrA[1][2]*arrA[0][0]-arrA[0][2]*arrB[1][0])*1)/(arrA[0][1]*arrA[1][2]-arrA[1][1]*arrA[0][2]),".2f")
                        solz=format((arrB[0][0]-arrA[0][0]-arrA[0][1]*soly)/arrA[0][2],".2f")
                        f6.write(f"Infinite solution\n{n} {1}\n{1}\n{soly}\n{solz}")



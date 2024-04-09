import sys
#importing different modules or libraries
import os 
import random 
import numpy as np
#taking input from user and storing it in variable rows and columns
r1=int(sys.argv[1])
c1=int(sys.argv[2])
r2=int(sys.argv[3])
c2=int(sys.argv[4])
#creating matrix with random data
matrixA=np.random.randint(10,size=(r1,c1))
matrixB=np.random.randint(10,size=(r2,c2))
#writing to MatA file
with open("MatA.txt","w") as f:
    f.write(f"{r1} {c1}\n")
    for row in matrixA:
        f.write(" ".join(str(a) for a in row))
        f.write("\n")
#writing to MatB file
with open("MatB.txt","w") as f:
    f.write(f"{r2} {c2}\n")
    for row in matrixB:
        f.write(" ".join(str(a) for a in row))
        f.write("\n")



    
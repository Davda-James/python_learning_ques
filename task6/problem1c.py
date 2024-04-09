import sys
import numpy as np
import math
def read_args():
    #checking whether the user has given input or not or has entered required no of arguments
    if len(sys.argv)!=4 and len(sys.argv)!=1:
        print("Please enter 3 file names as argument in terminal")
        exit()
    elif len(sys.argv)==1:
        #checking whether the user has given no input files
        print("Usage: python problem1c.py [file name (Seperated by space)]")
        exit()
    return sys.argv[1:]
lfile=read_args()
fileno=0

# while fileno<=len(lfile):
while fileno<len(lfile):
    with open(lfile[fileno],"r") as f:
        #reading the file
        data=f.readlines()
        #changes in data
        data[0]=data[0][2:]
        data[1]=data[1][2:]
        #taking data from string format to integer
        #error handling thrown during runtime 
        try:
            xvalues=list(map(int,data[0].split()))
            yvalues=list(map(int,data[1].split()))
        except ValueError as e:
            print("Please check the file, it contains some other character then integers")
            fileno+=1
            continue
    #finding correlation i.e r
    xvalues=np.array(xvalues)
    yvalues=np.array(yvalues)
    xyvalues=np.multiply(xvalues,yvalues)
    #finding mean
    meanxy=sum(xyvalues)/len(xyvalues)
    meanx=sum(xvalues)/len(xvalues)
    meany=sum(yvalues)/len(yvalues)
    stdxvalues=(sum((xvalues-meanx)**2)/len(xvalues))**0.5
    stdyvalues=(sum((yvalues-meany)**2)/len(yvalues))**0.5
    r=(meanxy-(meanx*meany))/(stdxvalues*stdyvalues)
    r=str(r)
    #writing to file 
    with open("Output1c.txt","a") as f2:
        f2.write(f"{r} ")
    # increment in fileno to access differenct files in lfile
    fileno+=1
        
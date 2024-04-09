import matplotlib.pyplot as plt
import sys
def read_args():
    #checking whether the user has given input or not or has entered required no of arguments
    if len(sys.argv)!=4 and len(sys.argv)!=1:
        print("Please enter 3 file names as argument in terminal")
        exit()
    elif len(sys.argv)==1:
        #checking whether the user has given no input files
        print("Usage: python problem1b.py [file name (Seperated by space)]")
        exit()
    return sys.argv[1:]
lfile=read_args()
fileno=0
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
            #plotting the graph of xvalues and yvalue
            plt.scatter(xvalues,yvalues,color="red")
            plt.title(f"X values vs Y values of data {fileno+1}",fontsize=20)
            plt.xlabel("X values",fontsize=15)
            plt.ylabel("Y values",fontsize=15)
            plt.show()
        except ValueError as e:
            print("Please check the file, it contains some other character then integers")
            fileno+=1
            continue
    #increment in index of filename stored in list
    fileno+=1



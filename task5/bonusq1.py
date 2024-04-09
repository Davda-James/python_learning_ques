#a. calculating correlation coefficient of given data
#importing required libraries
import math
import pandas as p 
# imprting and print Data.csv file
import pandas as pd
#use pandas to read the CSV 
csvData=pd.read_csv('Data.csv',sep=',')
listloan=csvData['B'].head(12)
listloan=listloan.tolist()
listcapita=csvData['I'].head(12)
listcapita=listcapita.tolist()
meanloan=sum(listloan)/2
meancapita=sum(listcapita)/2
#declaring three variables with initial value 0
sum1=0
sum2=0
sum3=0
for i in range(len(listloan)):
    sum1=(listloan[i]-meanloan)*(listcapita[i]-meancapita)+sum1
    sum2=(listloan[i]-meanloan)**2 +sum2
    sum3=(listloan[i]-meancapita)**2 + sum3
correlationcoeff=sum1/math.sqrt(sum2*sum3)
# printing the correlation coefficient
print("correlation coefficient is:",correlationcoeff)



#b. creating a scatter plot 
#importing matplotlib.pyplot
import matplotlib.pyplot as plt
def scatterplot(listloan,listcapita):
    plt.xlabel("listloan",fontsize=15)
    plt.ylabel("listcapita",fontsize=15)
    plt.title("listloan Vs listcapita")
    plt.scatter(listloan,listcapita,color="green")
    plt.show()
scatterplot(listloan,listcapita)

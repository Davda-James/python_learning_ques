#a. writing a function on information on population denstiy.per of margial farmers,per of women in overall workforce
import pandas as pd
#use pandas to read the CSV 
csvData=pd.read_csv('Data.csv',sep=',')
#convert dataframe into numpy array
csvDataNum=csvData.to_numpy()
#function displaying info about poppulation density
def popden(csvData):
    listf=csvData['F'].head(12)
    listf=listf.tolist()
    lists=csvData['State'].head(12)
    lists=lists.tolist()
    print("state with highest population density is:",lists[listf.index(max(listf))])
    print("state with lowest population density is:",lists[listf.index(min(listf))])
    #finding median
    listmedian=listf.copy()
    listmedian.sort()
    if len(listmedian)%2==0:
        print("median of population density is:",listmedian[int(len(listmedian)/2)])

    else:
        print("median of population density is:",listmedian[int((len(listmedian)+1)/2)])
    print("average of population density is:",sum(listf)/len(listf))
    #finding mode
    count=0
    maxrepel=0
    inx=0
    for i in range(len(listf)):
        if listf.count(listf[i])>1:
            count=listf.count(listf[i])
        if count>maxrepel:
            maxrepel=count
            inx=i
    print("mode of population density is:",listf[inx])

#function for per of marginal farmers info
def marfarm(csvData):
    listf=csvData['G'].head(12)
    listf=listf.tolist()
    lists=csvData['State'].head(12)
    lists=lists.tolist()
    print("state with highest per of marginal farmers is:",lists[listf.index(max(listf))])
    print("state with lowest per of marginal farmers is:",lists[listf.index(min(listf))])
    listmedian=listf.copy()
    listmedian.sort()
    #finding median
    if len(listmedian)%2==0:
        print("median of per of marginal farmers is:",listmedian[int(len(listmedian)/2)])

    else:
        print("median of per of marginal farmers is:",listmedian[int((len(listmedian)+1)/2)])
    #finding mode
    print("average of per of marginal farmers is:",sum(listf)/len(listf))
    count=0
    maxrepel=0
    inx=0
    for i in range(len(listf)):
        if listf.count(listf[i])>1:
            count=listf.count(listf[i])
        if count>maxrepel:
            maxrepel=count
            inx=i
    print("mode of per of marginal farmers is:",listf[inx])

#finding median 
def womwork(csvData):
    listf=csvData['K'].head(12)
    listf=listf.tolist()
    lists=csvData['State'].head(12)
    lists=lists.tolist()
    print("state with highest per of women in overall workforce is:",lists[listf.index(max(listf))])
    print("state with lowest per of women in overall workforce is:",lists[listf.index(min(listf))])
    listmedian=listf.copy()
    listmedian.sort()
    #finding mode
    if len(listmedian)%2==0:
        print("median of per of women in overall workforce is:",listmedian[int(len(listmedian)/2)])

    else:
        print("median of per of women in overall workforce is:",listmedian[int((len(listmedian)+1)/2)])
    print("average of per of women in overall workforce is:",sum(listf)/len(listf))
    #finding mode
    count=0
    maxrepel=0
    inx=0
    for i in range(len(listf)):
        if listf.count(listf[i])>1:
            count=listf.count(listf[i])
        if count>maxrepel:
            maxrepel=count
            inx=i
    print("mode of per of women in overall workforce is:",listf[inx])

popden(csvData)
marfarm(csvData)
womwork(csvData)



#b. plotting the bar graph 
# x-> countries
# y -> different information 
import numpy as np
import matplotlib.pyplot as plt
listd=csvData['D'].head(12)
listd=listd.tolist()
liste=csvData['E'].head(12)
liste=liste.tolist()
liststate=csvData['State'].head(12)
liststate=liststate.tolist()
width=0.4
listst=np.arange(len(liststate))
lists=[width+i for i in listst]
plt.xlabel("States",fontsize=0.2)
plt.ylabel("Information",fontsize=0.2)
plt.title("STATE INFORMATION ON DIFF TOPICS")
plt.bar(listst,listd,width,color="orange",label="average per area with > 30per slope")
plt.bar(lists,liste,width,color="blue",label="road density")
plt.legend()
plt.show()



#c. creating bar chart for states in ascending order having area with slope>30per showing road density
import numpy as np
import matplotlib.pyplot as plt
#sortirng D column of Data.csv file 
sortedcsvData=csvData.sort_values('D')
sortedstate=sortedcsvData['State'].head(12)
sortedd=sortedcsvData['D'].head(12)
sortede=sortedcsvData['E'].head(12)
# #bar graph plotting
plt.title("States Vs Road Density")
plt.xlabel("States",fontsize=15)
plt.ylabel("Road Density")
width=0.4
plt.bar(sortedstate,sortede,width,color="red",fill="false",hatch='*')
plt.show()


#EXTRA QUESTION 
extrasorted=csvData.sort_values('K')
extrak=extrasorted['K'].head(12)
extrak=extrak.tolist()
extrapci=extrasorted['I'].head(12)
extrapci=extrapci.tolist()
if extrak.index(max(extrak))==extrapci.index(max(extrapci)):
    print("YES")
else:
    print("False")






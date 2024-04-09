#importing important library and modules required
import random
import matplotlib.pyplot as plt 
import random
''' Uncomment the trials one by one and after running one trial please uncomment the other as if not uncommented the graph will be overlapped
    Also there are already stored image after running one by one trial in folder, visit it to see the figure if not want to run the whole program one by one
'''
#trials is 50
count0=0
count1=0
count2=0
count3=0 
freq0=[]
freq1=[]
freq2=[]
freq3=[]
notrials=[]
for i in range(50):
    num=random.randint(0,3)
    if num==0:
        count0+=1
    elif num==1:
        count1+=1
    elif num==2:
        count2+=1
    else:
        count3+=1
    notrials.append(i+1)
    freq0.append(count0/(i+1))
    freq1.append(count1/(i+1))
    freq2.append(count2/(i+1))
    freq3.append(count3/(i+1))
plt.plot(notrials,freq0,color='b',marker="*",label="0 Outcome")
plt.plot(notrials,freq1,color='r',marker="d",label="1 Outcome")
plt.plot(notrials,freq2,color='g',marker="2",label="2 Outcome")
plt.plot(notrials,freq3,color='orange',marker="^",label="3 Outcome")
plt.xlabel("No of Trials")
plt.ylabel("Relative Frequency")
plt.title("50 Trials Vs Relative Frequency")
plt.savefig("problem3a_50.png")

#trials is 500
# count_500_0=0
# count_500_1=0
# count_500_2=0
# count_500_3=0
# freq_500_0=[]
# freq_500_1=[]
# freq_500_2=[]
# freq_500_3=[]
# notrials1=[]
# for i in range(500):
#     num=random.randint(0,3)
#     if num==0:
#         count_500_0+=1
#     elif num==1:
#         count_500_1+=1
#     elif num==2:
#         count_500_2+=1
#     else:
#         count_500_3+=1
#     notrials1.append(i+1)
#     freq_500_0.append(count_500_0/(i+1))
#     freq_500_1.append(count_500_1/(i+1))
#     freq_500_2.append(count_500_2/(i+1))
#     freq_500_3.append(count_500_3/(i+1))
# plt.plot(notrials1,freq_500_0,color='b',label="0 Outcome")
# plt.plot(notrials1,freq_500_1,color='r',label="1 Outcome")
# plt.plot(notrials1,freq_500_2,color='g',label="2 Outcome")
# plt.plot(notrials1,freq_500_3,color='orange',label="3 Outcome")
# plt.xlabel("No of Trials")
# plt.ylabel("Relative Frequency")
# plt.title("500 Trials Vs Relative Frequency")
# plt.savefig("problem3a_500.png")

#trials is 5000
# count_5000_0=0
# count_5000_1=0
# count_5000_2=0
# count_5000_3=0
# freq_5000_0=[]
# freq_5000_1=[]
# freq_5000_2=[]
# freq_5000_3=[]
# notrials2=[]
# for i in range(5000):
#     num=random.randint(0,3)
#     if num==0:
#         count_5000_0+=1
#     elif num==1:
#         count_5000_1+=1
#     elif num==2:
#         count_5000_2+=1
#     else:
#         count_5000_3+=1
#     notrials2.append(i+1)
#     freq_5000_0.append(count_5000_0/(i+1))
#     freq_5000_1.append(count_5000_1/(i+1))
#     freq_5000_2.append(count_5000_2/(i+1))
#     freq_5000_3.append(count_5000_3/(i+1))
# plt.plot(notrials2,freq_5000_0,color='b',label="0 Outcome")
# plt.plot(notrials2,freq_5000_1,color='r',label="1 Outcome")
# plt.plot(notrials2,freq_5000_2,color='g',label="2 Outcome")
# plt.plot(notrials2,freq_5000_3,color='orange',label="3 Outcome")
# plt.xlabel("No of Trials")
# plt.ylabel("Relative Frequency")
# plt.title("5000 Trials Vs Relative Frequency")
# plt.savefig("problem3a_5000.png")

#trials is 50000
# count_50000_0=0
# count_50000_1=0
# count_50000_2=0
# count_50000_3=0
# freq_50000_0=[]
# freq_50000_1=[]
# freq_50000_2=[]
# freq_50000_3=[]
# notrials3=[]
# for i in range(50000):
#     num=random.randint(0,3)
#     if num==0:
#         count_50000_0+=1
#     elif num==1:
#         count_50000_1+=1
#     elif num==2:
#         count_50000_2+=1
#     else:
#         count_50000_3+=1
#     notrials3.append(i+1)
#     freq_50000_0.append(count_50000_0/(i+1))
#     freq_50000_1.append(count_50000_1/(i+1))
#     freq_50000_2.append(count_50000_2/(i+1))
#     freq_50000_3.append(count_50000_3/(i+1))
# plt.plot(notrials3,freq_50000_0,color='b',label="0 Outcome")
# plt.plot(notrials3,freq_50000_1,color='r',label="1 Outcome")
# plt.plot(notrials3,freq_50000_2,color='g',label="2 Outcome")
# plt.plot(notrials3,freq_50000_3,color='orange',label="3 Outcome")
# plt.xlabel("No of Trials")
# plt.ylabel("Relative Frequency")
# plt.title("50000 Trials Vs Relative Frequency")
# plt.savefig("problem3a_50000.png")

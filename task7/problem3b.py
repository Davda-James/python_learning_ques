#imporing library and modules required
import matplotlib.pyplot as plt
import numpy as np
''' Uncomment the trials one by one and after running one trial please uncomment the other as if not uncommented the graph will be overlapped
    Also there are already stored image after running one by one trial in folder, visit it to see the figure if not want to run the whole program one by one
'''
#5 trials for 50000 times
means=[]
for i in range(50000):
    sumnum=0
    for j in range(5):
        num=np.random.randint(0,3)
        sumnum+=num
    means.append(sumnum/5)
plt.title("Histogram of sample means of 5 trials for 50000 times")
plt.xlabel("means")
plt.hist(means,bins=15,edgecolor="black",linewidth=1)
plt.savefig("problem3b_5_50000.png")

#50 trials for 50000 times
# mean2=[]
# for i in range(50000):
#     sumnum=0
#     for j in range(50):
#         num=np.random.randint(0,3)
#         sumnum+=num
#     mean2.append(sumnum/50)
# plt.title("Histogram of sample means of 50 trials for 50000 times")
# plt.xlabel("means")
# plt.hist(mean2,bins=15,edgecolor="black",linewidth=1)
# plt.savefig("problem3b_50_50000.png")

    


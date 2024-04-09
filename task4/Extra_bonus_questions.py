# importing numerical python package for finding roots
from numpy.polynomial import polynomial as p
#q1. bonus
#taking input of polynomial's degree
p_deg=int(input("enter degree of polynomial:"))
p_list=[]
for i in range(-1,p_deg):
    y=int(input(f"enter {i+1} power of x polynomial:"))
    p_list.append(y)
print("roots of polynomial are:",p.polyroots(p_list))



#q2. bonus
#taking any elements in list in any order
list=[5,1,4,9,2,6]
#sorting list using selection sort
index=0
for j in range(0,len(list)-2):
    min=list[j]
    for i in range(j+1,len(list)):
        if list[i]<min:
            min=list[i]
            index=list.index(min)
    temp=list[j]
    list[j]=min
    list[index]=temp
print(list)


#a. sorting lists
#creating list
list1=[]
#taking input from user for no of elements in list1
n=int(input("enter number of elements in list1:"))
for i in range(0,n):
    x=int(input(f"enter {i+1} element:"))
    list1.append(x)
#sorting list1 in ascending order
list2=list1.copy()
list2.sort()
print(list2)
list2.reverse()
print(list2)

#b. replicating the list x number of times
#taking input from user of x
N=int(input("enter N(times you want to replicate the string:"))
print(list1*N)

#c. printing max and min in list
print(f"max of list1 is: {max(list1)}")
print(f"min of list1 is {min(list1)}")

#d. printing index of element in list
#taking input from user of element of which we have to print index 
k=int(input("enter k:"))
print(list1.index(k))

#e. printing sum of elements of list
print(sum(list1))






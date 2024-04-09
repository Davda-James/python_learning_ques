# a. fibonacci using function 
#creating a function fibonacci 
def fibonacci(n):
    series=[0,1]
    while len(series) <n:
        nextnum=series[-1]+series[-2]
        series.append(nextnum)
    
    for num in series:
        print(num,end=" ")
n=int(input("enter n:"))
fibonacci(n)
print()


#b.  printing the majority in list
#defining a variable count to calculate no of repeatation
def majority(list2):
    maxcount=0
    count=0
    inx=0
    for i in range(0,len(list2)-1):
        count=1
        for j in range(i+1,len(list2)):
            #comparing element
            if list2[j]==list2[i]:
                count+=1             
            #updating value of maxcount
            if count>=maxcount:
                maxcount=count
                inx=i
    if maxcount>int(len(list2)/2):
        print("majority element is/are:",list2[inx])
    else: 
        print("-1")

list2=[]
x=int(input("enter the no of elements you want to add in list2:",))
#taking input from user if list2 elements by using loop 
for i in range(0,x):
    y=int(input(f"enter {i+1} element:"))
    list2.append(y)
majority(list2)



#c. printing the first number that repeats
# taking input from user for z for ques c.
z=int(input("enter number of elements you want to add in list3:"))
list3=[]
#appending the number in list3
for i in range(0,z):
    m=int(input(f"enter {i+1} element:"))
    list3.append(m)
condition=False
#checking the elements in list
for i in range(0,len(list3)):
    for j in range(i+1,len(list3)):
        if list3[j]==list3[i]:
            condition=True
            print(list3[i])
            break
    if condition==True:
       break
if condition==False:
    print("no repeating element exist")

#d. printing the pattern triangle
#d. printing the pattern triangle
rows=int(input("enter rows of pattern to print:"))
for i in range(rows):
    # printing spaces
    k=rows-1-i
    while k>=1:
        print(" ",end="")
        k-=1
    # printng increasing number upto limit
    for j in range(0,i+1):
        print(j+1,end="")
        if j==i:
            # printing numnber in decreasing order upto limit
            while j>=1:
                print(j,end="")
                j-=1
    print()


#e. removing the repeated elements from list 
# taking input from user
list4=[]
#taking input from user for number of elements in list4
o=int(input("enter number of elements to be entered for list4:"))
for i in range(0,o):
    element=int(input(f"enter {i+1} element:"))
    list4.append(element)
for j in list4:
     if list4.count(j)>1:
          list4.remove(j)
print(list4)

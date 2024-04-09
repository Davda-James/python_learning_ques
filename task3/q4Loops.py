#a. reversing the string usng loop
str=input("enter string:")
str1=""
for i in str:
    str1=i+str1
print("reversed string is:",str1)

#b. printing sum of odd no and even no
N=int(input("enter N: "))
evenSum=0
oddSum=0
for i in range(1,N):
    if i%2==0:
        evenSum=evenSum+i
    else:
        oddSum=oddSum+i
print("sum of odd numbers less than N is:",oddSum,end="")
print(" and sum of even numbers less than N is:",evenSum)

#c. printing the factorial of number using while loop
n=int(input("enter n: "))
i=n-1
factorial =n
while i>=2:
    factorial=factorial*i
    i-=1
print("factorial of n is: ",factorial)


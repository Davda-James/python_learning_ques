#checking whether the string is palindrome or not 
str=input("enter a string:")
i=0
j=len(str)-1
condition=True
while i<=j:
    if str[i]==str[j]:
        condition=True
        i+=1
        j-=1
    else:
        condition=False
        break
if condition==True:
    print("yes the string is palindrome")
else:
    print("sorry! the string is not a palindrome!")



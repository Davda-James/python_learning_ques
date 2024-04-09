#concatenating the string after slicing
str=input("enter string:")
evenposstr=[]
oddposstr=[]
for i in range(0,len(str)):
    if i%2==0:
        evenposstr.append(str[i])
    else:
        oddposstr.append(str[i])
str1= "".join(evenposstr)
str2= "".join(oddposstr)
print(str1+str2)
        
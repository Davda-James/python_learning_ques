#dividing the even and odd letter of str and then concatenating after processing it 
str=input("enter string:")
x=len(str)
if x%2==0:
    str1=str[0:int(x/2)]
    str2=str[int(x/2):x]
else:
    str1=str[0:int((x+1)/2)]
    str2=str[int((x+1)/2):x]
str2=str2[::-1]
newstr=str2+" " +str1
print(newstr)
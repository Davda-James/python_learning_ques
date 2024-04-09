#reversing the string using negative indexing 
str=input("enter a string:") + "  "
newstr1=str[-1:-len(str)-1:-1]
print(newstr1)

#reversing the string by positive indexing
newstr2=newstr1[len(str)-1:1:-1]
print(newstr2)
print(newstr1,newstr2)
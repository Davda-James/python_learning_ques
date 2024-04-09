#using new method to replace words
str="Anyone can learn python, python is so easy.The best way to learn python is using it for different tasks."
y=str.rindex("python")
x=len(str)
print(x)
str1=str[:x-y]
str2=str[x-y:x]
str1=str1.replace("python","coding",1)
str2=str2.replace("python","coding")
newstr=str1 + str2
print(newstr)
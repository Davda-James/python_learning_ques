#changing the words in the string
str="Anyone can learn python, python is so easy.The best way to learn python is using it for different tasks."
str=str.replace("python","coding",1)
str1=str[:len(str)-39]
str2=str[len(str)-39:len(str)]
str2=str2.replace("python","coding")
newstr=str1+str2
print(newstr)
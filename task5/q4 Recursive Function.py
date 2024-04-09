#a. modifying the string using recursive call
#defining function
def prefRevCapStr(newstring):
    if len(newstring)==1:
        return newstring
    else:
        return prefRevCapStr(newstring[1:]) +newstring[0]

#taking input of string 
string=input("enter string:")
newstring=string.upper()
print(prefRevCapStr(newstring)+ " -> " + string)

#b. finding if substring exist in other string 
#defining a function
def scatSubStr(s,w):
    condition=True
    l=[]
    for j in range(len(s)//len(w)):
        for i in w:
            if i in s:
                l.append(i)
                s=s[s.index(i)+1:]
            else:
                break
        n=len(w)
    if len(l)//3>=1:
        print("Yes")
        # ans of extra question 
        print("occurence of w in s is:",len(l)//3)
    else:
        print("False")
# taking input of two strings
s=input("enter string s:")
w=input("enter string w:")
scatSubStr(s,w)




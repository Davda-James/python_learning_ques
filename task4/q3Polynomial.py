#a. returning the coefficient of polynomial
#taking the input from user for degree of polynomial
n=int(input("enter n:"))
def coefficient():
    listofcoefficient=[]
    for i in range(-1,n):
        x=int(input(f"enter coefficient of x^{i+1}:"))
        listofcoefficient.append(x)
    str=""
    for j in range(-1,n):
        if j==-1:
            str=f" {listofcoefficient[j+1]}x^{j+1}" +str
        if j>-1:
            str=f" {listofcoefficient[j+1]}x^{j+1} +" +str
    
    print("polynomial is:",str)
    m=int(input("enter the degree of which you want to see coefficient:"))
    if m>n:
        print("sorry degree is out of polynomial degree you entered")
    else:
        print(f"degree of x^{m} is:",listofcoefficient[m])
coefficient()

#b. giving value of function 
# f(x)= 4x^3-6x^2+0x-1
def output(x):
    return (4*x*x*x) - (6*x*x) -1
x=int(input("enter x:"))
print(output(x))

#c. adding two polynomials

# taking input of degree of polynomial
d1=int(input("enter the degree of polynomial 1:"))
d2=int(input("enter the degree of polynomial 2:"))
#creating a list of coefficients of list
p1=[]
p2=[]
for i in range(-1,d1):
    y=int(input(f"enter coefficient of {i+1} power of polynomial 1:"))
    p1.append(y)
for j in range(-1,d2):
    y=int(input(f"enter coefficient of {j+1} power of polynomial 2:"))
    p2.append(y)
#creating a string and appending it 
str1=""
str2=""
for l in range(-1,d1):
    if l==-1:
        str1=f" {p1[l+1]}x^{l+1}"
    if l>-1:
        str1=f" {p1[l+1]}x^{l+1} +" +str1
for m in range(-1,d2):
    if m==-1:
        str2=f" {p2[m+1]}x^{m+1}"+ str2
    if m>-1:
        str2=f" {p2[m+1]}x^{m+1} +"+str2
#printing a polynomial
print("polynomial 1 is:",str1)
print("polynomial 2 is:",str2)
if len(p1)>len(p2):
    for i in range(0,d1-d2):
        p2.append(0)
elif len(p1)<len(p2):
    for i in range(0,d2-d1):
        p1.append(0)
finalpolynomial=[]
for i in range(-1,len(p1)-1):
    finalpolynomial.append(p1[i+1]+p2[i+1])

newstr=""
for k in range(-1,len(p1)-1):
    if k==-1:
        newstr=f" {finalpolynomial[k+1]}x^{k+1}"
    if k>-1:
        newstr=f" {finalpolynomial[k+1]}x^{k+1} +"+newstr
print("sum of two polynomials is:",newstr)



#a.printing if number is postive 
x=(input("enter number x: "))
if x.isnumeric()==True:
    print(int(x))

#b. printing -1,0,1 on basis of diff conditions 
a=(input("enter number a: "))
if int(a)>0 and int(a)!=0:
    print("1")
elif int(a)==0:
    print("0")
elif int(a)<0: 
    print("-1")

#c. printing on basis of different conditions
str=input("enter a string:")
if str.isnumeric()==True :
    print("only digits!")
elif str.isalpha()==True :
    print("only alphabets!")
elif str.isalnum()==True :
    print("both digits and alphabets!")

#d. printing no of days in month
year=int(input("enter year: "))
month=input("enter month: ")
condtion=True
if month=="january" or month=="march" or month=="may" or month=="july" or month=="september" or month=="october" or month=="december":
    print("no of days in this month is 31")
elif month=="february":
    if year%4==0 and year%100!=0:
        condition=True
    elif year%100==0 and year%400==0:
        condition=True
    else:
        condition=False
    if condition==True:
        print("no of days in this month is 29")
    else:
        print("no of days in this month is 28")
else:
    print("no of days in this month is 30")


#e. mac of x,y,z
x=int(input("enter x: "))
y=int(input("enter y: "))
z=int(input("enter z: "))
print(max(x,y,z))


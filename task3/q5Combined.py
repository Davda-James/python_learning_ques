#a. printing whether the number is prime or not
N=int(input("enter N: "))
bool=True
for i in range(2,N):
    if N%i!=0 or N==2:
        bool=True
    else:
        bool=False
        break
        
if bool==True:
    print("N is prime")
else:
    print("N is not prime")

#b. printing whether the string is vowel dominant
str=input("enter string:")
vowels=0
consonants=0
for i in str:
    if str.isspace()==True:
        print("sorry wrong input string contain spaces")
        break
    elif i in {'a','e','i','o','u','A','E','I','O','U'}:
        vowels+=1
    else:
        consonants+=1

if vowels>consonants:
    print("str is vowel dominant")
elif vowels<consonants:
    print("string is consonant dominant")
elif vowels==consonants:
    print("string is neutral it is neither vowel nor consonant dominant")

#c. printing no of digits in string using function
str2=input("enter string:")
def calofdig(str2):
    digits=0
    for i in str2:
        if i.isnumeric()==True:
            digits+=1
    return digits
print(calofdig(str2))  
#d. printing the number of letters in string 
str1=input("enter string:")
def calofletter(str1):
    letter=0
    for i in str1:
        if i.isalpha()==True:
            letter+=1
        else:
            continue
    return letter
print("no of letter in string is:",calofletter(str1))


#e. divisors of n
def divisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
        else:
            pass
    return 
n=int(input("enter n: "))
divisors(n)

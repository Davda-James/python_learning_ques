#a. implementing f,g,h,k as recursive function
def f(n):
    if n<2:
        return 1
    elif n>=2:
        return 1.65*f(n-1)
def g(n):
    if n<2:
        return 1
    elif n>=2:
        return g(n-1)+g(n-2)
def h(n):
    if n<2:
        return 2
    elif n>=2:
        return 2*f(n-1)
def k(n):
    if n<3:
        return 3
    elif n>=3:
        return k(n-1)+k(n-2)
print(f(4))
print(g(4))
print(h(4))
print(k(4))


#b. plotting scatter points of every graph
import matplotlib.pyplot as plt

# function for graph of f(x)
def gf(x):
    y=[f(j) for j in x]
    plt.xlabel("input values",fontsize=15)
    plt.ylabel("f(x) values",fontsize=15)
    plt.title("Graph of Function")
    plt.scatter(x,y,color="blue")
    plt.show()

# funciton for graph of g(x)
def gg(x):
    y=[g(j) for j in x]
    plt.xlabel("input values",fontsize=15)
    plt.ylabel("g(x) values",fontsize=15)
    plt.title("Graph of Function")
    plt.scatter(x,y,color="orange")
    plt.show()

# function for graph of h(x)
def gh(x):
    y=[h(j) for j in x]
    plt.xlabel("input values",fontsize=15)
    plt.ylabel("h(x) values",fontsize=15)
    plt.title("Graph of Function")
    plt.scatter(x,y,color="green")
    plt.show()

# function for graph of k(x)
def gk(x):
    y=[k(j) for j in x]
    plt.xlabel("input values",fontsize=15)
    plt.ylabel("k(x) values",fontsize=15)
    plt.title("Graph of Function")
    plt.scatter(x,y,color="violet")
    plt.show()


x=[i for i in range(0,10)]
gf(x)
gg(x)
gh(x)
gk(x)


#c. curves of f,g,h,k in single plot
def singleplot(x):
    z=[f(i) for i in x]
    l=[g(i) for i in x]
    m=[h(i) for i in x]
    n=[k(i) for i in x]
    plt.xlabel("input values")
    plt.ylabel("f,g,h,k function")
    plt.title("plotting all functions in single graph")
    plt.scatter(x,z,color="blue",label="f(x)")
    plt.scatter(x,l,color="orange",label="g(x)")
    plt.scatter(x,m,color="green",label="h(x)")
    plt.scatter(x,n,color="violet",label="k(x)")
    plt.show()

singleplot(x)
# EXTRA QUESTION OF SQUARE FUNCTION 
def square(x):
    return x**2
def gsquare(xvalue):
    y=[square(i) for i in xvalue]
    plt.xlabel("Values of x")
    plt.ylabel("Function Values")
    plt.title("Plot of Function")
    plt.scatter(xvalue,y,color="violet",label="square(x)")
    plt.legend()
    plt.show()
xvalue=[-(i/10) for i in range(100)]
for i in range(100):
    xvalue.append(i/10)
gsquare(xvalue)

import math
def exponential(x):
    return math.exp(x)
def gexponential(xvalue):
    y=[exponential(i) for i in xvalue]
    plt.xlabel("Values of x")
    plt.ylabel("Function Values")
    plt.title("Plot of Function")
    plt.scatter(xvalue,y,color="violet",label="square(x)")
    plt.legend()
    plt.show()
gexponential(xvalue)


    
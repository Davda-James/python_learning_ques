#Using for loop for finding index of element in array 
#importing sys module for command line utility
import sys 
#importing time module 
import time 
def find(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return f"index of {val} in arr is {i}"
    return f"Sorry {val} does not exist in array arr"
f1=sys.argv[1]
#reading the text file
with open(f1,"r") as f:
    l=f.readlines()
#value of which index we have to find index
val=int(l[0].strip())
#array in which we have to search 
arr=list(map(int,l[1].split()))
start_time=time.perf_counter_ns()
print(find(arr,val))
end_time=time.perf_counter_ns()
print("time taken by for loop method is:",end_time-start_time,"nano sec")


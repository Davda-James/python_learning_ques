# BINARY SEARCH
#importing sys
import sys
#importing time module 
import time 
#function of binary search
def binarysearch(arr,val):
    start=0
    end=len(arr)-1
    mid=start+(end-start)//2
    while start<=end:
        if val==arr[mid]:
            return f"index of {val} in arr is {mid}"
        elif val>arr[mid]:
            start=mid+1
        else:
            end=mid-1
        mid=start+(end-start)//2
    return "Sorry element does not exist in list"
f1=sys.argv[1]
#reading input text file
with open(f1,"r") as f:
    l=f.readlines()
val=int(l[0])
#converting array elements into integers
arr=list(map(int,l[1].split()))
# arr.sort()
# starting timer
start_time=time.perf_counter_ns()
#calling binary search function 
print(binarysearch(arr,val))
#ending timer
end_time=time.perf_counter_ns()
#printing time taken by BINARY SEARCH
print("time taken by BINARY SEARCH ALGORITHM is:",end_time-start_time,"nano sec")

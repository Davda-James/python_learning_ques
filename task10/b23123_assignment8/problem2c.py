#determining the time of both methods in problem 2a and problem 2b
#importing time module
import time
#importing random 
import random
# BINARY SEARCH
def binarysearch(arr,val):
    start=0
    end=len(arr)-1
    mid=start+(end-start)//2
    while start<=end:
        if val==arr[mid]:
            return
        elif val>arr[mid]:
            start=mid+1
        else:
            end=mid-1
        mid=start+(end-start)//2
    return
# finding index of element in array arr
def find(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return
    return
#randomly generated sorted list of 100000 elements
def random_list(size):
    random_list = random.sample(range(0, size * 10), size)
    return random_list
arr= random_list(100000)
arr.sort()
val=200000
# time calculation of Binary Search for 100000 elements
start_time_binary_search=time.perf_counter_ns()
binarysearch(arr,val)
end_time_binary_search=time.perf_counter_ns()
print("time taken by BINARY SEARCH is ",end_time_binary_search-start_time_binary_search,"nano sec")
# time calculation of for loop for 100000 elements
start_time_for_search=time.perf_counter_ns()
find(arr,val)
end_time_for_search=time.perf_counter_ns()
print("time taken by for loop is ",end_time_for_search-start_time_for_search,"nano sec")

class queue:
    def __init__(self,queue_list):
        self.queue_list=queue_list
    def push(self):
        push_element=int(input("enter element you want to add:").strip())
        return [push_element]+ self.queue_list
    def pop(self):
        return self.queue_list[1:]
    def peek(self):
        return self.queue_list[0]


queue_list=[1,3,4,68,93,23]
object1=queue(queue_list)
print("updated queue after adding element is:",object1.push())
print("updated queue after removing element is:",object1.pop())
print("first element of queue list is:",object1.peek())


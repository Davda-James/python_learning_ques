class stack:
    def __init__(self,stack_list):
        self.stack_list=stack_list
    # push element in stack
    def push(self):
        push_element=int(input("enter element to add in stack:"))
        return self.stack_list+[push_element]
    # pop item from stack
    def pop(self):
        return self.stack_list[:-1]
    # peek value in stack
    def peek(self):
        return self.stack_list[-1]
stack_list=[1,3,6,7,9,12]
object1=stack(stack_list)
print('updated list after adding new element:',object1.push())
print('updated list after popping last element:',object1.pop())
print('last element of stack is:',object1.peek())

class app_stack:
    def __init__(self,string):
        self.string=string
    def balanced(self):
        temp=[]
        for i in range(len(self.string)):
            if self.string[i] in ['{','[','(']:
                temp.append(self.string[i])
            elif self.string[i]=='}':
                try:
                    if temp[len(temp)-1]=='{':
                        temp.pop(len(temp)-1)
                    else:
                        print(f"{0}")
                        return 
                except ValueError as e:
                    print(f"{0}")
                    return 
                except IndexError as e:
                    print(f"{0}")
                    return 
            elif self.string[i]==']':
                try:
                    if temp[len(temp)-1]=='[':
                        temp.pop(len(temp)-1)
                    else:
                        print(f"{0}")
                        return 
                except ValueError as e:
                    print(f"{0}")
                    return
                except IndexError as e:
                    print(f"{0}")
                    return  
            elif self.string[i]==')':
                try:
                    if temp[len(temp)-1]=='(':
                        temp.pop(len(temp)-1)
                    else:
                        print(f"{0}")
                        return 
                except ValueError as e:
                    print(f"{0}")
                    return
                except IndexError as e:
                    print(f"{0}")
                    return 
        if len(temp)==0:
            print(f"{1}")
        else:
            print(f"{0}")

string=input("enter string to be analysed:").strip()
object1=app_stack(string)
object1.balanced()

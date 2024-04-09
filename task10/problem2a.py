class IC152:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def valid_roll_no(self):
        if self.roll_no[0]!='B' or self.roll_no[1]!='2' or self.roll_no[2]!='3':
            print("Invalid Input")
            exit()
    def valid_marks(self):
        if self.marks>100 or self.marks<1:
            print("Invalid Input")
            exit()
    def pass_fail(self):
        if self.marks>=33:
            print("pass")
        else:
            print("fail")
student1=IC152(input("enter name:").strip(),input("enter roll no:").strip(),int(input("enter marks:").strip()))
student1.valid_roll_no()
student1.valid_marks()
student1.pass_fail()


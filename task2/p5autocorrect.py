with open("c:/users/admin/desktop/assignment 2/inputWithErrors.txt","r") as f:
    lines=[line.rstrip() for line in f]
foutput=open("c:/users/admin/desktop/assignment 2/outputClean.txt","w")
list=[]
i=0
for line in lines:
    if line==line[0]:
        line[0]=line.replace("features","Features")
    if line==line[1]:
        line[1]=line[1]
    if line==line[2]:
        line[2]=line.replace(" .",".")
    if line==line[3]:
        list[3]=line.lower()
        list[3]=list[3].replace(" ,",",")
        list[3]=list[3].replace(" .",".")
    if line==line[4]:
        list[4]=line.lower()
        list[4]=list[4].replace(" .",".")
    if line==line[5]: 
        list[5]=line.replace("Glue","glue")
        list[5]=list[5].replace(" .",".")
    if line==line[6]:
        list[6]=line.replace("Everywhere","everywhere")
    if line==line[7]:
        line[7]=line.replace("S","s")
        line[7]=line[7].replace("C","c")
    if line==line[8]:
        list[8]=line.replace("You","you")
        list.append(line)
        i+=1
newline="".join(list)
foutput.close()

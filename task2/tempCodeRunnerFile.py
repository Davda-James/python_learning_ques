#slicing the words and phrases to create newone
s1="quick read"
s2="python"
list=s1.split()
list.append(s2)
print("new phrases are:")
print(list[0]+" " + list[1])
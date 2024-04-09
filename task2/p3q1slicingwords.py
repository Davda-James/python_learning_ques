#slicing the words and phrases to create newone
s1="quick read"
s2="python"
list=s1.split()
list.append(s2)
print("new phrases are:")
print(list[0]+" " + list[1])
print(list[0]+" " +list[2])
print(list[1]+" "+list[2])
#cases
letter=s2[0]
letter=letter.upper()
word1=letter + "ick"
letter2=s1[4]
letter2=letter2.upper()
word2=letter2 + "inder"
print(word1,"and",word2)
import sys
import os
def read_args():
    #checking whether the user has given input or not or has entered required no of arguments
    if len(sys.argv)!=2 and len(sys.argv)!=1:
        print("Please enter 1 file name as argument in terminal")
        exit()
    elif len(sys.argv)==1:
        #checking whether the user has given no input files
        print("Usage: python extraproblem.py [file name (Seperated by space)]")
        exit()
    return sys.argv[1]
f1=read_args()
if os.path.getsize(f1)==0:
    print("Sorry! File is empty")
    exit()
with open(f1,"rb") as f:
    text=f.read()
    text=str(text)
text=text.lower()
text=text[1:]
text=text.replace(',',"")
text=text.replace('.',"")
text=text.replace('(',"")
text=text.replace(')',"")
text=text.replace('"',"")
text=text.replace('\ ',"")
text=text.replace('/',"")
text=text.replace('-'," ")
text=text.replace("\n"," ") 
text=text.replace("'","")
text=text.replace('“',"")
text=text.replace('”',"")
text=text.replace("\\r\\n"," ")
text=text.replace("\r\n"," ")
text=text.replace("\xe2\x80\x9d","")
text=text.replace("\xe2\x80\x9c","")
textwords=text.split()
worddic=dict()
# calculating the words in list containing all words of text
for i in textwords:
    if i not in worddic.keys():
        worddic[i]=1
    else:
        worddic[i]=worddic[i]+1
# final list of words with frequency
wordfreq=[]
for keys,values in worddic.items():
    wordfreq.append({'word':keys,"frequency":values})
#sorting in descending order
wordfreq=sorted(wordfreq, key=lambda i: i['frequency'], reverse=True)
# code to write above dict to csv
import csv
with open('extraProblemOutput.csv', 'w',newline='') as csvop:
# creating dictionary writer object
    writerObj = csv.DictWriter(csvop, fieldnames =['word', 'frequency'])
# write fieldnames
    writerObj.writeheader()
    writerObj.writerows(wordfreq)

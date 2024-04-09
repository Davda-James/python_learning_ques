# imprting and print Data.csv file
import pandas as pd
#use pandas to read the CSV 
csvData=pd.read_csv('Data.csv',sep=',')
#convert dataframe into numpy array
csvDataNum=csvData.to_numpy()
#convert numpy array into a list of lists
data=csvDataNum.tolist()
print(data[3][4])





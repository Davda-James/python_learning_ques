import pandas as pd
import sys
df=pd.read_csv("data/Cars93.csv")
# please run the code of problems one by one commenting others
#PROBLEM 1(a)
dfmodel=df.loc[:,['Unnamed: 0','Model']]
dfmodel['Model']=dfmodel['Model'].sort_values().values
dfmodel.rename(columns={'Model':'Model Sorted'},inplace=True)
dfmodel.rename(columns={'Unnamed: 0':''},inplace=True)   
dfmodel.to_csv('problem1a.csv',index=False)



#PROBLEM 1(b)
details=df.groupby('Type')
for type,typedf in details:
    index=typedf['Price'].idxmax()
    print(typedf.loc[[index]])



#PROBLEM 1(c)
manname=sys.argv[1]
diffmodel=df.loc[:,['Manufacturer','Model']]
diffmodel=diffmodel[diffmodel['Manufacturer']==manname]
print(diffmodel['Model'])




#PROBLEM 1(d)
carcount=df.groupby('Manufacturer').size()
carcount=carcount.reset_index()
indexdf=pd.DataFrame({'Sr no.': [i for i in range(1,len(carcount)+1)]})
carcount.rename(columns={0:'count'},inplace=True)
carcount.insert(0,'',indexdf['Sr no.'])
carcount.to_csv("problem1d.csv",index=False)





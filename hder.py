import pandas as pd
df=pd.read_excel('sample1.xlsx')
df['UNITPRICE']=df['QUALITY']*df['UNITPRICE']
df.head()
print(df)
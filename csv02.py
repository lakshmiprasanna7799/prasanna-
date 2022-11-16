import pandas as pd
df=pd.read_excel('sample1.xlsx')
df['UNITPRICE']=df['QUALITY']*df['UNITPRICE']
df.head()
print(df)
df_customers=df.groupby('customerid').agg(orders=('InvoiceNo', 'nunique'),
            skus=('StockCodeCustomers','nunique'),quantity=('QUALITY','sum'),revenue=('LinePrice',sum)).rest_index()
df_customers.head()
print(df_customers)
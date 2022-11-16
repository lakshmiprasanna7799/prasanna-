import pandas as pd
data={'country':['belgium','india','brazil'],
      'capital':['brussesls','newdelhi','brasilia'],
      'population':[11190846,1302342424,32424352523]}
df=pd.DataFrame(data,columns=['country','capital','population'])
print(df)
import pandas as pd
data=[1.1,2.1,3.1]
df=pd.Series(data)
print("This Series is:\n",df)
print("This type is ",type(df))
data={'a':1,'b':2,'c':3}
df=pd.Series(data)
print(df)

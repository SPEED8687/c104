import pandas as pd
df=pd.read_csv('data.csv')
weight=df['Weight(Pounds)'].tolist()
sum=0
for w in weight:
    sum=sum+float(w)

mean=sum/len(weight)
print(mean)
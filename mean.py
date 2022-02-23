import pandas as pd
df=pd.read_csv('data.csv')
height=df['Height(Inches)'].tolist()
sum=0
for h in height:
    sum=sum+float(h)

mean=sum/len(height)
print(mean)
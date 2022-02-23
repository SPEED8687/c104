import pandas as pd
df=pd.read_csv('data.csv')
height=df['Height(Inches)'].tolist()
l=len(height)
if l%2==0:
    median1=float(height[l//2])
    median2=float(height[l//2-1])
    median=(median1+median2)/2
    print(median)
else:
    median=float(height[l//2])
    print(median)
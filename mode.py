import statistics as st
import pandas as pd
df=pd.read_csv('data.csv')
height=df['Height(Inches)'].tolist()
mode=st.mode(height)
print(mode)
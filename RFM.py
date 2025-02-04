import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('C:/Users/DELL/Documents/transaction_data.csv')
df=pd.DataFrame(data)
print(df.head())
print(df.shape)
df.info()
df=df.dropna(subset=["UserId"])
print(df.duplicated().any())
df.drop_duplicates(inplace=True)
print(df.shape)
print(df.describe())
df["ItemDescription"]=df["ItemDescription"].str.strip()
df=df.rename(columns={"NumberOfItemsPurchased":"Quantity"})
print(df.columns)
df=df[df['UserId']>0]
print(df.describe())
df=df[df['Quantity']>0]
df=df[df['ItemCode']>0]
print(df.describe())
print(df.duplicated().any())
df.drop_duplicates(inplace=True)
print(df.duplicated().any())
print(df.shape)
print(df.isnull().sum())
print(df.nunique())
filtered_data=df[["Country","UserId"]].drop_duplicates()
print(filtered_data.head())
print(filtered_data.shape)
filtered_data.Country.value_counts()[:10].plot(kind='bar')
plt.show()
uk_data=df[df["Country"]=="United Kingdom"]
print(uk_data.head())
print(uk_data.nunique())
uk_data=uk_data[["UserId","TransactionId","TransactionTime","Quantity","CostPerItem"]]
uk_data["TotalPrice"]=uk_data["Quantity"]*uk_data["CostPerItem"]
uk_data["TransactionTime"]=pd.to_datetime(uk_data['TransactionTime'],errors="coerce")
print(uk_data.head())
present_time=datetime.now()
uk_data=uk_data[uk_data["TransactionTime"]<=present_time]
print(present_time)
rfm=uk_data.groupby("UserId").agg({"TransactionTime":lambda date:(present_time-date.max()).days,
"TransactionId":lambda num: len(num),"TotalPrice":lambda price:price.sum()})
rfm.columns=["Recency","Frequency","Monetary"]
rfm.info()
rfm["r_quartile"]=pd.qcut(rfm["Recency"],4,["1","2","3","4"])
rfm["f_quartile"]=pd.qcut(rfm["Frequency"],4,["4","3","2","1"])
rfm["m_quartile"]=pd.qcut(rfm["Monetary"],4,["4","3","2","1"])
print(rfm.head())
rfm["RFM_Score"]=rfm.r_quartile.astype(str)+rfm.f_quartile.astype(str)+rfm.m_quartile.astype(str)
print(rfm.head())
print(rfm[rfm["RFM_Score"]=="111"].sort_values("Monetary",ascending=False).head())
rfm["RFM_Score"]=rfm["RFM_Score"].astype(int)
segment_labels=["High-Value","Mid-Value","Low-Value"]
rfm["Value_Segment"]=pd.qcut(rfm["RFM_Score"],q=3,labels=segment_labels)
print(rfm.head())
plt.figure(figsize=(10,6))
ax=rfm.Value_Segment.value_counts().sort_values().plot(kind='bar',color=sns.color_palette("pastel"))
ax.set_title('Value Segment Distribution',fontsize=16)
ax.set_xlabel('Value Segment',fontsize=14)
ax.set_ylabel('Count',fontsize=14)
ax.grid(axis='y',linestyle='--',alpha=0.7)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x()+p.get_width()/2.,p.get_height()),
                ha='center',va='bottom',fontsize=12)
plt.show()
Top_countries = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
Top_countries.plot(kind='bar', color=sns.color_palette('Set3'), figsize=(10,6))
plt.title('Top 10 Countries by Total Quantity Sold', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Total Quantity Sold', fontsize=14)
plt.grid(axis='y', linestyle='-', alpha=0.7)
plt.show()

uk_data['TransactionWeek'] = uk_data['TransactionTime'].dt.to_period('W').astype(str)
Weekly_transactions = uk_data.groupby('TransactionWeek')['TransactionId'].nunique()
Weekly_transactions.plot(figsize=(12,6), color='green', marker='o', linestyle='-', linewidth=2)
plt.title('Weekly Transactions Over Time', fontsize=16)
plt.xlabel('Week', fontsize=14)
plt.ylabel('Number of Transactions', fontsize=14)
plt.grid(axis='both', linestyle='-', alpha=0.7)
plt.show()

Country_quantity_pivot = df.pivot_table(index='Country', values='Quantity', aggfunc='sum').sort_values(by='Quantity', ascending=False).head(10)
sns.heatmap(Country_quantity_pivot, annot=True, fmt='.0f', cmap='coolwarm', cbar=False, linewidths=1)
plt.title('Top 10 Countries by Quantity Sold', fontsize=16)
plt.xlabel('Quantity')
plt.ylabel('Country')
plt.show()


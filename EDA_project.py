import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import os

print("understanding dataset")

file_name = 'sales_data.csv'
if not os.path.exists(file_name):
     print("Error:{file_name}is not found")
     exit()
df = pd.read_csv(file_name)
print("successfully loaded")
print (f"shape of the dataset:rows:{df.shape[0]},columns:{df.shape[1]}")
print(df.head())
print(df.tail())
print(df .describe())

print("Handling Outliers and Missing Values in Age")
mean_age_before = df['Age'].mean()
print(f"Mean Age before handling outliers/missing values: {mean_age_before:.2f}")

# Identify outliers (Age > 100) and set to NaN
age_outliers = df['Age'] > 100
print(f"Detected {age_outliers.sum()} outliers in Age (values > 100)")
print(df[age_outliers])
df.loc[age_outliers, 'Age'] = None

median_age=df['Age'].median()
df['Age']= df['Age'].fillna(median_age)
print(f"Median Age (after handling outliers): {median_age}")
mean_age_after = df['Age'].mean()
print(f"Mean Age after handling outliers/missing values: {mean_age_after:.2f}")

median_spending=df['Spending'].median()
df['Spending']= df['Spending'].fillna(median_spending)
print(f"Median Spending: {median_spending}")

print("Missing values after imputation:")
print(df.isnull().sum())

print("\n--- Final Mean Values ---")
print(df[['Age', 'Spending', 'Visits_Per_Month']].mean())

plt.figure(figsize=(7,4))
df['Spending'].hist(bins=10,color='#6366F1',edgecolor='#1E1B4B')
plt.title('Distribution of spending')
plt.xlabel('spending Amount')
plt.ylabel('Number of customers')
plt.show()


correlation = df.corr(numeric_only=True)
print(correlation)

print("plotting Correlation Heatmap")
plt.figure(figsize=(7,4))
sns.heatmap(correlation,annot=True,cmap='mako',fmt=".2f")
plt.title("correlation Heatmap")
plt.show()
plt.figure(figsize=(7,4))
sns.boxplot(x=df['Age'],color='lightgreen')
plt.title("Boxplot of customer age")
plt.xlabel('Age')
plt.show()
print("Find the outliers in age")
outlers=df[['Age']>100]
print("Found outlers(s):")
print(outlers)

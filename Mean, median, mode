#Import CSV file
import pandas as pd 
import csv
with open('student_performance.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
df = pd.read_csv('student_performance.csv')

#Medians
df_median = df.drop(columns='grade')
df_median.median()

#Means
df_mean = df.drop(columns='grade')
df_mean.mean()

#Modes
df_mode = df.drop(columns={'student_id', 'grade'})
df_mode.mode()

#Unique Values
unique_values = df['grade'].nunique()

#Print
print("Medians")
print(df_median.median().to_string(dtype=False))

#Line Break
print("" \
"")

print("Means")
print(df_mean.mean().to_string(dtype=False))

#Line Break
print("" \
"")

print("Modes")
print(df_mode.mode().to_string(index=False))

#Line Break
print("" \
"")

print("Unique Values")
print("Grade   ", unique_values)


"""
RECORD CHECK  -  my version
===========================

Name  : SHANICE TSITSI ANGEL MURWIRA
Lane  :  AI 
Date  : 4/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
"""Creating a csv file,adding new columns ,manipulating the data and creating a bar chart """
import pandas as pd

file = pd.DataFrame({
    "dataset" : ["srv-01","srv-02","srv-03","srv-04","srv-05","srv-06"],
    "rows_loaded" : [45,56,89,101,95,120],
    "rows_expected" : [100,100,100,100,100,100]
})

file.to_csv("survey_file.csv",index = False)
# I created my DataFrame and saved it to a csv file so that I can use it in my template

df = pd.read_csv("survey_file.csv")  


df["percent"] = (df["rows_loaded"]/ df["rows_expected"] * 100)

df["status"] = df["percent"].apply(
    lambda p : "OVER LIMIT" if p >= 100 else "WARNING" if p > 90 else "OK"
)
#I created two new columns(percent and status) and used .apply() and lambda to be able to use
# a function inside my status column.

filtered = df[~ (df["status"] == "OK")]
grouped = filtered.groupby("status")
print(grouped.value_counts())
#I used  ~ to be able to get rows that are not "OK" and used groupby() to group my rows as well
# as value_counts() to get the number of values I have. 

df.to_csv("new_survey_file.csv",index = False)
#I saved my new dataframe with added columns to a csv file without the index.

import matplotlib.pyplot as plt
df["status"].value_counts().plot(kind="bar",title= "Counts per Status")
plt.savefig("Counts per Status")
plt.tight_layout
plt.show
# I imported matplotlib so that I will be able to create a bar chart with the counts per status
# and save the image of the bar chart.




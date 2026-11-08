"""
RECORD CHECK  -  my version
===========================

Name  :SHANICE TSITSI ANGEL MURWIRA
Lane  :  AI 
Date  :6/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def parse_line (raw_records): 
    """Creating a function that cleans up a messy record of lines"""
    new_record = raw_records.strip()

    surveyname_part,rest = new_record.split(",",1)
    surveyname = surveyname_part.strip().lower()


    new_rest = {}
    for r in rest.split(","):
        key,value = r.split("=")
        new_rest[key.strip().lower()] = float(value.strip())


    result = {"Surveyname":surveyname , **new_rest}
    return result 

def status_of(rating,age,warning_at=90):
    """It returns Over LIMIT ,WARNING or OK depending on our value """
    percent = rating/age *100
    
    if  percent >=warning_at:
        return "FLAGGED"
    else:
        return "OK"

#I have created two functions that will clean our records as well check the status of our values as well.

with open("messy_records.txt","w") as f:
    f.write("survey_2020, rating= 40,age=80\n")
    f.write(" survey_2021, rating= 45,age=50\n")
    f.write(" Survey_2022, rating= 20,age=80 \n")
    f.write("survey_2023, Rating= 54,age=60\n")
    f.write(" survey_2024, rating= 20,Age=40\n")
   
#I have saved my survey data to a file so that I can load the lines from the file.

with open("messy_records.txt") as f:
    record = 0
    for raw_record in f :
        records = parse_line(raw_record)
        record +=1
        print(parse_line(raw_record), status_of(records["rating"], records["age"]))
   

#the loop will go through the whole file and apply the parse line and status of functions.        

print("The number of records is :",record,f",the flagged records are : {record - len(records)}")
#This line will help us see how many records are in our file because we used a variable 
#that counts the number of files in our loop and we can calculate the flagged by subtracting.



"""
RECORD CHECK  -  my version
===========================

Name  :SHANICE TSITSI ANGEL MURWIRA
Lane  :  AI 
Date  :2/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
"""Creating a program that uses a decisions to be able to output status of the users input in a formatted  report
"""
while True :
    data_set_name = input("please enter  dataset name :")
    if data_set_name == "quit" :
        break   
    rows_loaded = float(input("please enter rows loaded :"))   
    rows_expected = float(input("please enter rows expected :"))    
#we use a while True loop to be able to print as many reports until the user types in quit then
#the loop will immediately stop.

    difference = rows_expected  - rows_loaded 
    percent = (rows_loaded / rows_expected) * 100

    if percent >= 100 :
         status = "OVER LIMIT"
    elif percent >= 90 :
        status = "WARNING"
    else :
        status = "OK"
  
   
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {data_set_name}")
    print("=" * 34)
    print(f"Used            : {rows_loaded:>10.2f}")
    print(f"Total           : {rows_expected:>10.2f} ")
    print(f"Free            : {difference:>10.2f}")
    print(f"Percent         : {percent:>10.2f} %  ")
    print(f"status          : {status:>10}" )
    print("=" * 34)

    over_limit = 0
    if status == "OVER LIMIT":
            over_limit +=1
    #this is is used to be able to count the number of records that where over limit and add it to the
    #variable over limit.
print("Records that were over limit are :",over_limit)

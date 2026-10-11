"""
RECORD CHECK  -  my version
===========================

Name  :SHANICE MURWIRA
Lane  :  AI 
Date  :9/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check(value,limit) :
    """It is used to check the percentage and difference of values entered"""
    difference = limit - value
    percent = (value/limit) * 100
    return difference,percent

def status_of(percent,warning_at =90) :
    """Used to check whether the percentage is within the limit or not"""
    if percent >= 100 :
        return "OVER LIMIT"
    elif percent >= warning_at :
        return "WARNING"
    else :
        return "OK"


data_set_name = input("please enter  dataset name :")     
rows_loaded = float(input("please enter rows loaded :"))   
rows_expected = float(input("please enter rows expected :"))


difference,percent = check(rows_loaded,rows_expected)       
status = status_of(percent)         

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


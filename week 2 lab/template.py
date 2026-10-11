"""
RECORD CHECK  -  my version
===========================

Name  :SHANICE MURWIRA
Lane  :  AI 
Date  :2/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

data_set_name = input("please enter  dataset name :")     
rows_loaded = float(input("please enter rows loaded :"))   
rows_expected = float(input("please enter rows expected :"))    


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


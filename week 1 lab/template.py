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

data_set_name = input("Enter dataset name :")      
rows_loaded= float(input("Please enter rows loaded :"))    
rows_expected = float(input("Please enter rows expected:"))


difference = rows_expected - rows_loaded
percent = (rows_loaded / rows_expected) * 100
percent_free = (difference /rows_expected) * 100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {data_set_name}")
print("=" * 34)
print(f"Used            : {rows_loaded:>10.2f}")
print(f"Total           : {rows_expected:>10.2f} ")
print(f"Free            : {difference:>+10.2f}")
print(f"Percent         : {percent:>10.2f} %  ")
print(f"Percent of free : {percent_free:>10.2f} %")# calculate the percentage of the difference so that 
print("=" * 34) #  the user knows how much they have left and if its a decrease or increase



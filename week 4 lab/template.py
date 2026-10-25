"""
RECORD CHECK  -  my version
===========================

Name  :SHANICE TSITSI ANGEL MURWIRA
Lane  :  AI 
Date  : 16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value,limit,warning_at=90) :
    """Used to check the difference,percent and status of the users inputs"""
    difference = value -limit 
    percent = (value/limit) * 100

    if percent >= 100 :
        status = "OVER LIMIT"
    elif percent >= warning_at :
        status = "WARNING"
    else :
        status = "OK"
    return difference,percent,status



def print_report(record_id, value, limit, difference, percent, status):
    """Used to print the users input in a formatted report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record_id}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Limit       : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()



def load_records(path) :
    """It reads label,value,limit from a file and returns the lists of dicts"""
    records = []
    with open(path) as f :
        for line in f :
            label,value,limit = line.strip().split(",")
            records.append({
                "label" : label,
                "value" : float(value),
                "limit" : float(limit),
            })
    return records

with open("results.txt" ,"w") as f:
    f.write("SRV-001,12,100\n")
    f.write("SRV-002,90,100\n")
    f.write("SRV-003,120,100\n")

records = load_records("results.txt")


for record in records :
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                     difference, percent, status)






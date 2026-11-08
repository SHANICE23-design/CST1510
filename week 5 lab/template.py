"""
RECORD CHECK  -  my version
===========================

Name  :SHANICE TSITSI ANGEL MURWIRA
Lane  :  AI 
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record():
    """This class goes through each record in a file and gives us the status,value,limit and label"""
    def __init__ (self,label,value,limit):
        self.label = label
        self.value = value
        self.limit = limit 

    def percent(self):
        """Calculate the percentage of the value using the limit"""
        return (self.value /self.limit) * 100

    def status(self):
        """Gives the status of the label using the percent and tells the user if it is over limit,warning or ok"""
        p = self.percent()
        if p >= 100 :
            return ("OVER LIMIT")
        elif p >= 90:
            return ("WARNING")
        else :
            return ("OK")
#I created a class Record that contains two methods that I can use with my objects to be able to
#calculate the percent and give the status of the objects.
        
def load_records(path) :
    """Reads label,value and limit from a file and returns list of objects"""
    records = []   
    with open (path) as f:
        for line in f :
            label ,value ,limit = line.strip().split(",")
            records.append(Record(label,float(value),float(limit)))
    return records

with open("records.txt","w") as f:
    f.write("R-001,87,100\n")
    f.write("R-002,96,100\n")
    f.write("R-003,120,100\n")
#I loaded my lines to a file so that every line will be created into an object which i can then 
#use to print my report below.
records = load_records("records.txt")

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Used  : {record.value :>10.2f}")
    print(f"Total : {record.limit:>10.2f}")
    print(f"Status: {record.status():>10}")
    print("=" * 34)


over_limit_count = 0
for record in records :
    if record.status() =="OVER LIMIT":
        over_limit_count +=1 

# I used a loop to be able to count how many were over limit so that I can print below how many 
#are over limit.

print(f"{over_limit_count} of {len(records)} were over limit")


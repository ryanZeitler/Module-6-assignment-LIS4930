import sys
from datetime import datetime, timedelta
    
dt = datetime.now()

time_string = dt.strftime("%X")


for line in sys.stdin:          #press tab after input, then type next input
    data = line.strip().split("\t")
    if len(data) == 6:
        _date, _time, store, item, cost, payment = data
        print ("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(dt,time_string,store,item,cost,payment))
        break     




dt = dt - timedelta(seconds=60)     #subtracts 60 from datetime object
print(dt)
dt = dt.replace(year=dt.year + 2)       #adds 2 years to datetime objectg (timedelta does not have years)
print(dt)


d = timedelta(days=100,hours=10,minutes=13)         #makes time delta object with 100 days, 10 hours, and 13 minutes
print(d)




def FTintoTime(feet,inches):                        #function to take feet and inches and put them intop datetime object
    
    datetime_object = datetime.now()           #makes datetime object
    
    print(datetime_object)      
    
    sum_inches = feet * 12 + inches     #conversts feet into inches and adds them to inchest for easier conversion 
    
    m_in_seconds = sum_inches * 0.0254          #multiple the sum of inches to conversion for meters(0.9254)
    
    datetime_object = datetime_object + timedelta(seconds = m_in_seconds)   #adds conversted amount of meters per second to seconds of datetime object
    
    return datetime_object

conversion= FTintoTime(5,6)
print (conversion)

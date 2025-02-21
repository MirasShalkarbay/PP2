#Ex 1
import datetime

def days():
    x = datetime.datetime.now()
    return x.day - 5
print(days())   

#Ex 2
import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(today)
print(yesterday)
print(tomorrow)

#Ex 3
import datetime

current_datetime = datetime.datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime without microseconds:", current_datetime_without_microseconds)

#Ex 4
import datetime

def diff_on_seconds(date1, date2):
    difference = date1 - date2
    return difference.total_seconds()

date1 = datetime.datetime(2024, 2, 21, 12, 50, 15)  
date2 = datetime.datetime(2024, 2, 22, 12, 0, 10)  

difference_btwn_seconds = diff_on_seconds(date1, date2)
print(difference_btwn_seconds)



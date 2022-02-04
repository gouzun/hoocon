from datetime import datetime,date
from calendar import monthrange

#to validate d29,d30,d31 whethere exist on current month


todays_date = date.today()  
currentyear = todays_date.year  
currentmonth = todays_date.month  
currentday = todays_date.day 
# fetching the current year, month and day of today
#currentmonth = 2 
print("Current year:", str(currentyear))
print("Current month:", currentmonth)

currentmonth = 4
currentyear = 2022                  
currentmonthtotaldays = monthrange(currentyear, currentmonth)[1]
print("currentmonthtotaldays= " + str(currentmonthtotaldays))
if 31 > currentmonthtotaldays:
    print("31=0")
if 30 > currentmonthtotaldays:
    print("30=0")
if 29 > currentmonthtotaldays:
    print("29=0")

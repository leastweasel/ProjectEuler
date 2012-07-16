DaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

startingDayOfWeek = 2   # Tuesday
dayInCentury = 0    # January 1st, 1901

daysInCentury = 36525
month = 0
year = 1901

monthsStartingOnSunday = 0

def isLeapYear(year):
    leapYear = False
    
    if year % 100 == 0:
        leapYear = year % 400 == 0
    else:
        leapYear = year % 4 == 0
    
    return leapYear
    
while dayInCentury < daysInCentury:
    if month == 2 and isLeapYear(year):
        dayInCentury += 1

    if dayInCentury % 7 == 5:
        monthsStartingOnSunday += 1
        print "Year:",str(year)," Month:", str(month + 1)," Day:", dayInCentury

    dayInCentury += DaysInMonth[month];
    month += 1
    
    if month == 12:
        month = 0
        year += 1
        
print monthsStartingOnSunday
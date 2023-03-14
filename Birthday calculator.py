def day_difference(given_date:int,future_date:int)->int:
    """Return the day differences between day1(given_date) and day2(future_date)
    Example: 
    day_difference(100,120)
    20"""
    return abs(future_date - given_date)
given_date,future_date = [int(x) for x in input("Enter Given date; Future date:").split(";")]
x = day_difference(given_date, future_date)
#print(day_difference(given_date,future_date))

def weekday_from_today(given_day:int,x:int) -> int:
    """Return the weekday of a day in the future, given a day in the week
    Example:
    weekday_from_today(7,1)
    1
    weekday_from_today(1,8)
    2"""
    return ((given_day + x - 1)%7 + 1)
given_day = int(input("Enter given day:"))
#print (weekday_from_today(given_day,day_difference(given_date,future_date)))

def get_date (given_date:int, given_day:int, future_date:int)->int:
    """Return the date of a day in future, given a day of the year and its corresponding date
    Example:
    get_date(4,3,10)
    2"""
    return (weekday_from_today(given_day, x))
print (get_date(given_date, given_day, future_date))
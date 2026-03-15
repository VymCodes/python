
import calendar
from datetime import date , time , datetime


x = datetime.now()
print(x)


year = 2026
month = 3
print(calendar.month(year, month))

today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and time is", now)

print("\nDate components", today.year, today.month, today.day)
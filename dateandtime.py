
from datetime import *


#current date and time
now = date.time.now()
print(f"Current date and time: {now}")

#current date
today = datetime.now()
print(f"Current date: {today}")

#current date and time
current_time = now.time()
print(f"Current time: {current_time}")

#formatting date and time
formatted_date_time = now.strftime("%d-%m-%Y %H:%M:%S")
print(f"Current formatted date and time: {formatted_date_time}")


#formatting date and time
formatted_date_time = now.strftime("%I:%M:%S %p")
print(f"Current time in 12 hr clock: {formatted_date_time}")

#finding diff between 2 dates
date1 = datetime(2026 , 1, 1)
date2 = datetime(2026, 1, 1)

diff = date1 - date2
print(f"Difference in dates : {diff}")

"""
Meaning of Each Part:
----------------------
%d → Day (01 to 31)
%m → Month (01 to 12)
%Y → Full Year (2026)

%H → Hour (00 to 23) → 24-hour format
%M → Minutes (00 to 59)
%S → Seconds (00 to 59)

%I → Hour in 12 hr clock
%p → for am or pm
"""


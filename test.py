import datetime
import json

start_time = '15:00'
end_time = '18:00'
slot_time = 20

# Start date from today to next 5 day
start_date = datetime.datetime.now().date()
end_date = datetime.datetime.now().date()

days = []
date = start_date
while date <= end_date:
    hours = []
    time = datetime.datetime.strptime(start_time, '%H:%M')
    end = datetime.datetime.strptime(end_time, '%H:%M')
    while time <= end:
        hours.append(time.strftime("%H:%M"))
        time += datetime.timedelta(minutes=slot_time)
    date += datetime.timedelta(days=1)
    days.append(hours)

slots = {}
for hours in days:
	av = {}
	for h in hours:
		av[h] = False
	slots[datetime.date.today().strftime("%d-%m-%y")] = av

js = json.dumps(slots)
print(js)
print(type(js))
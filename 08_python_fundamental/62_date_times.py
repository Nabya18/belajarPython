import datetime

date = datetime.date(2020, 12, 25)
today = datetime.date.today()

time = datetime.time(12, 30, 45)
now = datetime.datetime.now() # base on the operation system time

now = now.strftime("%d/%m/%Y %H:%M:%S")

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime > current_datetime:
    print("The target date has not passed")
else:
    print("The target date has passed")

print(date)
print(today)
print(time)
print(now)


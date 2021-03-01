import datetime

h, m = map(int, input().split())
time = datetime.datetime.strptime(f'{h}:{m}', '%H:%M')
time -= datetime.timedelta(minutes=45)
print(time.hour, time.minute)

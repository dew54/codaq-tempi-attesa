
import datetime as dt






arrivalDate = dt.datetime.strptime('2022-03-07', '%Y-%m-%d')

waitTime = "0b'00:23'"

waitingTime = dt.datetime.strptime(str(waitTime)[3:8], '%H:%M')

print(waitingTime)
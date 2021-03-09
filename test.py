from datetime import datetime
datetime1 = datetime.strptime('07/11/2019 14:45', '%m/%d/%Y %H:%M')
datetime2 = datetime.strptime('08/11/2019 17:45', '%m/%d/%Y %H:%M')

timediff = datetime1 - datetime2
 
#convert to seconds
seconds = timediff.total_seconds()
 
print(seconds)
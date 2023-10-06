import datetime
year,month,day = map(int,input().split(" "))
yuandan = datetime.datetime(year,1,1)
now = datetime.datetime(year,month,day)
print((now-yuandan).days + 1)
#python标准库datetime

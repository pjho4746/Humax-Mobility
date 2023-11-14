from datetime import date

# 오늘 날짜
now = date.today()

# st_date end_date 20231101 20231130
# 2023-11-23, 요일, 날짜
# str  strftime

print(now.strftime("%m-%d-%y"))
print(now.strftime("%d-%b-%Y is a %A"))
print(now.strftime("%d day of %B"))

# 지금까지 살아온 날짜
mybirth = date(2000, 5, 27)
myage = now - mybirth
print(myage.days)

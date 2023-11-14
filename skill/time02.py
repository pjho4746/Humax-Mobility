from datetime import date

# now = date.today()

# d = date(2023, 11, 14)
# print(d.replace(2024, 10, 10))

# 요일 확인 weekday() -> 0(일요일)~6, isoweekday-> 1~7
# weekday = date(2023, 11, 14).weekday()
weekday = date(2023, 11, 13).isoweekday()
weekday2 = date(2023, 11, 15).isoweekday()
# print(f"weekday : {weekday}")
# print(f"isoweekday : {weekday2}")

calc_weekday = weekday2 - weekday
print(calc_weekday)

# 상품 이벤트의 만기일까지 남은 날짜를 작성해보자
# 23년 12월 31일

expiration_date = date(2023, 12, 31)
today = date.today()

days_remaining = (expiration_date - today).days

print(f"오늘로부터 상품 이벤트의 만기일까지 남은 날짜: {days_remaining}일")
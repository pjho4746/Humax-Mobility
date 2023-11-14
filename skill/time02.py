from datetime import date

# now = date.today()

# d = date(2023, 11, 14)
# print(d.replace(2024, 10, 10))

# 요일 확인 weekday() -> 0(일요일)~6, isoweekday-> 1~7
weekday = date(2023, 11, 14).weekday()
weekday2 = date(2023, 11, 14).isoweekday()
print(f"weekday : {weekday}")
print(f"isoweekday : {weekday2}")
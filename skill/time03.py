# 주말에만 작업이 되어야 하는 메소드

from datetime import date

# 주말 호출 메서드
def is_weekend():
    today = date.today()
    print(today.strftime("%m-%d-%y")) 
    # return today.isweekday in [5, 6]
    return today.isoweekday() in [6, 7]

def perform_weekend_task():
    if is_weekend():
        print("주말에만 작업을 수행함")
    else:
        print("주중에는 작업을 수행하지 않음")

perform_weekend_task()

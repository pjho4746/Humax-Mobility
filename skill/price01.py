# 숫자 계산 시 자료형

int_x = 10
float_y = 2.5
calc_z = int_x/float_y

print(type(int_x))
print(type(float_y))
print(type(calc_z))

print(isinstance(calc_z, int))
print(isinstance(calc_z, float))


# 적금 계산
# 1년 만기 '단리'적금에 매달 100만원
# 연 이자는 5%

# 세전 이자 (각각 출력)
# 세후 이자 (각각 출력)

# 월 적금 납입액 float
# 이자율도 float
# 기간 int

# 100만 원 5% -> 세전 5만원
# 100만원 5% 11개월 + ... + 100만원 5% 1개월

dep = 1000000.0
rate = 5.0       
period = 12 

def installment_saving_calc():
    rate_result = rate / 100  # 연 이자율
    pretax_interest = dep * rate_result * period  # 세전 이자
    aftertax_interest = pretax_interest * 0.846  # 세후 이자 (15.4% 세금 공제)

    print("세전 이자:", pretax_interest)
    print("세후 이자:", aftertax_interest)

installment_saving_calc()

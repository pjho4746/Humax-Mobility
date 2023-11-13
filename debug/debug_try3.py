# 이런 식의 소스 코드가 1000줄
# 정확히 어떤 부분에서 문제가 있는지 모를 때 어떻게 해당 부분을 찾을까?
# 일일이 breakpoint()를 찍거나, print()를 100줄 단위로 작성 (범위를 점점 좁히기)
# print(f'where is my error!!! {cnt}')
# cnt += 1

import pdb

def calc_sum(x, y):
    pdb.set_trace()  # breakpoint()
    result = x + y
    return result

number1 = int(input("input number1: "))
number2 = int(input("input number2: "))

result = calc_sum(number1, number2)

print(f"{number1} 더하기 {number2}는 {result}입니다")

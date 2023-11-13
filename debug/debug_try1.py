import pdb

def calc_sum(x, y):
    pdb.set_trace()  # breakpoint()
    result = x + y
    return result

number1 = int(input("input number1: "))
number2 = int(input("input number2: "))

result = calc_sum(number1, number2)

print(f"{number1} 더하기 {number2}는 {result}입니다")

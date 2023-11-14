# 티셔츠 1장 만원 (1장 구매 할인 X)
# 추가 구매 시마다 장당 10% 추가 할인

# 최대 할인 50%

# print 할인률
# print 총 가격

# 함수(가격, 수량)

def cal_discount_and_total_price(price, quantity):
    base_price = price * quantity  # 기본 가격 계산

    if quantity > 1:
        discount_rate = min(0.5, (quantity-1) * 0.1)  # 최대 50% 할인, 장당 10% 추가 할인
        discounted_price = base_price - (base_price * discount_rate)
        print(f"할인율: {discount_rate * 100}%")
        print(f"총 가격: {discounted_price}원")
    else:
        print("할인없음")
        print(f"총 가격: {base_price}원")

tshirt_price = 10000
tshirt_quantity = int(input("티셔츠 개수를 입력하세요: "))
cal_discount_and_total_price(tshirt_price, tshirt_quantity)



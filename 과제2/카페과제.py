#2022111354 정보보호학과 한아림

while True:
    order = input("무슨 커피를 선택하시겠습니까? : ")
    size = input("어떤 사이즈를 원하십니까? : ")

    price = 0

    if order == 'Americano':
        price = 3500
    elif order == 'Cafe Latte':
        price = 4500
    elif order == 'Cafe mocha':
        price = 4000
    else:
        price = 5000

    if size == 'grande':
        price += 1000
    elif size == 'regular':
        price += 500
    else:
        price +=0
    

    print(f"총 금액은 {price}원입니다. ")

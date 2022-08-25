#한아림 정보보호학과 2022111354

def round(a,b):
    return a*2 + b*2
def area(a, b):
    return a*b

print("<계산을 시작합니다!>")

while True:
    menu = int(input("1.넓이 2.둘레 3.종료:   "))
    if(menu<=2):
        weight=int(input("가로는 얼마입니까?: "))
        hight = int(input("세로는 얼마입니까: "))
    if(menu==1):
        result=area(weight,hight)
        print("넓이: %d"%result)
    elif(menu==2):
        result=round(weight, hight)
        print("둘레: %d"%result)
    elif(menu==3):
        break
    else:
        print("올바른 수를 입력하라.")
        

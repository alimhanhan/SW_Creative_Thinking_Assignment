def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("***계산기***")

while True:
    menu = int(input("1.덧셈 2.뺄셈 3. 곱셈 4. 나눗셈 5.종료:   "))
    if(menu<=5):
        numberA=int(input("숫자를 입력하세요: "))
        numberB=int(input("숫자를 입력하세요: "))
    if(menu==1):
        result=sum(numberA,numberB)
        print("결과: %d"%result)
    elif(menu==2):
        result=sub(numberA,numberB)
        print("결과: %d"%result)
    elif(menu==3):
        result=mul(numberA,numberB)
        print("결과: %d"%result)
    elif(menu==4):
        result=div(numberA,numberB)
        print("결과: %d"%result)
    elif(menu==5):
        break
    else:
        print("올바른 수를 입력하세요.")
    
#한아림 정보보호학과 2022111354

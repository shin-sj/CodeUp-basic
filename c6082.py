n = int(input())

for i in range(1, n+1) :
    if i%10==3 or i%10==6 or i%10==9 :
        print("X", end=' ')    #출력 후 공백문자(빈칸, ' ')로 끝냄
    else :
        print(i, end=' ')
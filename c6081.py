n = int(input(), 16)    #16진수로 입력 
for i in range(1, 16) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

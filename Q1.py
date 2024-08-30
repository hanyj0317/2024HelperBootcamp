error = 0

while (error != 3):
    n = input()
    isneg = False
    
    if n[0] == '-':
        n = n[1:]
        isneg = True
        
    if (n.isdigit() != True):
        print('숫자만 입력하시오')
        error += 1
        if error == 3:
            print("3회 이상 잘못 입력하셨습니다")
            break
        
    elif len(n) > 20:
        print('20자리 이내로 입력하시오')
        error += 1
        if error == 3:
            print("3회 이상 잘못 입력하셨습니다")
            break
    else :
        lst = []
        for i in n:
            lst.append(i)
        lst.reverse()
        cnt = 0
        result = []

        for j in lst:
            cnt += 1
            result.append(j)
            if cnt % 3 == 0:
                result.append(',')
                cnt = 0
            
        result.reverse()
        if result[0] == ',':
            result.pop(0) 
        
        if isneg == True:
            print('-', end="")
        
        print(''.join(result))


##def diffsum(a,b,c):
##    sum1=a+b+c
##    sum2=a**2 + b**2 + c**2
##    diff=abs(sum1-sum2) 
##
##    #retrn diff
##
##    rv=str(sum1) + '와 ' + str(sum2) + '의 차는 '+ str(diff)
##    return rv
##
##a,b,c=map(int,input('숫자 3개 입력:').split())
##print (diffsum(a,b,c))

def diffsum(a,b,c):
    global m
    sum1=a+b+c
    sum2=a**2 + b**2 + c**2
    diff=abs(sum1-sum2) 
    if diff > m:
        m=diff
    #retrn diff

    rv=str(sum1) + '와 ' + str(sum2) + '의 차는 '+ str(diff)
    return rv

m=0
print('m 값 :',m)
a,b,c=map(int,input('숫자 3개 입력:').split())
print (diffsum(a,b,c))
print('m 값:',m)

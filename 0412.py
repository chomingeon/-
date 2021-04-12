##a=123456##a=123456
##b=7890
##print('{:10,}'.format(a))
##print('+{:>9,}'.format(b))
##print('-----------')
##print('{:>10,}'.format(a+b))

##a=123456
##b=7890
##print('{:10,}'.format(a))
##print('-{:>9,}'.format(b))
##print('-----------')
##print('{:>10,}'.format(a-b))

def numchk(a):
    if a%2 == 1:
        print("홀수")
    else:
        print("짝수")
a=int(input("숫자입력:"))
numchk(a)

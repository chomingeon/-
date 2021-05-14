##a = int(input('숫자1 입력:'))
##b = int(input('숫자2 입력:'))
##c=a+b
##if c >= 100:
##    print('100 이상입니다.')
##else:
##    print('100 미만 입니다.')
##a,b = map(int,input('숫자 2개 입력:').split())
##c = a + b
##if c >= 100:
##    print('100 이상입니다.')
##else:
##    print('100 미만 입니다.')
##a=int(input('식사 시간 입력:'))
##if 8 <= a <=9:
##    print('아침식사')
##elif 11 <= a <= 13:
##    print('점심식사')
##elif 17 <= a <= 20:
##    print('저녁식사')
##else:
##    print('식사시간이 아닙니다.')
a=input('생년월일 입력')
print(a[0:4] + '년')
print(a[4:6] + '월')
print(a[6:] + '일')
if a[0:4] <= '2000':
    print('20세기 인간')
else:
    print('21세기 인간')

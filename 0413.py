def days1(mon):
    
    if mon in (1,3,5,7,8,10,12):

        rv=31

    elif mon in (4,6,7,11):

        rv=30

    elif mon == 2 :

        rv=28

    else:

        print('월 입력 error')

        rv=0

    return rv

mon = int(input('월 입력:'))
print(days1(mon))


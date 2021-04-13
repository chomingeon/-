def day2(yymm):
    yy=int(yymm[0:4])
    mm= int(yymm[4:6])
    if mm in (1,3,5,7,8,10,12):
        rv = 31
    elif mm in (4,6,9,11) :
        rv=30
    else:
        if (yy%4 == 0 and yy%100 !=0) or yy%400 == 0:
            rv = 29
        else :
            rv=28
    return rv

yymm=input('연월을 입력하세요(예:200105) ')
print(day2(yymm))

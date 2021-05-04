##class Car:
##    color=''
##    speed=0
##
##    def upspeed(self,value):
##        self.speed+=value
##
##    def downspeed(salf,value):
##        self.speed-=value
##
##mycar1=Car()
##mycar1.color='빨강'
##mycar1.speed=0
##
##mycar2=Car()
##mycar2.color='노랑'
##mycar2.speed=0
##
##mycar3=Car()
##mycar3.color='파랑'
##mycar3.speed=0
##
##mycar1.upspeed(30)
##print('자동차의 1의 색상은 %이며, 현재 속도는 %dkm입니다' %(mycar1.color, mycar1.speed))
##
##mycar2.downspeed(60)
##print('자동차의 2의 색상은 %이며, 현재 속도는 %dkm입니다' %(mycar1.color, mycar1.speed))
##
##mycar3.downspeed(10)
##print('자동차의 3의 색상은 %이며, 현재 속도는 %dkm입니다' %(mycar1.color, mycar1.speed))

##class Car:
##    color=''
##    speed=0
##    def __init__(self):
##        self.color='빨'
##        self.speed=0
##    def upspeed(self,value):
##        self.speed+=value
##
##    def downspeed(self,value):
##        self.speed-=value

##class Car:
##    def __init__(self,value1,value2):
##        self.color=value1
##        self.speed=value2

##class Car:
##    count=0
##    def __init__(self):
##        self.speed=0
##        Car.count +=1

mycar1=Car()
mycar1.speed=30
print('자동차 1의 현재 속도는 %dkm, 생산된 자동차는 %d입니다.'%(mycar1.spped,Car.count))

mycar2=Car()
mycar2.speed=60
print('자동차 2의 현재 속도는 %dkm, 생산된 자동차는 %d입니다.'%(mycar2.spped,mycar2.count))

mycar3=Car()
mycar3.speed=100
print('자동차 3의 현재 속도는 %dkm, 생산된 자동차는 %d입니다.'%(mycar3.spped,mycar3.count))











































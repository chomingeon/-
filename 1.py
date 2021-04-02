# 리스트
'''
a = [1,2,3,4,5]
print(a)
a.append(10)
print(a)
a.append(6)
print(a)

b = []
print(b)
for i in range(5):
    temp = input('리스트에 추가할 값을 입력하세요:')
    b.append(temp)

print(b)

a = [1,2,3,4,5]
print(a)
a.append([6,7,8])
print(a)
print(a[5])

print(a[5][2]) # 만일 중첩된 리스트의 값에 접근하고 싶다면 사용 

b = [1,2,3,4,5]
print(b)
b.extend([6,7,8])
print(b)

c = [1,3,4,5,7]
print(c)
c.insert(1, 2)
print(c)
c.insert(5, 6)
print(c)
c.insert(7, 8) # 가장 마직막 인덱스 보다 : 큰 값을 인덱스로 저장하면  append와 동알한 동작을 한다
print(c)

d1 = [1,2,7,8]
d2 = [1,2,7,8]

d1.insert(2,[3,4,5,6])
print(d1)

d2[2:2] = [3,4,5,6]
print(d2)

a = [1,2,3,4,5]
a.pop()
print(a)
a.pop()
print(a)

b = [1,2,3,4,5]
b.pop(2)
print(b)
del b[1]
print(b)

c = [1,3,5,7,9]
c.remove(6)
print(c)
'''
























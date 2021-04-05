'''
b = [1,2,3,4,5]
b.pop(2)
print(b)
del b [1]
print(b)

c = [1,3,5,7,9]
c.remove(5)
print(c)

c = [1,3,5,7,9]
c.remove(6)
print(c)

d = [1,3,5,7,9]
for i in range(2):
    data = int(input('리스트에서 삭제할 값을 입력하세요 :'))
    if data in d:
        d.remove(data)
        print(d)
    else:
        print('리스트에 존재하지 않는 값입니다.')
        print(d)

a = [10,20,30,40,50]
print(a.index(40))
print(a.index(25))

a = [10,20,30,40,50,60,40]
print(a.count(40))

b = [30, 10, 40, 20, 60, 50]
b.sort()
print(b)
b.sort(reverse=True)
print(b)

b = [30, 10, 40, 20, 60, 50]
print(b)
b.reverse()
print(b)

test=[13,6,2,1,7,8,9,3,2,6,7,5,2]

a = [1,2,3,4,5]
b = a
print(id(a))
print(id(b))
print(a)
print(b)
b[3] = 400
print(a)
print(b)

a = [1,2,3,4,5]
b = a.copy()
print(id(a))
print(id(b))
print(a)
print(b)
b[3] = 400
print(a)
print(b)

c = [1,2,3,4,5]
d = [6,7,8,9,10]
c.clear()
del d[:]
print(c)
print(d)

a = ['서울','인천','대전','춘천','전주','광주','부산','울산']

for i in a:
    print(i, end='-')

a = ['서울','인천','대전','춘천','전주','광주','부산','울산']

for index, city in enumerate(a):
    print(city,'(',index,')')

a = [i for i in range(10)]
print(a)

b = [i+1 for i in range(10)]
print(b)

listA = [i+5 for i in range(10) if i%2 ==1]
print(listA)

a = [1.3, 2.6, 3.5, 4.7, 5.2]
a = list(map(int, a))
print(a)

a = [1.3, 2.6, 3.5, 4.7, 5.2]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = list(map(str.range(!0)))
print(a)

a = map(int, input().split())
print(a)
a =list(a)
print(a)
'''
a = [10,4,67,53,6,3,9]
print('리스트의 최소값',min(a))
print('리스트의 최대값',max(a))
print('리스트의 값들의 합',sum(a))












































































































'''
a = [1,3,5,7,10]
print(a)
a.append(11)
print(a)
a.insert(3,6)
print(a)
a[5:5]=[8,9]
print(a)
'''
lista = [1,2,3,4,5,6,7,8]
a=int(input('숫자를 입력하세요:'))
if a in lista:
      print(lista.index(a))
else:
    print('리스트에 없습니다')

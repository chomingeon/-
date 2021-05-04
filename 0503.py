import sqlite3
poem = ''' 오랜 벗과 한잔하는 날의 시

우린 뭐가 그리 바쁜지

한 계절을 못 만나고 살았다.

 

그래도 삶의 굽이굽이

문득 떠오르는 너의 얼굴

 

수천의 날들 동안

알뜰히 쌓인 우리의 깊은 우정.

 

좀 있다 만나서

친구야 무척 보고 싶었던 친구야

 

걸쭉하게 한잔하면서

가슴속 회포를 시원히 풀자.'''

con,cur=None,None
onechar,count='',0
con = sqlite3.connect("C:\\Users\\user\\Desktop\\sangilDB")
##con = sqlite3.connect("C:\\Users\\User\\Desktop\\sangilDB")

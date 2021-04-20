import sqlite3
con = sqlite3.connect("C:\\Users\\User\\Desktop\\sqlite\\sang")

cur= con.cursor()
cur.execute("CREATE TABLE studenTB (id char(5), name char(15),email char(15), birthyear int)")
cur.execute("INSERT INTO studenTB VALUES('31301','Anne','31301@naver.com',2004)")
cur.execute("INSERT INTO studenTB VALUES('31301','Rachel','31302@naver.com',2003)")
cur.execute("INSERT INTO studenTB VALUES('31301','James','31303@naver.com',2003)")
cur.execute("INSERT INTO studenTB VALUES('31301','Tom','31304@naver.com',2003)")

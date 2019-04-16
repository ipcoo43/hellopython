import sqlite3

conn = sqlite3.connect('test.db')

cur = conn.cursor() # 커서 위치를 시작지점을 가르킴 

cur.execute('select * from Student') # 커서는 Student의 처음을

rows = cur.fetchall()  # 모든 것을 가져오는 준비 fetch(가져오다), 데이터 주소
                       # fetchall은 리스트 형태로 반환
for row in rows:  # 엑세스 할 때 데이터에 접근
	print(row)

conn.close()
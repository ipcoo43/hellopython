import sqlite3

conn = sqlite3.connect('test.db')

width conn:
	cur = conn.cursor()
	sql = 'select * from Student where id=? or name=?'
	cur.execute(sql,(1,'홍일동'))
	row cur.fetchall()

	for row in rows:
		print(row)


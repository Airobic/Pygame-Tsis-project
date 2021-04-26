import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
# connection
cur = conn.cursor()
#insert
sql = """
insert into points(name) values(%s) returning name
"""
point_name = 'first'
cur.execute(sql, (point_name,)) # for many executemany(sql,(sssss,))
inserted_name = cur.fetchone()
print(inserted_name)
cur.close()
conn.commit()
conn.close()
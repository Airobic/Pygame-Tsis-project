import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
# connection
cur = conn.cursor()
#delete
sql = """
delete from points Where name = %s
"""
points_name = 'first'
cur.execute(sql, (points_name,))
print(cur.rowcount)
cur.close()
conn.commit()
conn.close()
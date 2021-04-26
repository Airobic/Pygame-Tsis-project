import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
# connection
cur = conn.cursor()
#update
sql = """
update points
set surname = %s
where name = %s
"""
surname = 'aleks'
point_name = 'first'
cur.execute(sql, (surname, point_name))
print(cur.rowcount)
cur.close()
conn.commit()
conn.close()
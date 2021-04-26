import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
# connection
cur = conn.cursor()
#querying
sql = """
select name from points
"""
cur.execute(sql)
row = cur.fetchone()
while row is not None:
    print(row)
    row = cur.fetchone()
cur.close()
conn.commit()
conn.close()
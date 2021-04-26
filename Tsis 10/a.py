import psycopg2
#create database postgres
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
# connection
cur = conn.cursor()
# create table
cur.execute("""
CREATE TABLE points (
    name varchar(255),
    surname varchar(255),
    id integer,
    student_points integer,
    joined_date date
);
""")

cur.close()
conn.commit()

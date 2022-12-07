import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="1111",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres")
cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS lifetime_data_1")

cur.execute("""CREATE TABLE lifetime_data_1 (object_id serial PRIMARY key,
            lifetime_name varchar (50) NOT NULL,
            lifetime_description varchar (140) NOT NULL , 
            lifetime_date date); """)

connection.commit()

cur.close()
connection.close()

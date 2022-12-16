from database import get_db_connection


if __name__ == '__main__':
    connection = get_db_connection()
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS lifetime_data_1")

    cur.execute(
        """CREATE TABLE lifetime_data_1 (object_id serial PRIMARY key,
                lifetime_name varchar (50) NOT NULL,
                lifetime_description varchar (140) NOT NULL , 
                lifetime_date date); """
    )

    connection.commit()
    cur.close()

    print('MIGRATION DONE')

    connection.close()

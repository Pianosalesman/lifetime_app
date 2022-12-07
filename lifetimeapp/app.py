import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


def get_lt_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="1111",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    return connection


@app.route('/')
def index():
    connection = get_lt_connection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM lifetime_data_1;')
    lifetime_data_1 = cur.fetchall()
    cur.close()
    connection.close()
    return render_template('index.html', lifetime_data_1=lifetime_data_1)


# noinspection PyUnresolvedReferences
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        lifetime_name = request.form['Название']
        lifetime_description = request.form['Описание']
        lifetime_date = request.form['calendar']
        connection = get_lt_connection()
        cur = connection.cursor()

        cur.execute('INSERT INTO lifetime_data_1(lifetime_name, lifetime_description, lifetime_date)'
                    'VALUES (%s, %s, %s)',
                    (lifetime_name, lifetime_description, lifetime_date))
        # noinspection PyUnresolvedReferences
        connection.commit()
        cur.close()
        connection.close()
        return redirect(url_for('index'))
    return render_template('create.html')

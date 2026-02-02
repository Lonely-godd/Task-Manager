import psycopg2
from secret import password


def connect_to_db():
    return psycopg2.connect(dbname='study_db',
                            user='postgres',
                            password=password,
                            host='localhost',
                            port='5432')


def print_result(cursor):
    result = cursor.fetchall()
    print(result)


if __name__ == '__main__':
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email='d.deerter@gmail.com';")
    print_result(cursor)

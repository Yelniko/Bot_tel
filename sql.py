import pymysql.cursors
from config import host, user, password, db_name

def connection_sql():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        print("successfully connected...")
        yield connection

        print("successfully disabled...")
        yield connection.close()

    except Exception as ex:
        print("Connection refused...\n", ex)

def request_sql():

    connection = connection_sql()

    try:
        with next(connection).cursor() as cursor:
            pass
    finally:
        next(connection)


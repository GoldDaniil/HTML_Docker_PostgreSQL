import psycopg2
from psycopg2 import sql

def authenticate_user(username, password):
    try:
        conn = psycopg2.connect(
            dbname="database_my",
            user="db_username",
            password="db_password",
            host="localhost",
            port="5432" #port="5001:5000"
        )
        cursor = conn.cursor()

        query = sql.SQL(" = %s")
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            print("yeah!")
            return True
        else:
            print("no!")
            return False

    except psycopg2.Error as e:
        print(f"network err: {e}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

username = input("логин: ")
password = input("пароль: ")
authenticate_user(username, password)

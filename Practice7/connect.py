import psycopg2
from config import load_config

def create_table():
    config = load_config()

    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    )
    """

    try:
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute(sql)
        conn.commit()

        cur.close()
        conn.close()

        print("Table created")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

if __name__ == "__main__":
    create_table()
        
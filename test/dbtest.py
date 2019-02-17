import _sqlite3

# Создание таблицы в БД для заполнения
def create_db():
    query("""CREATE TABLE WALLET
                        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        client VARCHAR(50),
                        money INTEGER )
                    """)

def add_data():
    for i in range(10):
        query("INSERT INTO WALLET (client, money) VALUES ('{0}', '{1}')".format('user' + str(i), i))

# Функция для подключения к БД и выполнения запроса
def query(sql):
    try:
        conn = _sqlite3.connect("../mydata.db")
    except _sqlite3.Error as err:
        print("Error: ", err)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def main():

    # Проверка доступности файла с данными
    try:
        query("SELECT COUNT(*) FROM WALLET")
    except:
        create_db()
    add_data()


if __name__ == '__main__':
    main()
import json
import _sqlite3


def query(sql):
    try:
        conn = _sqlite3.connect("mydata.db")
    except _sqlite3.Error as err:
        print("Error: ", err)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def get_data(data):
    sender = data['sender']
    destination = data['destination']
    order_sum = data['sum']
    return sender, destination, order_sum


def json_loads(data):
    obj = dict()
    data = data.replace('{', '')
    data = data.replace('}', '')
    data = data.replace('"', '')
    data = data.replace('\'', '')
    data = data.replace(' ', '')
    l = data.split(',')

    print(l)
    # sender = obj['sender']
    # destination = data['destination']
    # sum = data['sum']
    # return print(sender, destination, sum)
    return obj
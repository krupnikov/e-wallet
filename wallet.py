import json
import _sqlite3

N = 10
def query(sql):
    try:
        conn = _sqlite3.connect("mydata.db")
    except _sqlite3.Error as err:
        print("Error: ", err)

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


def check_money_stat(client):
    q = query("SELECT money FROM WALLET WHERE client = '{0}'".format(client))
    return q[0][0]


def update_money(sender, destination, order_sum):
    stat = check_money_stat(destination)
    if stat > N:
        return print('Перевод нельзя выпольнить')
    else:
        query("UPDATE WALLET SET money = money - {0} WHERE client = '{1}'".format(order_sum, sender))
        query("UPDATE WALLET SET money = money + {0} WHERE client = '{1}'".format(order_sum, destination))


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


def main():
    data = {"sender": "user5", "destination": "user1", "sum": 3}
    sender, destination, order_sum = get_data(data)
    update_money(sender, destination, order_sum)


main()
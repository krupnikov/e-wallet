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
        return print('Перевод нельзя выполнить')
    else:
        query("UPDATE WALLET SET money = money - {0} WHERE client = '{1}'".format(order_sum, sender))
        query("UPDATE WALLET SET money = money + {0} WHERE client = '{1}'".format(order_sum, destination))


def get_data(data):
    sender = data['sender']
    destination = data['destination']
    order_sum = data['sum']
    return sender, destination, order_sum


def main_job(data):
    sender, destination, order_sum = get_data(data)
    update_money(sender, destination, order_sum)

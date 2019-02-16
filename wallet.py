import json

def json_loads(data):
    obj = dict()
    data = data.replace('{', '')
    data = data.replace('}', '')
    print(obj)
    # sender = obj['sender']
    # destination = data['destination']
    # sum = data['sum']
    # return print(sender, destination, sum)
    return obj
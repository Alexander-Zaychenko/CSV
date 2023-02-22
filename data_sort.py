from data import data


def data_sort(data):
    new_data = {}
    for i in data:
        name, item, count = i.split(',')
        new_data[name] = {item: count}
    print(new_data)
    data = new_data

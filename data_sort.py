from data import data
from data_pack import data_pack


def data_sort(data):
    new_data = {}
    for i in data:
        name, item, count = i.split(',')
        new_data[name] = {item: count}
    return new_data

print(data_sort(data))
print(data_pack(data_sort(data)))

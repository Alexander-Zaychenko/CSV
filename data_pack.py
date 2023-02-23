from data import data

def data_pack(data):
    packed_data = []
    for name, item_count in data.items():
        for item, count in item_count.items():
            packed_data.append(name + ',' + item + ',' + count)
    return packed_data

# print(data_pack(data))
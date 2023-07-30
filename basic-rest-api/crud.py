# This file imitates CRUD operations for a database
from random import randint

items_data = {
    '1': {
        'name': 'item_1',
        'size': 45,
        'description': 'First item'
    },
    '2': {
        'name': 'item_2',
        'size': 50,
        'description': 'Second item'
    }
}


def read_item(item_id):
    return items_data[item_id]


def read_all_items():
    return items_data


def create_item(name, size, description):
    item_id = str(randint(3, 100))
    items_data[item_id] = {
        'name': name,
        'size': size,
        'description': description,
    }
    return item_id

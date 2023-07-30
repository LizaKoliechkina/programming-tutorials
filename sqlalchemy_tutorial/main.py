from db_query import insert_record, retrieve_data, update_product_price

if __name__ == '__main__':
    insert_record(1, 'product1', 404.6, 'First product')
    insert_record(2, 'product2', 504.6, 'Second product')
    insert_record(3, 'product3', 104.6, 'Third product')
    update_product_price(5, 734.0)
    print(retrieve_data())

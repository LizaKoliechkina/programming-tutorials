from fastapi import FastAPI

import crud

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/items')
async def read_all_items():
    items = crud.read_all_items()
    return items

@app.get('/items/{item_id}')
async def read_item(item_id):
    item = crud.read_item(item_id)
    return item

@app.post('/items/create_item')
async def create_item(name, size, description):
    item_id = crud.create_item(name, size, description)
    return item_id


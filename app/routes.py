from . import api

@api.get("/")
async def get_root():
    return {"Hello": "World"}

@api.get("/items/{item_id}")
async def read_item(item_id:int, q:str=None):
    return {"item_id": item_id, "q": q}

def get_name_with_age(name:str, age:int):
    waa:int = 2
    full_name:str = name.title() + str(age)

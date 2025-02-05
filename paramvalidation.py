from fastapi import FastAPI , Path , Query
app = FastAPI()
# path params
@app.get("/products/{product_id}")
async def get_product(product_id:int = Path(...,gt=0)):
    return {"product id:",product_id}

# QUERY PARAMS
@app.get("/items/")
async def read_items(limit: int = Query(10, gt=0, lt=100)):  # Default value 10
    return {"message": f"Returning {limit} items"}



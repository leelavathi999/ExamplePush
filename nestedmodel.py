from typing import Tuple
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Define the supplier model
class supplier(BaseModel):
    supplierID: int
    supplierName: str

# Define the product model
class product(BaseModel):
    productID: int
    prodname: str
    price: int
    supp: supplier  # supplier as a nested model

# Define the customer model
class customer(BaseModel):
    custID: int
    custname: str
    prod: Tuple[product]  # Tuple of products (a list of products)

@app.get("/sayhello/")
async def sayhello():
    return {"message": "hi hello"}

@app.post("/invoice/")
async def getInvoice(c1: customer):
    return c1

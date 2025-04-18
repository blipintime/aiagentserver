from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Define data models
class Card(BaseModel):
    id: int
    name: str
    type: str
    owner_id: Optional[int] = None

class Customer(BaseModel):
    id: int
    name: str
    email: str

# Mock database (in memory for this example)
cards_db = [
    Card(id=1, name="Visa Gold", type="credit", owner_id=1),
    Card(id=2, name="Mastercard Platinum", type="credit", owner_id=2)
]

customers_db = [
    Customer(id=1, name="John Doe", email="john@example.com"),
    Customer(id=2, name="Jane Smith", email="jane@example.com")
]

# API endpoints
@app.get("/api/cards", response_model=List[Card])
async def get_cards():
    return cards_db

@app.get("/api/cards/{card_id}")
async def get_card(card_id: int):
    card = next((card for card in cards_db if card.id == card_id), None)
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

@app.post("/api/card", response_model=Card)
async def create_card(card: Card):
    # In a real application, you would validate and save to a database
    cards_db.append(card)
    return card

@app.get("/api/customers", response_model=List[Customer])
async def get_customers():
    return customers_db

@app.get("/api/customers/{customer_id}")
async def get_customer(customer_id: int):
    customer = next((customer for customer in customers_db if customer.id == customer_id), None)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 
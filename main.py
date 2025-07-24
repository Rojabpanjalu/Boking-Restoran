from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import uuid
import os

app = FastAPI()

DATA_FILE = "data.json"

class Booking(BaseModel):
    id: str
    name: str
    phone: str
    date: str
    time: str
    people: int

def read_data() -> List[Booking]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [Booking(**item) for item in json.load(f)]

def write_data(bookings: List[Booking]):
    with open(DATA_FILE, "w") as f:
        json.dump([booking.dict() for booking in bookings], f, indent=2)

@app.get("/bookings", response_model=List[Booking])
def get_bookings():
    return read_data()

@app.post("/bookings", response_model=Booking)
def create_booking(booking: Booking):
    bookings = read_data()
    bookings.append(booking)
    write_data(bookings)
    return booking

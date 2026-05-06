import time
from datetime import date
from fastapi import FastAPI
from src.models import WeatherRecord
from src.services import fetch_coordinates, fetch_weather
from src.database import save_and_clean
app = FastAPI(title="Pro Weather API Clone")

@app.get("/weather/{city}")
async def read_weather(city: str):
    start_time = time.time()
    
    # Logic flow
    loc = await fetch_coordinates(city)
    raw_weather = await fetch_weather(loc["latitude"], loc["longitude"])
    
    # Create & Validate with Pydantic
    record = WeatherRecord(
        city=loc["name"],
        country=loc.get("country"),
        temperature=raw_weather["current_weather"]["temperature"],
        windspeed=raw_weather["current_weather"]["windspeed"],
        total_taken=round(time.time() - start_time, 4),
        date_of_request=date.today()
    )
    
    save_and_clean(record)
    return record
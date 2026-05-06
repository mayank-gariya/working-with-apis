import httpx
from fastapi import HTTPException

# Ensure the name matches EXACTLY what you call in main.py
async def fetch_coordinates(city: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()
        if not data.get('results'):
            raise HTTPException(status_code=404, detail="City not found")
        return data['results'][0]

async def fetch_weather(lat: float, lon: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail="Weather API error")
        return resp.json()
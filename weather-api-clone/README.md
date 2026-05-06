# 🌦️ Pro Weather API Clone

A professional, modular FastAPI implementation of a Weather API using the Open-Meteo geocoding and forecast services. This project features Pydantic validation, a clean folder hierarchy, and automated query logging with duplicate removal.

## 🚀 Features

- **Asynchronous API Calls:** Uses `httpx` for non-blocking requests to Open-Meteo.
- **Pydantic Validation:** Strict data typing and custom validation for temperature and windspeed.
- **Folder Hierarchy:** Clean separation of concerns (Models, Database, Services, Routes).
- **History Logging:** Saves unique city queries to a `data.json` file.
- **Auto-Cleanup:** Automatically removes duplicate city entries, keeping only the most recent search.

## 📂 Project Structure

```text
weather-api-clone/
├── data/
│   └── data.json          # Persistent storage for query history
├── src/
│   ├── __init__.py        # Makes src a Python package
│   ├── main.py            # FastAPI entry point and routes
│   ├── models.py          # Pydantic schemas and validators
│   ├── services.py        # External API communication (Open-Meteo)
│   └── database.py        # File I/O and data cleaning logic
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 🛠️ Setup & Installation

1. **Clone the project:**
   ```bash
   git clone <your-repo-url>
   cd weather-api-clone
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn src.main:app --reload
   ```

4. **Access the Documentation:**
   - Interactive Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📡 API Endpoints

### 1. Get Weather
**`GET /weather/{city}`**
Fetches current weather for a specific city, validates the data, and logs it to history.

**Example Response:**
```json
{
  "city": "London",
  "country": "United Kingdom",
  "temperature": 15.2,
  "windspeed": 12.5,
  "unit": "Celsius",
  "total_taken": 0.4521,
  "date_of_request": "2024-05-06"
}
```

### 2. Root Section
**`GET /`**
Returns a simple welcome message.

## 🧪 Validation Logic (Pydantic)
- **Windspeed:** Must be greater than or equal to 0.
- **Temperature:** Validated to be within realistic Earth limits (-90°C to 60°C).
- **City Name:** Minimum length of 1 character required.

## 📝 Requirements
- FastAPI
- Uvicorn
- HTTPX
- Pydantic

# FastAPI Machine Learning Model Deployment on Google Colab

This repository contains an advanced-level implementation for deploying a Machine Learning model using **FastAPI** within a Google Colab environment. The project demonstrates the integration of asynchronous web services with predictive modeling, utilizing **ngrok** for public accessibility.

## 🚀 Project Overview

The core objective of this project is to serve a pre-trained machine learning model (`model.pkl`) via a RESTful API. It handles customer data to provide real-time recommendations, showcasing a production-like deployment workflow in a cloud-based notebook.

## 🛠️ Technical Stack

* **FastAPI**: A high-performance web framework for building APIs with Python.
* **Uvicorn**: An ASGI web server implementation for Python.
* **Pydantic**: Data validation and settings management using Python type annotations.
* **Pyngrok**: A Python wrapper for ngrok to manage secure tunnels.
* **Joblib**: For loading the serialized machine learning model.
* **Pandas**: For data manipulation and preparing inputs for the model.

## 📖 Code Explanation

### 1. Initialization and Environment Setup
The project begins by installing necessary dependencies and importing core modules. 
* `nest_asyncio.apply()` is crucial as it allows `uvicorn` to run within the notebook's existing event loop without conflicts.

### 2. Data Validation Schema
We use Pydantic's `BaseModel` to define the `PredictionInput` class. This ensures that the API only accepts properly formatted data, including:
* `age`: Customer age.
* `gender`: Gender identification.
* `city`: Customer location.
* `income` & `spending_score`: Financial metrics for the recommendation engine.

### 3. API Endpoints
* **`@app.get('/')`**: Returns a JSON greeting to verify the server is active.
* **`@app.post('/predict')`**: The primary logic gate. It converts incoming JSON data into a Pandas DataFrame, passes it to the `model.predict()` function, and returns a user-friendly recommendation status (Yes/No) based on the model's inference.

### 4. Background Server Execution
To prevent the server from blocking the Colab interface, we utilize the `threading` library. By running `uvicorn.run()` in a separate thread, the API remains live while the notebook stays responsive.

## 🔧 How to Run

1.  Place your `model.pkl` in the project directory.
2.  Set your `auth_token` for ngrok.
3.  Execute the cells to generate a public URL.
4.  Navigate to `{public_url}/docs` to test the endpoints using the interactive Swagger UI.

---

**Signed by:**
Mayank Gariya
**Email:** mayankgariya482@gamil.com

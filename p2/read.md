This project is a High-Concurrency Inventory Management System built with FastAPI. It is designed to simulate a real-world "Flash Sale" environment where multiple users might attempt to purchase limited stock simultaneously.

The core value of this project is its focus on Data Integrity and Concurrency Control, moving beyond a simple "CRUD" app into professional backend engineering.

## Technical Architecture
Framework: FastAPI (Asynchronous) for high-performance API routing.

Database: PostgreSQL (simulated via SQLite + aiosqlite) using SQLAlchemy 2.0.

Pattern: Service-Repository Pattern, which separates business logic from API endpoints for better maintainability.

Validation: Pydantic V2 for strict request/response data modeling.

## Key "Industry-Grade" Features
Atomic Transactions: Uses async with db.begin() to ensure that either an entire purchase happens or none of it does, preventing partial data corruption.

Row-Level Locking: Implements .with_for_update() in SQL queries. This locks specific product rows during a transaction, preventing "Race Conditions" where two users buy the last item at the same time.

Database-Level Constraints: Includes a CheckConstraint on the stock_count column. This acts as a final safety net, ensuring the database physically rejects any operation that would result in negative inventory.

Asynchronous I/O: Every database hit is non-blocking, allowing the server to handle hundreds of concurrent connections without hanging.

## Project Structure
Plaintext
app/
├── database/
│   └── config.py      # Async engine & session management
├── models/
│   └── inventory.py   # SQL Alchemy models with DB constraints
├── schemas/
│   └── inventory.py   # Pydantic models for data validation
├── services/
│   └── inventory_service.py  # Business logic & Row-locking
└── main.py            # API routes and application entry point

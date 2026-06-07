# School Students API Project

A comprehensive FastAPI project demonstrating complete CRUD (Create, Read, Update, Delete) operations with MongoDB integration.

## 📋 Project Overview

This project showcases the development of a fastAPI for managing school student data. Built with Python and MongoDB, it demonstrates professional API design patterns and database management practices.

## 🎯 Key Features

### CRUD Operations
- **Create** - Add new student records to the database
- **Read** - Retrieve and query student information
- **Update** - Modify existing student data
- **Delete** - Remove student records from the database

### Technology Stack
- **Backend**: Python
- **Database**: MongoDB
- **Connection**: MongoDB Atlas
- **API Framework**: fastAPI

## 📁 Project Structure

```
School students project/
├── confugration.py          # MongoDB connection configuration
├── api_endpoints.py         # CRUD API endpoints
├── models.py               # Data models
└── src/                    # Resources and images
```

## 🔧 Configuration

The project uses MongoDB Atlas for cloud-based database management. Connection details are configured in `confugration.py`:

```python
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://albert:<password>@todo.58rwtsz.mongodb.net/?appName=todo"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.todo
collections = db['school_data']
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/mayank-gariya/working-with-apis.git
   cd working-with-apis
   ```

2. **Install dependencies**
   ```bash
   pip install pymongo
   ```

3. **Run the API**
   ```bash
   uvicorn main:app --reload
   ```

## 📊 API Endpoints

### Create Student
```
POST /students
```
Add a new student record to the database.

### Read Students
```
GET /students
GET /students/<id>
```
Retrieve all students or a specific student by ID.

### Update Student
```
PUT /students/<id>
```
Update an existing student's information.

### Delete Student
```
DELETE /students/<id>
```
Remove a student record from the database.

## 💾 Database Schema

The project uses MongoDB collections to store school student data with flexible document structures, allowing for scalable and dynamic data management.

## 📚 Learning Outcomes

Through this project, I've demonstrated:
- ✅ fastAPI design principles
- ✅ MongoDB integration and queries
- ✅ Complete CRUD operation implementation
- ✅ Database connection management
- ✅ Python best practices
- ✅ streamlit for frontend 

## 👨‍💻 Author

**Mayank**

---

*Last Updated: June 7, 2026*

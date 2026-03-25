Open a terminal at the root of the project path.
For building the project use command:
```
git clone git@github.com:ivanova-zz/to-do-test.git
cd to-do-test
docker-compose up -d 
```
The API will be available at http://localhost:8000

**Task Management REST API**

A clean, lightweight, and professional RESTful API built with FastAPI to manage a to-do list. This project demonstrates modern Python development practices including Clean Architecture, Pydantic validation, and Unit/Integration testing.

**Features**

_1. RESTful Endpoints_: Full CRUD operations for tasks.

_2. In-Memory Storage_: Fast execution using Python's native data structures.

_3. Automatic ID Generation_: No need to provide IDs when creating tasks.

_4. Data Validation_: Powered by Pydantic models.

_5. Interactive Documentation_: Built-in Swagger UI and ReDoc.

_6. Dockerized_: Ready for containerized deployment.

_7. Fully Tested_: High coverage with pytest.

**Documentation**

- Swagger UI: http://localhost:8000/docs

- ReDoc: http://localhost:8000/redoc
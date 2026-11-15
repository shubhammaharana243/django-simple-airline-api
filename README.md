# ✈️ Django Simple Airline API

A RESTful Airline Management API built using **Python, Django, and Django REST Framework**. This project demonstrates REST API development, CRUD operations, serializers, relational database handling, and Many-to-Many relationships.

## 🚀 Features

- **Flight Management:** Create, retrieve, update, and delete flight records.
- **Passenger Management:** Manage passenger records through REST API endpoints.
- **Airport Management:** Manage airport records using Django Admin.
- **Foreign Key Relationships:** Connect flights with origin and destination airports.
- **Many-to-Many Relationship:** Associate multiple passengers with multiple flights.
- **Custom Serializers:** Customize API input and output representations.
- **Related Field Handling:** Represent airport relationships using city names.
- **ViewSets:** Implement CRUD operations using Django REST Framework ModelViewSet.
- **API Routing:** Automatically generate API routes using DefaultRouter.
- **API Browsable Interface:** Interact with API endpoints through DRF's browsable API.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Django | Backend Framework |
| Django REST Framework | REST API Development |
| SQLite | Database |
| Git & GitHub | Version Control |

## 📂 Project Structure

```text
django-simple-airline-api/
│
├── airline_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── flights/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/shubhammaharana243/django-simple-airline-api.git

cd django-simple-airline-api
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate virtual environment**

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Create a superuser**

```bash
python manage.py createsuperuser
```

**7. Run development server**

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## 📡 API Endpoints

Base URL:

```text
http://127.0.0.1:8000/api/
```

### ✈️ Flight Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/api/flights/` | Retrieve all flights |
| POST | `/api/flights/` | Create a new flight |
| GET | `/api/flights/{id}/` | Retrieve a specific flight |
| PUT | `/api/flights/{id}/` | Update a flight |
| PATCH | `/api/flights/{id}/` | Partially update a flight |
| DELETE | `/api/flights/{id}/` | Delete a flight |

### 👤 Passenger Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/api/passengers/` | Retrieve all passengers |
| POST | `/api/passengers/` | Create a new passenger |
| GET | `/api/passengers/{id}/` | Retrieve a specific passenger |
| PUT | `/api/passengers/{id}/` | Update a passenger |
| PATCH | `/api/passengers/{id}/` | Partially update a passenger |
| DELETE | `/api/passengers/{id}/` | Delete a passenger |

*Note: These endpoints are generated using Django REST Framework's DefaultRouter and ModelViewSet.*

## 🗄️ Database Relationships

This project demonstrates two types of database relationships.

### 1. ForeignKey Relationship

A Flight is connected to two Airport records:

- Origin Airport
- Destination Airport

```python
class Flight(models.Model):
    origin = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="departures"
    )

    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="arrivals"
    )

    duration = models.IntegerField()
```

### 2. Many-to-Many Relationship

A Passenger can be associated with multiple flights, and a flight can have multiple passengers.

```python
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    flights = models.ManyToManyField(
        Flight,
        blank=True,
        related_name="passengers"
    )
```

**Relationship overview:**

```text
Airport ───────< Flight
                   |
                   |
              Many-to-Many
                   |
                   |
               Passenger
```

## 📝 API Request Examples

### Create a Flight

**POST**

```text
/api/flights/
```

Example request:

```json
{
    "origin": "New York",
    "destination": "London",
    "duration": 415
}
```

Example response:

```json
{
    "id": 1,
    "origin": "New York",
    "destination": "London",
    "duration": 415
}
```

*Airport city values must match existing Airport records.*

### Create a Passenger

**POST**

```text
/api/passengers/
```

Example request:

```json
{
    "first": "Shubham",
    "last": "Maharana",
    "flights": [1, 2]
}
```

Example response:

```json
{
    "id": 1,
    "first": "Shubham",
    "last": "Maharana",
    "flights": [1, 2]
}
```

*Note: The flight IDs must already exist in the database. These examples illustrate the default ModelSerializer representation of the Many-to-Many relationship.*

## 🛠️ Django Admin

Airport, Flight, and Passenger models are registered in Django Admin.

Access the admin panel:

```text
http://127.0.0.1:8000/admin/
```

Create a superuser to manage database records through the admin interface.

## 📚 Concepts Practiced

- Django REST Framework fundamentals
- ModelSerializer
- Custom Serializers
- ForeignKey Relationships
- Many-to-Many Relationships
- PrimaryKeyRelatedField and SlugRelatedField
- ModelViewSet
- DefaultRouter
- GET, POST, PUT, PATCH and DELETE operations
- JSON Serialization and Deserialization
- Django ORM
- Database Migrations
- Django Admin

## 🎯 Project Purpose

This project was developed as a hands-on learning project to understand REST API development using Django REST Framework.

The main focus is on CRUD operations, database relationships, serializers, ViewSets, and API routing.

## 👨‍💻 Author

**Shubham Maharana**

- GitHub: [@shubhammaharana243](https://github.com/shubhammaharana243)
- Project Repository: [Django Simple Airline API](https://github.com/shubhammaharana243/django-simple-airline-api)

---

⭐ If you find this project useful, consider giving it a star on GitHub!

# ✈️ Django Simple Airline API

A RESTful Airline Management API built using **Python, Django, and Django REST Framework**. This project focuses on managing airports and flights while demonstrating REST API development and relational database handling.

## 🚀 Features

- **Airport Management:** Manage airport records with city and airport codes.
- **Flight Management:** Create, retrieve, update, and delete flight records.
- **Foreign Key Relationships:** Connect flights with origin and destination airports.
- **Custom Serializers:** Customize API input and output representations.
- **Related Field Handling:** Display airport information in `City (CODE)` format.
- **API Browsable Interface:** Interact with API endpoints through Django REST Framework's browsable API.

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
├── Airlines/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── Flights/
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
python manage.py migrate
```

**6. Run development server**

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## 📡 API Functionality

The API supports airport and flight management.

### Airports

- Create airport records.
- Retrieve airport information.
- View airport city and code.

### Flights

- Create new flights.
- Retrieve flight details.
- Update existing flights.
- Delete flights.
- Associate flights with origin and destination airports.

### Example Flight JSON

**Request:**

```json
{
    "origin": "JFK",
    "destination": "LHR",
    "duration": 415
}
```

**Example Response:**

```json
{
    "id": 1,
    "origin": "New York (JFK)",
    "destination": "London (LHR)",
    "duration": 415
}
```

*Note: The example demonstrates the custom airport relationship representation. Actual endpoint paths depend on the project's URL configuration.*

## 📚 Concepts Practiced

- Django REST Framework fundamentals
- ModelSerializer
- Custom serializers
- ForeignKey relationships
- Primary Key and Slug Related Fields
- SerializerMethodField and custom RelatedField
- GET, POST, PUT, PATCH and DELETE operations
- JSON serialization and deserialization
- API request and response handling

## 🎯 Project Purpose

This project was developed as a hands-on learning project to understand REST API development using Django REST Framework, especially model relationships, serializers, and CRUD operations.

## 👨‍💻 Author

**Shubham Maharana**

- GitHub: [@shubhammaharana243](https://github.com/shubhammaharana243)
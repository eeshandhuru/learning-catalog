# Learning Catalog API

A Django REST API for managing Vendors, Products, Courses, Certifications, and their relationships through mapping tables.

---

# 1. Project Setup

### 1. Clone the Repository

```bash
git clone <repository_url>
cd learning-catalog
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

# 2. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

Main dependencies include:

* Django
* Django REST Framework
* drf-yasg (Swagger documentation)
* psycopg2-binary (PostgreSQL adapter)

---

# 3. Installed Apps

The project contains the following Django apps:

| App                          | Description                        |
| ---------------------------- | ---------------------------------- |
| vendor                       | Manages vendor information         |
| product                      | Manages products                   |
| course                       | Manages courses                    |
| certification                | Manages certifications             |
| vendor_product_mapping       | Vendor–Product relationships       |
| product_course_mapping       | Product–Course relationships       |
| course_certification_mapping | Course–Certification relationships |

---

# 4. Database Configuration

Configure PostgreSQL in `settings.py`.

Example:

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "learning_catalog",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

---

# 5. Run Migrations

Generate migration files:

```bash
python manage.py makemigrations
```

Apply migrations to create tables:

```bash
python manage.py migrate
```

---

# 6. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create login credentials.

---

# 7. Run Development Server

Start the Django server:

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

Swagger documentation:

```
http://127.0.0.1:8000/swagger/
```

---

# 8. API Usage Examples

## Create Vendor

POST `/api/vendors/`

Request Body:

```json
{
  "name": "AWS",
  "code": "AWS01",
  "description": "Cloud provider"
}
```

---

## Get Vendors

GET `/api/vendors/`

Response:

```json
[
  {
    "id": 1,
    "name": "AWS",
    "code": "AWS01",
    "description": "Cloud provider",
    "created_at": "2026-03-16T10:00:00"
  }
]
```

---

## Create Product

POST `/api/products/`

```json
{
  "name": "Cloud Computing",
  "code": "CC01"
}
```

---

## Create Vendor–Product Mapping

POST `/api/vendor-product-mappings/`

```json
{
  "vendor": 1,
  "product": 1,
  "primary_mapping": true
}
```

---

## Get Vendor–Product Mappings

GET `/api/vendor-product-mappings/`

Filter by vendor:

```
GET /api/vendor-product-mappings/?vendor_id=1
```

---

# 9. Soft Delete

The project implements **soft delete** using the `is_active` field.

DELETE requests do not remove records from the database; instead they update:

```
is_active = False
```

Inactive records are excluded from GET responses.

---

# 10. API Documentation

Interactive API documentation is available through Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

It allows:

* Viewing all endpoints
* Testing APIs
* Checking request/response formats
* Exploring query parameters

---

# 11. Project Features

* Modular Django app structure
* REST APIs using Django REST Framework
* Soft delete implementation
* Mapping tables with validation
* PostgreSQL database integration
* Swagger API documentation

# 📝 MarkFlow - Online Markdown Editor API

A Django REST API for creating, editing, managing, and tagging Markdown documents.  
Built as a coding assessment for Barq.dev – with authentication, filters, Docker support, and optional test cases.

---

## 🚀 Features

- JWT-based Authentication using SimpleJWT
- Create, update, delete Markdown documents
- Tag documents and filter by tags
- Sort documents by created or updated date
- Dockerized setup with SQLite support

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 4+
- Django REST Framework
- SimpleJWT (JWT Authentication)
- SQLite (default)
- Docker (bonus)
- Optional: PostgreSQL for production

---

## 🔐 API Endpoints

| Method | Endpoint                      | Description                            | Auth |
|--------|-------------------------------|----------------------------------------|------|
| POST   | `/api/users/login/`           | Login with username & password         | ❌   |
| GET    | `/api/documents/`             | List all documents (filter/sort ready) | ✅   |
| POST   | `/api/documents/`             | Create new Markdown document           | ✅   |
| GET    | `/api/documents/<id>/`        | Retrieve single document               | ✅   |
| PATCH  | `/api/documents/<id>/`        | Update a document                      | ✅   |
| DELETE | `/api/documents/<id>/`        | Delete a document                      | ✅   |

### 🔎 Optional Query Params

- `?sort=created` or `?sort=updated`
- `?tag=<tag_id>`

---

## 🧪 Example API Response (POST `/api/documents/`)

**Request:**
```json
{
  "title": "My Doc",
  "content": "# Hello Markdown!",
  "tags": [1, 2]
}


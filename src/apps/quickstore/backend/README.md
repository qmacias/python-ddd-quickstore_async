### Getting Started

Here the clients interact with the provided endpoints

---

#### Quickstore Backend Routes

| Method | Url                                   | Description        |
|--------|---------------------------------------|--------------------|
| GET    | http://127.0.0.1:8001/status-check    | Status check       |
| PUT    | http://127.0.0.1:8001/users/{user_id} | Creates a new user |

Status check
```bash
http GET http://127.0.0.1:8001/status-check
```

Creates a new user
```bash
echo '{"name": "John Doe", "email": "john.doe@example.com"}' | http PUT http://127.0.0.1:8001/users/04c0176d-30b3-4ace-b8f1-e2e51b0eca56
```
### Getting Started

Here the clients interact with the provided endpoints

---

#### Backoffice Backend Routes

| Method | Url                                         | Description           |
|--------|---------------------------------------------|-----------------------|
| GET    | http://127.0.0.1:8000/status-check          | Status check          |
| PUT    | http://127.0.0.1:8000/users/{user_id}       | Creates a new user    |
| PUT    | http://127.0.0.1:8000/products/{product_id} | Creates a new product |

Status check
```bash
http GET http://127.0.0.1:8000/status-check
```

Creates a new user
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:8000/users/04c0176d-30b3-4ace-b8f1-e2e51b0eca56
```

Creates a new product
```bash
echo '{"name": "Wireless Mouse"}' | http PUT http://127.0.0.1:8000/products/8f3e9d63-c83a-48de-8815-bf08a9e52219
```
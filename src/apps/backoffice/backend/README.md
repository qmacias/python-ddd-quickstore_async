### Getting Started

Here the clients interact with the provided endpoints

---

#### Backoffice Backend Routes

| Method | Url                                         | Description           |
|--------|---------------------------------------------|-----------------------|
| GET    | http://127.0.0.1:8000/status-check          | Status check          |
| PUT    | http://127.0.0.1:8000/products/{product_id} | Creates a new product |

Status check
```bash
http GET http://127.0.0.1:8000/status-check
```

Creates a new product
```bash
echo '{"name": "Wireless Mouse", "price": 2499}' | http PUT http://127.0.0.1:8000/products/8f3e9d63-c83a-48de-8815-bf08a9e52219
```
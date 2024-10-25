### Getting Started

Here the clients interact with the provided endpoints

---

#### Quickstore Backend Routes

| Method | Url                                                     | Description                  |
|--------|---------------------------------------------------------|------------------------------|
| GET    | http://127.0.0.1:8001/status-check                      | Status check                 |
| PUT    | http://127.0.0.1:8001/users/{user_id}                   | Creates a new user           |
| PUT    | http://127.0.0.1:8001/productreviews/{productreview_id} | Creates a new product review |


Status check
```bash
http GET http://127.0.0.1:8001/status-check
```

Creates a new user
```bash
echo '{"name": "John Doe", "email": "john.doe@example.com"}' | http PUT http://127.0.0.1:8001/users/04c0176d-30b3-4ace-b8f1-e2e51b0eca56
```

Creates a new product review
```bash
echo '{"userId": "e3385ef0-75e6-4f9a-a464-0c6c535ea69a", "productId": "cb510aff-28e0-4f91-9194-5f280ffbc326", "rating": 3}' | http PUT http://127.0.0.1:8001/productreviews/a783ce5c-a9bd-4589-81eb-53b195e7cb46
```
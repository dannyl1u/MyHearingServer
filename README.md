# MyHearingServer

## Endpoints

### 1. Insert Data

- **URL:** `/api/v1/insert`
- **Method:** `POST`
- **Description:** Inserts new row of data including a location specified by latitude and longitude, a noise level, and a timestamp.
- **Content-Type:** `application/json`
- **Request Body:**
  ```json
  {
    "latitude": "<latitude>",
    "longitude": "<longitude>",
    "noise_level": "<noise_level>",
    "timestamp": "<timestamp>"
  }```
- **Curl Example:**:
```bash
curl -X POST http://127.0.0.1:5000/api/v1/insert \
-H "Content-Type: application/json" \
-d '{"latitude": "40.7128", "longitude": "-74.0060", "noise_level": "55", "timestamp": "2023-11-26T15:30:00"}'
```

### 2. Get Data

- **URL:** `/api/v1/get`
- **Method:** `GET`
- **Description:** Retrieves all saved rows
- **Response:** JSON array of objects, each representing a row.
  - Example Response:
    ```json
    [
      {
        "Location": "40.7128, -74.0060",
        "Noise Level": "55",
        "Timestamp": "2023-11-26T15:30:00"
      },
      ...
    ]
    ```
- **Curl Example:**
```bash
 curl http://127.0.0.1:5000/api/v1/get
```
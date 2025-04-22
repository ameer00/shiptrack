# Package Management API - Flask Implementation

This is a simple Flask application that provides an API endpoint to retrieve package details based on a `packageId`. It reads data from a local JSON file (`packages.json`).

## Features

*   GET `/packages/{packageId}`: Retrieves details for a specific package.

## Setup

1.  **Clone the repository (if applicable) or ensure you have the files:**
    *   `app.py`
    *   `test_app.py`
    *   `packages.json`
    *   `README.md`

2.  **Install dependencies:**
    ```bash
    pip install Flask
    ```

## Running the Application

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/app.py
```
The application will start on `http://127.0.0.1:5000` by default.

## Running Tests

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/test_app.py
```

## Example Usage

To get package details for `packageId` "1":
```bash
curl http://127.0.0.1:5000/packages/1
```

To get package details for a non-existent `packageId` "999":
```bash
curl http://127.0.0.1:5000/packages/999
```
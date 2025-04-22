# Package Management API - Flask Implementation

This is a simple Flask application that provides an API endpoint to retrieve package information based on its `packageId`. The data is sourced from a local JSON file (`packages.json`).

## Features

*   **Get Package by ID:** Retrieve details for a specific package using the `/packages/{packageId}` endpoint.

## Setup

1.  **Prerequisites:**
    *   Python 3.x
    *   pip (Python package installer)

2.  **Installation:**
    ```bash
    pip install Flask
    ```

3.  **Data File:**
    Ensure the `/Users/ameerabbas/Documents/GCP/shiptrack/packages.json` file exists and contains the package data in the expected JSON format (an array of package objects).

## Running the Application

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/app.py
```
The application will start, typically listening on `http://127.0.0.1:5000/`.

## Running Tests

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/test_app.py
```

## Example Usage (using curl)

```bash
# Get package with ID '1'
curl http://127.0.0.1:5000/packages/1

# Try to get a non-existent package
curl http://127.0.0.1:5000/packages/999
```
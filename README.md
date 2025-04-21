# Package Information API

This Flask application provides an API endpoint to retrieve package information based on its `packageId`. It reads data from a local `packages.json` file.

## Features

*   GET `/packages/{packageId}`: Retrieves details for a specific package.

## Setup

1.  **Prerequisites:**
    *   Python 3.x
    *   pip (Python package installer)

2.  **Installation:**
    ```bash
    pip install Flask
    ```

3.  **Data File:**
    Ensure the `packages.json` file exists at `/Users/ameerabbas/Documents/GCP/shiptrack/packages.json` and contains valid JSON data in the expected format.

## Running the Application

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/app.py
```
The application will start on `http://127.0.0.1:5000` by default.

## Running Tests

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/test_app.py
```
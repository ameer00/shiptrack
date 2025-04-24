# Package Management API - Flask Implementation

This Flask application provides an API endpoint to retrieve package details based on the OpenAPI specification (`shipping.yaml`). It reads package data from a local JSON file (`packages.json`).

## Features

*   **Get Package by ID:** Retrieve details for a specific package using its `packageId`.

## Setup

1.  **Prerequisites:**
    *   Python 3.x installed.
    *   Flask installed (`pip install Flask`).
2.  **Data File:** Ensure the `packages.json` file exists at `/Users/ameerabbas/Documents/GCP/shiptrack/packages.json` and contains package data in the expected format (an array of package objects).

## Running the Application

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/app.py
```
The application will start the development server, typically accessible at `http://127.0.0.1:5000`.

## Running Tests

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/test_app.py
```
# Package Information API

This is a simple Flask API to retrieve package information based on a `packageId`. It reads data from a local `packages.json` file.

## Features

*   GET `/packages/{packageId}`: Retrieves details for a specific package.

## Setup

1.  **Clone the repository (or ensure files are in the same directory):**
    Make sure `app.py`, `test_app.py`, and `packages.json` are in the `/Users/ameerabbas/Documents/GCP/shiptrack/` directory.

2.  **Install dependencies:**
    ```bash
    pip install Flask
    ```

## Running the Application

```bash
python /Users/ameerabbas/Documents/GCP/shiptrack/app.py
```
The API will be running at `http://127.0.0.1:5000`.

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
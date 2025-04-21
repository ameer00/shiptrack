# Package Information API

This is a simple Flask API to retrieve package information based on a `packageId`. It reads data from a local `packages.json` file.

## Features

*   GET `/packages/{packageId}`: Retrieves details for a specific package.

## Setup

1.  **Prerequisites:**
    *   Python 3.x
    *   pip (Python package installer)

2.  **Installation:**
    *   Clone this repository or download the files.
    *   Navigate to the project directory in your terminal.
    *   Install the required Python package:
        ```bash
        pip install Flask
        ```
    *   Ensure the `packages.json` file is in the same directory as `app.py`.

## Running the Application

```bash
python app.py
```
The API will be running at `http://127.0.0.1:5000`.

## Running Tests

```bash
python test_app.py
```

## Example Usage (using curl)

```bash
# Get package with ID '1'
curl http://127.0.0.1:5000/packages/1

# Get package with ID '10'
curl http://127.0.0.1:5000/packages/10

# Try getting a non-existent package
curl -i http://127.0.0.1:5000/packages/999
```
import unittest
import json
from app import app, load_packages # Import the Flask app and the loader function

class PackageApiTestCase(unittest.TestCase):
    """Test suite for the Package API endpoints."""

    def setUp(self):
        """Set up test client and load test data."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        # Ensure tests use the same data loading logic
        self.packages_data = load_packages()
        # Manually inject test data if needed, or ensure packages.json is correct
        # For isolated testing, you might want to mock load_packages
        # or provide a specific test JSON file.
        # Here, we rely on the actual packages.json being present.

    def test_get_existing_package(self):
        """Test retrieving an existing package."""
        # Assuming packageId '1' exists in packages.json
        response = self.client.get('/packages/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['packageId'], '1')
        self.assertEqual(data['product_id'], '1')
        self.assertEqual(data['height'], 10)
        # Add more assertions based on the expected data for packageId '1'
        self.assertEqual(data['special_handling_instructions'], 'Fragile')

    def test_get_another_existing_package(self):
        """Test retrieving another existing package."""
        # Assuming packageId '10' exists in packages.json
        response = self.client.get('/packages/10')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['packageId'], '10')
        self.assertEqual(data['product_id'], '10')
        self.assertEqual(data['weight'], 1)
        self.assertEqual(data['special_handling_instructions'], 'Semifragile')

    def test_get_nonexistent_package(self):
        """Test retrieving a package that does not exist."""
        response = self.client.get('/packages/999')
        self.assertEqual(response.status_code, 404)
        # Flask's default 404 response might be HTML or simple text
        # If you customize the 404 error handler to return JSON:
        # data = json.loads(response.data)
        # self.assertIn('message', data) # Or check for the specific error message
        self.assertIn(b"Package with ID '999' not found", response.data) # Check the description text

if __name__ == '__main__':
    unittest.main()
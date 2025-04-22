import unittest
import json
import os
from app import app, load_packages # Import the Flask app and data loading function

class PackageApiTestCase(unittest.TestCase):
    """Test suite for the Package API."""

    @classmethod
    def setUpClass(cls):
        """Load test data once for all tests."""
        # Construct the absolute path to the packages.json file relative to this test file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        cls.test_packages_path = os.path.join(base_dir, 'packages.json')
        # Ensure the app uses the same data for testing
        app.config['TEST_PACKAGES_DATA'] = load_packages(cls.test_packages_path)

    def setUp(self):
        """Set up the test client for each test."""
        self.app = app.test_client()
        self.app.testing = True
        # Override the app's data source with the test data
        # This is a simple way for this example; more complex apps might use mocking
        # or dependency injection. We'll reload it here for simplicity in this context.
        global packages_data
        packages_data = load_packages(self.test_packages_path)


    def test_get_existing_package(self):
        """Test retrieving an existing package by packageId."""
        response = self.app.get('/packages/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['packageId'], '1')
        self.assertEqual(data['product_id'], '1')
        self.assertEqual(data['special_handling_instructions'], 'Fragile')

    def test_get_non_existent_package(self):
        """Test retrieving a package that does not exist."""
        response = self.app.get('/packages/999')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data) # Flask abort(404) returns JSON error
        self.assertIn("Package with ID '999' not found", data['message'])


if __name__ == '__main__':
    unittest.main()
import unittest
import json
from app import app, load_packages, PACKAGES_FILE # Import your Flask app instance and functions

class PackageApiTestCase(unittest.TestCase):
    """Test suite for the Package API endpoints."""

    def setUp(self):
        """Set up test client and mock data before each test."""
        self.app = app.test_client()
        self.app.testing = True

        # Create a dummy packages.json for testing if it doesn't exist
        # or override existing one for controlled tests
        self.test_packages = [
            {
              "product_id": "1",
              "packageId": "1",
              "height": 10,
              "width": 5,
              "depth": 2,
              "weight": 1,
              "special_handling_instructions": "Fragile"
            },
            {
              "product_id": "2",
              "packageId": "2",
              "height": 8,
              "width": 6,
              "depth": 3,
              "weight": 2,
              "special_handling_instructions": "Antifragile"
            }
        ]
        # You might want to mock open() instead of writing a file in more complex scenarios
        with open(PACKAGES_FILE, 'w') as f:
            json.dump(self.test_packages, f)

    def test_get_package_success(self):
        """Test retrieving an existing package."""
        response = self.app.get('/packages/1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['packageId'], '1')
        self.assertEqual(data['special_handling_instructions'], 'Fragile')

    def test_get_package_not_found(self):
        """Test retrieving a non-existent package."""
        response = self.app.get('/packages/999')
        # Flask's abort(404, description=json_string) returns description in response.data
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['code'], 'NOT_FOUND')
        self.assertEqual(data['message'], 'Package with ID 999 not found.')

if __name__ == '__main__':
    unittest.main()
import unittest
import json
from app import app # Import the Flask app instance

class PackageApiTestCase(unittest.TestCase):
    """Test suite for the Package API."""

    def setUp(self):
        """Set up test client and other test variables."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        # Mock data similar to packages.json for testing purposes
        self.test_package_id_1 = "1"
        self.test_package_data_1 = {
            "height": 10,
            "width": 5,
            "depth": 2,
            "weight": 1,
            "special_handling_instructions": "Fragile"
        }
        self.non_existent_package_id = "999"

    def test_get_package_success(self):
        """Test retrieving an existing package."""
        response = self.client.get(f'/packages/{self.test_package_id_1}')
        self.assertEqual(response.status_code, 200)
        # Parse the JSON response data
        data = json.loads(response.data)
        # Assert that the returned data matches the expected subset
        self.assertEqual(data, self.test_package_data_1)

    def test_get_package_not_found(self):
        """Test retrieving a non-existent package."""
        response = self.client.get(f'/packages/{self.non_existent_package_id}')
        self.assertEqual(response.status_code, 404)
        # Parse the JSON error response
        data = json.loads(response.data)
        # Assert the structure of the error message
        self.assertIn('message', data)
        self.assertIn('code', data)
        self.assertEqual(data['code'], 'NOT_FOUND')
        self.assertIn(f"Package with ID {self.non_existent_package_id} not found", data['message'])

if __name__ == '__main__':
    unittest.main()
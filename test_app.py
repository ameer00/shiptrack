import unittest
import json
from app import app, load_packages, PACKAGES_FILE_PATH # Import the Flask app and helper functions

class PackageApiTestCase(unittest.TestCase):
    """Test suite for the Package API."""

    @classmethod
    def setUpClass(cls):
        """Load test data once for all tests."""
        # Load the actual data to compare against
        cls.packages_data = load_packages(PACKAGES_FILE_PATH)
        if not cls.packages_data:
            raise Exception(f"Could not load test data from {PACKAGES_FILE_PATH}")
        cls.test_package_1 = cls.packages_data[0] # Assuming packageId '1' is the first item

    def setUp(self):
        """Set up a test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_package_success(self):
        """Test retrieving an existing package."""
        package_id_to_test = self.test_package_1['packageId']
        response = self.app.get(f'/packages/{package_id_to_test}')
        data = json.loads(response.data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['packageId'], package_id_to_test)
        self.assertEqual(data['product_id'], self.test_package_1['product_id'])
        self.assertEqual(data['height'], self.test_package_1['height'])
        self.assertEqual(data['width'], self.test_package_1['width'])
        self.assertEqual(data['depth'], self.test_package_1['depth'])
        self.assertEqual(data['weight'], self.test_package_1['weight'])
        self.assertEqual(data['special_handling_instructions'], self.test_package_1['special_handling_instructions'])

    def test_get_package_not_found(self):
        """Test retrieving a non-existent package."""
        non_existent_id = "non_existent_package_id_999"
        response = self.app.get(f'/packages/{non_existent_id}')

        # Assertions
        self.assertEqual(response.status_code, 404)
        # Check if the response body contains the expected error message (Flask's default 404 JSON might vary)
        self.assertIn(b"not found", response.data.lower()) # Check for 'not found' in the response body

if __name__ == '__main__':
    unittest.main()
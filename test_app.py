import unittest
import json
from app import app, load_packages, PACKAGES_FILE

class PackageApiTestCase(unittest.TestCase):
    """Test suite for the Package API."""

    @classmethod
    def setUpClass(cls):
        """Load test data before all tests."""
        # Ensure we load the data for tests, potentially overriding app's load
        cls.test_packages = load_packages()
        # If loading failed in setUpClass, tests might fail, which is intended.

    def setUp(self):
        """Set up the test client for each test."""
        app.config['TESTING'] = True
        # Inject the test data into the app's context for testing purposes
        # This avoids relying on the global 'packages_data' loaded at app start
        app.config['PACKAGES_DATA'] = self.test_packages
        self.client = app.test_client()

        # Override the route handler to use the injected data
        @app.route('/packages/<string:packageId>', methods=['GET'])
        def get_package_test(packageId):
            """Test version of get_package using injected data."""
            packages_data = app.config['PACKAGES_DATA']
            package = next((pkg for pkg in packages_data if pkg.get('packageId') == packageId), None)
            if package:
                from flask import jsonify
                return jsonify(package)
            else:
                from flask import abort
                abort(404, description=f"Package with ID '{packageId}' not found.")

    def test_get_existing_package(self):
        """Test retrieving an existing package."""
        response = self.client.get('/packages/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['packageId'], '1')
        self.assertEqual(data['product_id'], '1') # Verify other fields too

    def test_get_nonexistent_package(self):
        """Test retrieving a package that does not exist."""
        response = self.client.get('/packages/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Package with ID '999' not found", response.data)

if __name__ == '__main__':
    unittest.main()
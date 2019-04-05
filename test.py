import os
import app
import json
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.testing = True
        self.app = app.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def test_add_fr_error_without_client(self):
        data = {
            "title": "New Request",
            "description": "New Request",
            "client_priority": 2,
            "target_date": "04/29/2019",
            "product_area": "Policies"
        }
        rv = self.app.post('/new',
                           data=json.dumps(data),
                           content_type='application/json')
        assert (rv.status_code == 406)

    def test_add_fr_error_without_title(self):
        data = {
            "description": "New Request",
            "client": 'Client A',
            "client_priority": 2,
            "target_date": "04/29/2019",
            "product_area": "Policies"
        }
        rv = self.app.post('/new',
                           data=json.dumps(data),
                           content_type='application/json')
        assert (rv.status_code == 406)

    def test_add_fr_error_without_description(self):
        data = {
            "title": "New Request",
            "client": 'Client A',
            "client_priority": 2,
            "target_date": "04/29/2019",
            "product_area": "Policies"
        }
        rv = self.app.post('/new',
                           data=json.dumps(data),
                           content_type='application/json')
        assert (rv.status_code == 406)

    def test_add_fr(self):
        data = {
            "title": "New Request #1",
            "description": "New Request",
            "client": 'Client A',
            "client_priority": 2,
            "target_date": "04/29/2019",
            "product_area": "Policies"
        }
        rv = self.app.post('/new',
                           data=json.dumps(data),
                           content_type='application/json')
        assert (rv.status_code == 200)


if __name__ == '__main__':
    unittest.main()

import unittest
import json
from app import app

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_rule(self):
        response = self.app.post('/create_rule', data=json.dumps({'rule': 'your_rule_string_here'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('rule_id', json.loads(response.data))

    def test_combine_rules(self):
        response = self.app.post('/combine_rules', data=json.dumps({'rule_ids': [1, 2]}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('combined_rule', json.loads(response.data))

    def test_evaluate_rule(self):
        response = self.app.post('/evaluate_rule', data=json.dumps({'rule_id': 1, 'data': {'temp': 30}}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()

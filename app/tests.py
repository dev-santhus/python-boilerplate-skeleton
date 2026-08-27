from django.test import TestCase


class HomeViewTests(TestCase):
    def test_home_returns_expected_template_greeting(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello from ${{ values.name }}")

from django.test import TestCase
from django.core.management import call_command
from .models import Date


class ApiViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'myproject_api/fixtures/test_data.json')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/dates/')
        self.assertEqual(response.status_code, 200)

    def test_lists_all_dates(self):
        response = self.client.get('/dates/')
        self.assertEqual(len(response.data), 6)

    def test_post_new_date(self):
        month, day = 5, 4
        response = self.client.post('/dates/', {'month': month, 'day': day})
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Date.objects.filter(month=month, day=day).exists())

    def test_remove_date_no_credentials(self):
        response = self.client.delete('/dates/3/')
        self.assertEqual(response.status_code, 403)

    def test_popular_dates(self):
        response = self.client.get('/popular/')
        ranking = [{'month': 'July', 'days_checked': 3},
                   {'month': 'November', 'days_checked': 2},
                   {'month': 'May', 'days_checked': 1}]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ranking)

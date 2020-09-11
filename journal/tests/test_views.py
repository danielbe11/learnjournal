from django.test import TestCase, Client
from django.urls import reverse
from journal.models import Resource
from datetime import datetime, date


class ViewResourcesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_resources = 10
        for resource_id in range(number_of_resources - 5):
            Resource.objects.create(name_text=f'Resource {resource_id}',
                                    # attachment=f'{resource_id}.pdf',
                                    link=f'http://www.{resource_id}.com',
                                    language='Python',
                                    framework='Django',
                                    notes=f'{resource_id}',
                                    post_date=datetime.now()
                                    )
        for resource_id in range(number_of_resources - 5, number_of_resources):
            Resource.objects.create(name_text=f'Resource {resource_id}',
                                    # attachment=f'{resource_id}.pdf',
                                    link=f'http://www.{resource_id}.com',
                                    # language='Python',
                                    # framework='Django',
                                    # notes=f'{resource_id}',
                                    post_date=datetime.now()
                                    )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('journal:view_resources'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('journal:view_resources'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journal/view_resources.html')

    def test_lists_all_resources(self):
        response = self.client.get(reverse('journal:view_resources'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['list_resources']), 10)

    # Test the search function

    def test_search_empty_query(self):
        response = self.client.get(reverse('journal:view_resources'), {'q': ''})
        self.assertEqual(len(response.context['list_resources']), 10)
        self.assertEqual(response.status_code, 200)

    def test_search_Python_query(self):
        response = self.client.get(reverse('journal:view_resources'), {'q': 'Python'})
        self.assertEqual(len(response.context['list_resources']), 5)
        self.assertEqual(response.status_code, 200)

    def test_search_name_query(self):
        response = self.client.get(reverse('journal:view_resources'), {'q': '1'})
        self.assertEqual(len(response.context['list_resources']), 1)
        self.assertEqual(response.status_code, 200)


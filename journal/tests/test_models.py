from django.test import TestCase
from journal.models import Resource
from datetime import datetime, date


class ResourceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Resource.objects.create(name_text='Google', link='https://www.google.co.uk', attachment=
                                'journal/attachments/ewkhdqqwsae0xpo_hwbzcot.jpeg', language='Python',
                                framework='Django', post_date=datetime.now())
    # Test labels

    def test_resource_name_label(self):
        resource = Resource.objects.get(pk=1)
        field_label = resource._meta.get_field('name_text').verbose_name
        self.assertEquals(field_label, 'Resource name')

    def test_link_label(self):
        resource = Resource.objects.get(pk=1)
        field_label = resource._meta.get_field('link').verbose_name
        self.assertEquals(field_label, 'Link')

    def test_attachment_label(self):
        resource = Resource.objects.get(pk=1)
        field_label = resource._meta.get_field('attachment').verbose_name
        self.assertEquals(field_label, 'Attachment')

    def test_language_label(self):
        resource = Resource.objects.get(pk=1)
        field_label = resource._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'Language')

    def test_framework_label(self):
        resource = Resource.objects.get(pk=1)
        field_label = resource._meta.get_field('framework').verbose_name
        self.assertEquals(field_label, 'Framework')

    def test_notes_label(self):
        resource = Resource.objects.get(pk=1)
        field_label = resource._meta.get_field('notes').verbose_name
        self.assertEquals(field_label, 'Notes')

    def test_post_date_label(self):
        resource = Resource.objects.get(pk=1)
        field_label = resource._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'Post date')

    # Test

    def test_str_representation(self):
        resource = Resource.objects.get(pk=1)
        self.assertEqual(resource.__str__(), resource.name_text)

    def test_post_date_populated(self):
        resource = Resource.objects.get(pk=1)
        self.assertIsNotNone(resource.post_date)


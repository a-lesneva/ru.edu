from django.test import TestCase
from django.urls import reverse, resolve

from ..views import SchoolListView

class TestSchoolsList(TestCase):

    def test_schools_opens_by_name(self):
        url = reverse('schools:schools')
        self.assertEquals(resolve(url).func.view_class, SchoolListView)

    def test_schools_status_code_by_name(self):
        response = self.client.get(reverse('schools:schools'))
        self.assertEquals(response.status_code, 200)

    def test_schools_opens_by_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_schools_uses_schools_template(self):
        response = self.client.get(reverse('schools:schools'))
        self.assertTemplateUsed(response, 'schools.html')
        


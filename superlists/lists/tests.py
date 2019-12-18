from django.test import TestCase
from django.urls.base import resolve
from .views import home_page

# Create your tests here.
# run command: python manage.py test lists.tests


class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


if __name__ == '__main__':
    TestCase.run()

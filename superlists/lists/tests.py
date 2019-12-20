from django.test import TestCase
from django.urls.base import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page

# Create your tests here.
# run command: python manage.py test lists.tests


class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 2)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_current_html(self):
        request = HttpRequest()
        response = home_page(request)
        # self.assertTrue(response.content.startswith(b'<html>'))  # 不要测试常量，应该测试实现的方法
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)   # decode()把content中的字节转换成Python中的Unicode字符串


if __name__ == '__main__':
    TestCase.run()

from django.test import TestCase
from django.urls.base import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page
from lists.models import Item

# Create your tests here.
# run command: python manage.py test lists.tests


class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 2)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # def test_home_page_return_current_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     # self.assertTrue(response.content.startswith(b'<html>'))  # 不要测试常量，应该测试实现的方法
    #     # self.assertIn(b'<title>To-Do lists</title>', response.content)
    #     # self.assertTrue(response.content.endswith(b'</html>'))
    #     expected_html = render_to_string('home.html')
    #     self.assertEqual(response.content.decode(), expected_html)   # decode()把content中的字节转换成Python中的Unicode字符串


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_save_item = saved_items[0]
        second_save_item = saved_items[1]
        self.assertEqual(first_save_item.text, 'The first (ever) list item')
        self.assertEqual(second_save_item.text, 'Item the second')


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the_only_list_in_the_world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_display_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the_only_list_in_the_world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

    def test_saving_a_post_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})   # 使用Django测试客户端重写

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the_only_list_in_the_world/')


if __name__ == '__main__':
    TestCase.run()

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
run command: python manage.py test functional_tests
'''

# HOST = 'http://localhost:8000'


class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)  # 隐式等待

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 撕葱听说了一个很酷的在线待办事项应用
        # 他去看了这个应用的首页
        self.browser.get(self.live_server_url)

        # 他注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请他输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 他在一个文本输入框中输入了“学习数据结构和算法”
        inputbox.send_keys('学习数据结构和算法')

        # 他按回车键后，被带到了一个新的URL
        # 待办事项表格中显示了“1: 学习数据结构和算法”
        inputbox.send_keys(Keys.ENTER)
        sicong_list_url = self.browser.current_url
        self.assertRegex(sicong_list_url, '/list/.+')
        self.check_for_row_in_list_table('1: 学习数据结构和算法')

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 他在文本输入框中输入了“趣谈Linux操作系统”
        # 撕葱做事很有规划
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('趣谈Linux操作系统')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，他的清单显示了这两个待办事项
        self.check_for_row_in_list_table('1: 学习数据结构和算法')
        self.check_for_row_in_list_table('2: 趣谈Linux操作系统')

        # 现在一个叫热狗的新用户访问了网站
        ## 确保撕葱的信息不会从cookie中泄露出来
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # 热狗访问首页，页面中看不到撕葱的的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('学习数据结构和算法', page_text)
        self.assertNotIn('趣谈Linux操作系统', page_text)

        # 热狗输入一个新待办事项，新建一个清单
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('霍霍霍霍霍')
        inputbox.send_keys(Keys.ENTER)

        # 热狗获取了他唯一的一个URL
        regou_lists_url = self.browser.current_url
        self.assertRegex(regou_lists_url, '/list/.+')
        self.assertNotEqual(sicong_list_url, regou_lists_url)

        # 这个页面也没有撕葱的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('学习数据结构和算法', page_text)
        self.assertIn('霍霍霍霍霍', page_text)

        # 他很满意，去rap了
        self.fail('finish the test!')

        # 他访问这个url，发现他的待办事项列表还在
        # 他很满意，去炫富了

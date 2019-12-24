from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

HOST = 'http://localhost:8000'


class NewVisitorTest(unittest.TestCase):

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
        self.browser.get(HOST)

        # 他注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请他输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 他在一个文本输入框中输入了“学习数据结构和算法”
        inputbox.send_keys('学习数据结构和算法')

        # 他按回车键后，页面更新了
        # 待办事项表格中显示了“1: 学习数据结构和算法”
        inputbox.send_keys(Keys.ENTER)

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 他在文本输入框中输入了“趣谈Linux操作系统”
        # 撕葱做事很有规划
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('趣谈Linux操作系统')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，他的清单显示了这两个待办事项
        self.check_for_row_in_list_table('1:学习数据结构和算法')
        self.check_for_row_in_list_table('2:趣谈Linux操作系统')
        self.fail('finish the test!')


        # 撕葱想知道网站是否会记住他的清单
        # 他看到网站为他生成了一个唯一的url
        # 而且页面中有一些文字解说这个功能

        # 他访问这个url，发现他的待办事项列表还在
        # 他很满意，去炫富了


if __name__ == '__main__':
    unittest.main()

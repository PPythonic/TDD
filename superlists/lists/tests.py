from django.test import TestCase

# Create your tests here.
# run command: python manage.py test lists.tests


class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 3)


if __name__ == '__main__':
    TestCase.run()

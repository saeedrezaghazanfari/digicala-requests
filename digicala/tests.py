import requests
from django.test import TestCase

class HomeTest(TestCase):

    def test_apple_url(self):
        req = requests.get('https://www.digikala.com/search/category-mobile-phone/apple/')
        assert req.status_code == 200

    def test_shampoo_url(self):
        req = requests.get('https://www.digikala.com/search/category-baby-shampoo/')
        assert req.status_code == 200
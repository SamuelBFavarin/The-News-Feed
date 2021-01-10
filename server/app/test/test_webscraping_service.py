import unittest
from datetime import datetime
import uuid

from app.main import db

from app.main.model.author import Author
from app.main.model.news import News

from app.main.services.webscraping_service import generate_valid_tag

from app.test.base import BaseTestCase


class TestWebScrapingService(BaseTestCase):

    def test_get_a_valid_tag(self):

        self.assertTrue(generate_valid_tag('politics') == 'POLITICS')
        self.assertTrue(generate_valid_tag('technology') == 'TECH')
        self.assertTrue(generate_valid_tag('science') == 'SCIENCE')
        self.assertTrue(generate_valid_tag('sport') == 'SPORTS')
        self.assertTrue(generate_valid_tag('business') == 'BUSINESS')


if __name__ == '__main__':
    unittest.main()

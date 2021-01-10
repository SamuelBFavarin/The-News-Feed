import unittest
from datetime import datetime
import uuid

from app.main import db

from app.main.model.author import Author
from app.main.model.news import News

from app.main.services.feed_service import save_news, list_news

from app.test.base import BaseTestCase


class TestFeedService(BaseTestCase):

    def test_save_news(self):

        # save a correct news
        news_data = {
            'title': 'the news title',
            'text': 'the news content text',
            'tag': 'SCIENCE',
            'photo': 'www.photo.com/thisisaphoto.jpg',
            'author_name': 'Samuel Brati Favarin',
            'author_photo': 'www.photo.com/thisisanotherphoto.jpg'
        }

        response, code = save_news(news_data)
        self.assertTrue(response['status'] == 'success')
        self.assertTrue(code == 200)

        # save a news with wrong tag
        news_data = {
            'title': 'the news title',
            'text': 'the news content text',
            'tag': 'WRONG',
            'photo': 'www.photo.com/thisisaphoto.jpg',
            'author_name': 'Samuel Brati Favarin',
            'author_photo': 'www.photo.com/thisisanotherphoto.jpg'
        }

        response, code = save_news(news_data)
        self.assertTrue(response['status'] == 'error')
        self.assertTrue(code == 400)

        # save a news missing require attributes
        news_data = {
            'tag': 'WRONG',
            'photo': 'www.photo.com/thisisaphoto.jpg',
            'author_photo': 'www.photo.com/thisisanotherphoto.jpg'
        }

        response, code = save_news(news_data)
        self.assertTrue(response['status'] == 'error')
        self.assertTrue(code == 400)

    def test_list_news(self):
        self.__create_mock_data()

        # list all news
        result = list_news()
        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0]['title'] == self.news_data2['title'])
        self.assertTrue(result[1]['title'] == self.news_data1['title'])

        # list news with politics tag
        result = list_news(tag='POLITICS')
        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0]['title'] == self.news_data2['title'])

        # filter news with science tag (response must have nothing news)
        result = list_news(tag='SCIENCE')
        self.assertTrue(len(result) == 0)

        # filter with wrong tag
        result = list_news(tag='WRONG')
        self.assertTrue(len(result) == 0)

    def __create_mock_data(self):

        new_author = Author(
            public_id=str(uuid.uuid4()),
            name='samuelbfavarin37',
            photo='https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            created_at=datetime.utcnow())

        db.session.add(new_author)
        db.session.commit()

        self.author_entity_id = new_author.id

        self.news_data1 = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': 'this is a title',
            'text': 'this is as text',
            'tag': 'TECH',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.news_data2 = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': 'this is a title2',
            'text': 'this is as text2',
            'tag': 'POLITICS',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.__create_news_entities(self.news_data1)
        self.__create_news_entities(self.news_data2)

    def __create_news_entities(self, news):

        try:
            new_news = News(
                public_id=news['public_id'],
                author_id=news['author_id'],
                title=news['title'],
                text=news['text'],
                photo=news['photo'],
                tag=news['tag'],
                created_at=news['created_at']
            )

            db.session.add(new_news)
            db.session.commit()
            return new_news
        except:
            return False


if __name__ == '__main__':
    unittest.main()

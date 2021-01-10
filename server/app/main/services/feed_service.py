import uuid
import datetime

from app.main import db

import app.main.services.author_service as Author
import app.main.services.news_service as News


def save_news(data):
    """ 
        Save news at database.

        Parameters
        ----------
        data : dict
            The data to save a entity. The dict must have this structure:
            {
                'title': 'the news title',
                'text': 'the news content text',
                'tag': 'the news tag' (the value must be 'POLITICS', 'TECH', 'SCIENCE', 'SPORTS' or 'BUSINESS'),
                'photo': 'the news url photo' (optional),
                'author_name': 'the name of author',
                'author_photo': 'the author url photo (optional)'
            } 

    """

    if __validate_require_attributes(data) == False:
        response_object = {
            'status': 'error',
            'message': 'You must send all requires attributes'
        }

        return response_object, 400

    author = Author.get_author(data['author_name'])

    if not author:

        author_name = data['author_name']
        author_photo = None
        if 'author_photo' in data:
            author_photo = data['author_photo']

        author = Author.create_author(
            {'name': author_name, 'photo': author_photo})

    try:
        News.create_news(data, author.id)
        response_object = {
            'status': 'success',
            'message': 'News Successfully created.'
        }

        return response_object, 200

    except:
        response_object = {
            'status': 'error',
            'message': 'Error on create the news.'
        }

        return response_object, 400


def list_news(tag=None):
    """ 
        List all news, with author data
    """
    data = News.list_news(tag_filter=tag)
    return data


def __validate_require_attributes(attributes_received):
    required_attributes = ['title', 'text', 'tag', 'author_name']
    for attribute in required_attributes:
        if attribute not in attributes_received:
            return False

    return True

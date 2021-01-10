from ..util.decorator import token_required
import urllib.request as request
from bs4 import BeautifulSoup
import json

from app.main.services.feed_service import save_news
from app.main.services.news_service import get_news

from app.main.config import the_guardian_api_key


def generate_news():
    """
        Generate News by https://www.theguardian.com/,
        you must define a valid `guardianapis.com` API_KEY in config.py file

    """

    count_errors = 0
    count_success = 0
    count_repeated = 0

    tags = ['politics',
            'science',
            'technology',
            'sport',
            'business']

    for tag in tags:
        news = __get_news(tag)
        for item in news:

            if (get_news(item['title']) == None):
                try:
                    save_news(item)
                    count_success += 1
                except:
                    count_errors += 1

            else:
                count_repeated += 1

    response_object = {
        'status': 'success',
        'news_created': count_success,
        'news_error': count_errors,
        'news_repeated': count_repeated,
        'message': str(count_success) + ' news created with success, ' + str(count_errors) + ' news errors, and ' + str(count_repeated) + ' news not created because already exists'
    }

    return response_object, 200


def __get_news(tag, max=2):
    """
        Generate News by TAG using https://www.theguardian.com/

        Parameters
        ----------
        tag : str
            The tag to filter news, you must send a valid tag like:
                - politics
                - science
                - technology
                - sport
                - business

        max : int
            The max news to get. The max value can be 10

    """
    API_KEY = the_guardian_api_key

    news = []

    news_urls = __get_news_URL(tag, API_KEY)

    if news_urls:
        for url in news_urls[0:max]:
            result = __get_news_info(url, tag, API_KEY)
            if result:
                news.append(result)

    return news


def __get_news_URL(tag, key):
    """
        Get the news urls

        Parameters
        ----------
        tag : str
            The tag to filter news, you must send a valid tag like:
                - politics
                - science
                - technology
                - sport
                - business

        key : str
            A valid `guardianapis.com` API KEY

    """

    try:
        url = "https://content.guardianapis.com/search?section="+tag+"&api-key=" + key
        res = request.urlopen(url).read().decode("utf-8")
        news_basic_data = json.loads(res)
        return [i['apiUrl'] for i in news_basic_data['response']['results']]

    except:
        return False


def __get_news_info(url, tag, key):
    """
        Get the news info by news url

        Parameters
        ----------
        url : str
            The news url

        tag : str
            The tag to filter news, you must send a valid tag like:
                - politics
                - science
                - technology
                - sport
                - business

        key : str
            A valid `guardianapis.com` API KEY

    """

    # get news
    news_url = url + "?api-key=" + key + \
        "&show-fields=bodyText,thumbnail,byline,bylineHtml"
    res = request.urlopen(news_url).read().decode("utf-8")
    news_info = json.loads(res)

    # get required infos
    item = {}
    try:
        item['title'] = news_info['response']['content']['webTitle']
        item['text'] = news_info['response']['content']['fields']['bodyText']
        item['author_name'] = news_info['response']['content']['fields']['byline']
        item['tag'] = generate_valid_tag(tag)
    except:
        return False

    # validate required item size
    if len(item['title']) == 0 or len(item['text']) == 0:
        return False

    # get the photo
    try:
        item['photo'] = news_info['response']['content']['fields']['thumbnail']
    except:
        pass

    # get author photo
    author_photo = __get_author_photo(
        news_info['response']['content']['fields']['bylineHtml'])
    if author_photo:
        item['author_photo'] = author_photo

    return item


def __get_author_photo(authorHTML):
    """
        Get author image by author HTML

        Parameters
        ----------
        authorHTMLrl : str
            The author HTML
    """

    try:
        author_url = "https://www.theguardian.com/" + authorHTML.split('"')[1]
        res = request.urlopen(author_url).read()
        soup = BeautifulSoup(res, 'html.parser')
        author_photo = soup.findAll(
            "img", {"class": "index-page-header__image"})[0]["src"]

        return author_photo

    except:
        return False


def generate_valid_tag(tag):
    """
        Generate a valid tag name based in model/news.py

        Parameters
        ----------
        tag : str
            The tag to filter news, you must send a valid tag like:
                - politics
                - science
                - technology
                - sport
                - business
    """

    if tag == 'sport':
        tag = 'sports'

    elif tag == 'technology':
        tag = 'tech'

    return tag.upper()

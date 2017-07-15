#!venv/bin/python
import requests

from flaskbook.orm.models import *


def _go():
    User.query.delete()
    Story.query.delete()
    Category.query.delete()
    db.session.commit()
    print('Dropped all rows from the database')

    db.session.add_all(_dummy_stories)
    db.session.commit()
    print('Added %i dummy stories to the database' % len(_dummy_stories))


def _create_dummy_story(template: dict) -> Story:
    story = Story()
    story.title = template['title']
    story.flavour_text = template['flavour']
    story.fulltext_html = template['fulltext']
    story.author = template['author']
    story.category = template['category']
    return story


def _lorem_ipsum(paras: int) -> str:
    url = 'https://www.baconipsum.com/api/?paras=%i&format=%s&type=%s&start-with-lorem=%i'
    url = url % (paras, 'text', 'meat-and-filler', 1)
    response = requests.get(url)
    return response.text if (response.status_code == 200) else None


_dummy_users = [User(nickname='Test 1'),
                User(nickname='Test 2'),
                User(nickname='Test 3'),
                User(nickname='This test user has an extra long name for testing purposes')]

_dummy_categories = [Category(name='Test 1'),
                     Category(name='Test 2'),
                     Category(name='Test 3'),
                     Category(name='This test category has an extra long name for testing purposes')]

_stories = [{
    'title': 'Test Story 1',
    'flavour': 'This test story is vanilla flavoured.',
    'fulltext': _lorem_ipsum(3),
    'author': _dummy_users[0],
    'category': _dummy_categories[0]
}, {
    'title': 'Test Story 2',
    'flavour': 'This test story is chocolate flavoured.',
    'fulltext': _lorem_ipsum(3),
    'author': _dummy_users[0],
    'category': _dummy_categories[0]
}, {
    'title': 'Test Story 3',
    'flavour': 'This test story is strawberry flavoured.',
    'fulltext': _lorem_ipsum(3),
    'author': _dummy_users[1],
    'category': _dummy_categories[1]
}, {
    'title': None,
    'flavour': None,
    'fulltext': None,
    'author': None,
    'category': None
}, {
    'title': 'Mostly Empty',
    'flavour': 'This story is empty except for the title and the flavour text.',
    'fulltext': None,
    'author': None,
    'category': None
}, {
    'title': 'This test story has a very long title and some very long flavour text and was written by an author with '
             'a very long nickname and is part of a category which has a very long name in order to allow for more '
             'thorough dev testing',
    'flavour': _lorem_ipsum(1),
    'fulltext': _lorem_ipsum(20),
    'author': _dummy_users[3],
    'category': _dummy_categories[3]
}]

_dummy_stories = [_create_dummy_story(story) for story in _stories]

_go()

#!venv/bin/python
import requests

from flaskbook.orm.models import *


def _drop_all_data():
    User.query.delete()
    Story.query.delete()
    Category.query.delete()
    db.session.commit()
    print('Dropped all rows from the database')


def _create_dummy_category(template: dict) -> Category:
    category = Category()
    category.name = template['name']
    db.session.add(category)
    db.session.commit()
    return category


def _create_dummy_user(template: dict) -> User:
    user = User()
    user.nickname = template['name']
    db.session.add(user)
    db.session.commit()
    return user


def _create_dummy_story(template: dict) -> Story:
    story = Story()
    story.title = template['title']
    story.flavour_text = template['flavour']
    story.fulltext_html = template['fulltext']
    story.author = template['author']
    story.category = template['category']
    db.session.add(story)
    db.session.commit()
    return story


def _lorem_ipsum(paras: int, as_html: bool = True) -> str:
    url = 'https://www.baconipsum.com/api/?paras=%i&format=%s&type=%s&start-with-lorem=%i'
    url = url % (paras, 'text', 'meat-and-filler', 1)
    print('Requesting: %s' % url)
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        if as_html:
            text = text.replace('\n\n', '<p></p>')
            text = text.replace('\n', '<br>')
        return text
    return None


_drop_all_data()

_categories = [{'name': 'Test 1'},
               {'name': 'Test 2'},
               {'name': 'Test 3'},
               {'name': 'This test category has an extra long name for testing purposes'}]
_dummy_categories = [_create_dummy_category(category) for category in _categories]

_users = [{'name': 'Test 1'},
          {'name': 'Test 2'},
          {'name': 'Test 3'},
          {'name': 'This test user has an extra long name for testing purposes'}]
_dummy_users = [_create_dummy_user(user) for user in _users]

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
    'flavour': _lorem_ipsum(1, as_html=False),
    'fulltext': _lorem_ipsum(20),
    'author': _dummy_users[3],
    'category': _dummy_categories[3]
}]
_dummy_stories = [_create_dummy_story(story) for story in _stories]

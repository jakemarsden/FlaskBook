#!venv/bin/python
from typing import Optional

import lorem
from sqlalchemy.orm.properties import RelationshipProperty
from sqlalchemy_imageattach.context import store_context

from flaskbook import db, image_store
from flaskbook.orm.models import Album, AlbumEntry, AlbumImage, Category, User, UserAvatar, Story, StoryCover


def _drop_all_data():
    print('Dropping all rows')
    Album.query.delete()
    AlbumEntry.query.delete()
    AlbumImage.query.delete()
    Category.query.delete()
    User.query.delete()
    UserAvatar.query.delete()
    Story.query.delete()
    StoryCover.query.delete()
    db.session.commit()


def _create_dummy_category(template: dict) -> Category:
    print('Adding category: %r' % template)
    category = Category(name=template['name'])
    db.session.add(category)
    db.session.commit()
    return category


def _create_dummy_user(template: dict) -> User:
    print('Adding user: %r' % template)
    user = User(nickname=template['name'])
    with store_context(image_store):
        _set_image(template['avatar'], user.avatar)
        db.session.add(user)
        db.session.commit()
    return user


def _create_dummy_album(template: dict) -> Album:
    print('Adding album: %r' % template)
    album = Album(title=template['title'],
                  author=template['author'],
                  category=template['category'])
    with store_context(image_store):
        for idx, entry_template in enumerate(template['entries']):
            entry = AlbumEntry(order=(idx + 1),
                               caption=entry_template['caption'])
            _set_image(entry_template['image'], entry.image)
            album.entries.append(entry)
        db.session.add(album)
        db.session.commit()
    return album


def _create_dummy_story(template: dict) -> Story:
    print('Adding story: %r' % template)
    story = Story(title=template['title'],
                  flavour_text=template['flavour'],
                  fulltext_html=template['fulltext'],
                  author=template['author'],
                  category=template['category'])
    with store_context(image_store):
        _set_image(template['cover'], story.cover)
        db.session.add(story)
        db.session.commit()
    return story


def _set_image(file_path: Optional[str], field: RelationshipProperty):
    if file_path is not None:
        field.from_file(open(file_path, 'rb'))


def _lorem_ipsum(paras: int, as_html: bool = True) -> Optional[str]:
    paras = [lorem.paragraph() for i in range(0, paras)]
    return ('<p></p>' if as_html else '\n\n').join(paras)


_drop_all_data()

_categories = [{'name': 'Test 1'},
               {'name': 'Test 2'},
               {'name': 'Test 3'},
               {'name': 'This test category has an extra long name for testing purposes'}]
_dummy_categories = [_create_dummy_category(category) for category in _categories]

_users = [{'name': 'Test 1', 'avatar': None},
          {'name': 'Test 2', 'avatar': None},
          {'name': 'Test 3', 'avatar': None},
          {'name': 'This test user has an extra long name for testing purposes', 'avatar': 'dummy_user_avatar.png'}]
_dummy_users = [_create_dummy_user(user) for user in _users]

_albums = [{'title': 'Test Album 1',
            'author': _dummy_users[0],
            'category': _dummy_categories[0],
            'entries': [{'caption': 'Test 1', 'image': 'dummy_album_image.png'},
                        {'caption': 'Test 2', 'image': 'dummy_album_image.png'},
                        {'caption': 'Test 3', 'image': 'dummy_album_image.png'}]},
           {'title': 'Mostly Empty',
            'author': None,
            'category': None,
            'entries': []},
           {'title': None,
            'author': None,
            'category': None,
            'entries': []},
           {'title': 'This test album has a very long title and contains lots of images with very long captions and '
                     'was written by an author with a very long nickname and is part of a category which has a very '
                     'long name in order to allow for more thorough dev testing',
            'author': _dummy_users[3],
            'category': _dummy_categories[3],
            'entries': [{'caption': _lorem_ipsum(1, as_html=False), 'image': 'dummy_album_image.png'},
                        {'caption': _lorem_ipsum(1, as_html=False), 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': _lorem_ipsum(1, as_html=False), 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'},
                        {'caption': None, 'image': 'dummy_album_image.png'}]}]
_dummy_albums = [_create_dummy_album(album) for album in _albums]

_stories = [{'title': 'Test Story 1',
             'flavour': 'This test story is vanilla flavoured.',
             'fulltext': _lorem_ipsum(3),
             'author': _dummy_users[0],
             'category': _dummy_categories[0],
             'cover': 'dummy_story_cover.png'},
            {'title': 'Test Story 2',
             'flavour': 'This test story is chocolate flavoured.',
             'fulltext': _lorem_ipsum(3),
             'author': _dummy_users[0],
             'category': _dummy_categories[0],
             'cover': 'dummy_story_cover.png'},
            {'title': 'Test Story 3',
             'flavour': 'This test story is strawberry flavoured.',
             'fulltext': _lorem_ipsum(3),
             'author': _dummy_users[1],
             'category': _dummy_categories[1],
             'cover': 'dummy_story_cover.png'},
            {'title': None,
             'flavour': None,
             'fulltext': None,
             'author': None,
             'category': None,
             'cover': None},
            {'title': 'Mostly Empty',
             'flavour': 'This story is empty except for the title and the flavour text.',
             'fulltext': None,
             'author': None,
             'category': None,
             'cover': None},
            {'title': 'This test story has a very long title and some very long flavour text and was written by an '
                      'author with a very long nickname and is part of a category which has a very long name in order '
                      'to allow for more thorough dev testing',
             'flavour': _lorem_ipsum(1, as_html=False),
             'fulltext': _lorem_ipsum(20),
             'author': _dummy_users[3],
             'category': _dummy_categories[3],
             'cover': 'dummy_story_cover.png'}]
_dummy_stories = [_create_dummy_story(story) for story in _stories]

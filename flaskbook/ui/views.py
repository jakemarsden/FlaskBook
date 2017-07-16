from flask import flash, redirect
from sqlalchemy.sql import collate

from flaskbook import app
from flaskbook.orm.models import Album, Category, Story
from flaskbook.ui.ui import MenuItem, Page, render


@app.route('/')
@app.route('/index')
def get_index():
    return render('index.html', Page())


@app.route('/albums/<int:album_id>')
def get_album_by_id(album_id: int):
    album = (Album.query
             .filter(Album.id == album_id)
             .one_or_none())
    if album is None:
        flash('No album found with the specified ID: %i' % album_id)
        return redirect('/albums')
    return render('album_fulltext.html', _page(), album=album)


@app.route('/stories')
def get_stories():
    stories = (Story.query
               .order_by(collate(Story.title, 'NOCASE'))
               .all())
    if len(stories) == 0:
        flash('No stories found')
    return render('story_list.html', _page(), stories=stories)


@app.route('/stories/<int:story_id>')
def get_story_by_id(story_id: int):
    story = (Story.query
             .filter(Story.id == story_id)
             .one_or_none())
    if story is None:
        flash('No story found with the specified ID: %i' % story_id)
        return redirect('/stories')
    return render('story_fulltext.html', _page(), story=story)


def _page():
    categories = (Category.query
                  .order_by(collate(Category.name, 'NOCASE'))
                  .all())
    menu_items = [MenuItem(category.name, '/category/%r' % category.id) for category in categories]
    return Page(menu_items)

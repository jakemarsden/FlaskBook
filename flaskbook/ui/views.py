from flask import flash, redirect
from sqlalchemy.sql import collate

from flaskbook import app
from flaskbook.orm.models import Category, Story
from flaskbook.ui.ui import MenuItem, Page, render


@app.route('/')
@app.route('/index')
def get_index():
    return render('index.html', Page())


@app.route('/stories')
def get_stories():
    stories = (Story.query
               .order_by(collate(Story.title, 'NOCASE'))
               .all())
    if len(stories) == 0:
        flash('No stories found')
    return render('story_list.html', _stories_page(), stories=stories)


@app.route('/stories/<int:story_id>')
def get_story_by_id(story_id: int):
    story = (Story.query
             .filter(Story.id == story_id)
             .one_or_none())
    if story is None:
        flash('No story found with the specified ID: %i' % story_id)
        return redirect('/stories')
    return render('story_fulltext.html', _stories_page(), story=story)


def _stories_page():
    categories = (Category.query
                  .order_by(collate(Category.name, 'NOCASE'))
                  .all())
    menu_items = [MenuItem(category.name, '/category/%r' % category.id) for category in categories]
    return Page(menu_items)

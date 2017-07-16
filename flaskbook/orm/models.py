from typing import Optional

from sqlalchemy_imageattach import entity
from sqlalchemy_imageattach.context import store_context

from flaskbook import db, image_store


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, unique=True, nullable=False)

    avatar = entity.image_attachment('UserAvatar')
    stories = db.relationship('Story', back_populates='author')

    @property
    def avatar_url(self) -> Optional[str]:
        with store_context(image_store):
            try:
                return self.avatar.locate()
            except IOError:
                pass
        return None

    def __repr__(self):
        return '<User: %r>' % self.nickname


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String)
    flavour_text = db.Column(db.String)
    fulltext_html = db.Column(db.String)

    cover = entity.image_attachment('StoryCover')
    author = db.relationship('User', back_populates='stories')
    category = db.relationship('Category', back_populates='stories')

    @property
    def cover_url(self) -> Optional[str]:
        with store_context(image_store):
            try:
                return self.cover.locate()
            except IOError:
                pass
        return None

    def __repr__(self):
        return '<Story: %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    stories = db.relationship('Story', back_populates='category')

    def __repr__(self):
        return '<Category: %r>' % self.name


class UserAvatar(db.Model, entity.Image):
    __tablename__ = 'user_avatar'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, unique=True)

    def __repr__(self):
        return '<UserAvatar: %r>' % self.user_id


class StoryCover(db.Model, entity.Image):
    __tablename__ = 'story_cover'
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), primary_key=True, unique=True)

    def __repr__(self):
        return '<StoryCover: %r>' % self.story_id

from typing import Optional

from sqlalchemy_imageattach import entity
from sqlalchemy_imageattach.context import store_context

from flaskbook import db, image_store


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Source: %r>' % self.url


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), unique=True, nullable=False)
    nickname = db.Column(db.String, unique=True, nullable=False)

    source = db.relationship('Source')
    avatar = entity.image_attachment('UserAvatar')
    albums = db.relationship('Album', back_populates='author')
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


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String)

    source = db.relationship('Source')
    author = db.relationship('User', back_populates='albums')
    category = db.relationship('Category', back_populates='albums')
    entries = db.relationship('AlbumEntry', back_populates='album', order_by='AlbumEntry.order')

    @property
    def first_entry(self) -> Optional['AlbumEntry']:
        if len(self.entries) != 0:
            return self.entries[0]
        return None

    @property
    def first_entry_url(self) -> Optional[str]:
        entry = self.first_entry
        if entry is not None:
            return entry.image_url
        return None

    def __repr__(self):
        return '<Album: %r>' % self.title


class AlbumEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    caption = db.Column(db.String)

    album = db.relationship('Album', back_populates='entries')
    image = entity.image_attachment('AlbumImage')

    @property
    def image_url(self) -> Optional[str]:
        with store_context(image_store):
            try:
                return self.image.locate()
            except IOError:
                pass
        return None

    def __repr__(self):
        return '<AlbumEntry: %r>' % self.caption


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String)
    flavour_text = db.Column(db.String)
    fulltext_html = db.Column(db.String)

    source = db.relationship('Source')
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

    albums = db.relationship('Album', back_populates='category')
    stories = db.relationship('Story', back_populates='category')

    def __repr__(self):
        return '<Category: %r>' % self.name


class UserAvatar(db.Model, entity.Image):
    __tablename__ = 'user_avatar'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, unique=True)

    def __repr__(self):
        return '<UserAvatar: %r>' % self.user_id


class AlbumImage(db.Model, entity.Image):
    __tablename__ = 'album_image'
    entry_id = db.Column(db.Integer, db.ForeignKey('album_entry.id'), primary_key=True, unique=True)

    def __repr__(self):
        return '<AlbumImage: %r>' % self.entry_id


class StoryCover(db.Model, entity.Image):
    __tablename__ = 'story_cover'
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), primary_key=True, unique=True)

    def __repr__(self):
        return '<StoryCover: %r>' % self.story_id

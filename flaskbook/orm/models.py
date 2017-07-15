from flaskbook import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, unique=True, nullable=False)

    stories = db.relationship('Story', back_populates='author')

    def __repr__(self):
        return '<User: %r>' % self.nickname


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String)
    flavour_text = db.Column(db.String)
    fulltext_html = db.Column(db.String)

    author = db.relationship('User', back_populates='stories')
    category = db.relationship('Category', back_populates='stories')

    def __repr__(self):
        return '<Story: %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    stories = db.relationship('Story', back_populates='category')

    def __repr__(self):
        return '<Category: %r>' % self.name

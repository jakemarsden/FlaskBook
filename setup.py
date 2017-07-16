from setuptools import setup

setup(
    name='FlaskBook',
    packages=['flaskbook'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'lorem',
        'SQLAlchemy-ImageAttach',
        'sqlalchemy-migrate'
    ]
)

import os

from setuptools import setup


def read(file_name):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    return open(file_path, 'rt').read()


setup(
    name='FlaskBook',
    version='0.0.1',
    author='Jake Marsden',
    author_email='jakemarsdenjm@gmail.com',
    url='https://github.com/jakemarsden/FlaskBook',
    long_description=read('README.md'),
    license='GNU GPLv3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],

    packages=['flaskbook'],
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'lorem',
        'SQLAlchemy-ImageAttach',
        'sqlalchemy-migrate'
    ]
)

from typing import List

from flask import render_template


def render(template_name: str, page: 'Page', **kwargs):
    if page is None:
        raise TypeError
    return render_template(template_name, page=page, **kwargs)


class Page:
    def __init__(self, menu_items: List['MenuItem'] = None):
        if menu_items is None:
            menu_items = []
        self.menu_items = menu_items


class MenuItem:
    def __init__(self, name: str, href: str):
        self.name = name
        self.href = href

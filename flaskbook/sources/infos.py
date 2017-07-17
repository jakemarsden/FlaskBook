from datetime import datetime
from typing import List


class Info:
    def __init__(self, source_url=None, retrieval_timestamp=None):
        self.source_url: str = source_url
        self.retrieval_timestamp: datetime = retrieval_timestamp


class UserInfo(Info):
    def __init__(self, source_url=None, retrieval_timestamp=None, nickname=None, avatar_url=None):
        super().__init__(source_url, retrieval_timestamp)
        self.nickname: str = nickname
        self.avatar_url: str = avatar_url


class AlbumInfo(Info):
    def __init__(self, source_url=None, retrieval_timestamp=None, title=None, author_url=None, category_name=None,
                 entries=None):
        super().__init__(source_url, retrieval_timestamp)
        if entries is None:
            entries = []
        self.title: str = title
        self.author_url: str = author_url
        self.category_name: str = category_name
        self.entries: List[AlbumEntryInfo] = entries


class AlbumEntryInfo:
    def __init__(self, caption=None, image_url=None):
        self.caption: str = caption
        self.image_url: str = image_url


class StoryInfo(Info):
    def __init__(self, source_url=None, retrieval_timestamp=None, title=None, flavour_text=None, fulltext_html=None,
                 author_url=None, category_name=None, cover_url=None):
        super().__init__(source_url, retrieval_timestamp)
        self.title: str = title
        self.flavour_text: str = flavour_text
        self.fulltext_html: str = fulltext_html
        self.author_url: str = author_url
        self.category_name: str = category_name
        self.cover_url: str = cover_url

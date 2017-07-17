from flaskbook.sources.infos import AlbumInfo, StoryInfo, UserInfo


class InfoSource:
    def get_user_info(self, url: str) -> UserInfo:
        raise NotImplementedError

    def get_album_info(self, url: str) -> AlbumInfo:
        raise NotImplementedError

    def get_story_info(self, url: str) -> StoryInfo:
        raise NotImplementedError

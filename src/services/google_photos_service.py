import logging
from utils.google_photos import init_photos_library


class GooglePhotosService:
    def __init__(
        self,
    ):
        self.logger = logging.getLogger('google_photos_helper')
        self.photos_library = init_photos_library()

    def scan(
        self,
        is_shared: bool,
        is_in_album: bool,
    ):
        self.logger.debug('Scanning media items')
        media_items = []
        next_page_token = None

        while True:
            results = self.photos_library.mediaItems().list(pageSize=100, pageToken=next_page_token).execute()
            items = results.get('mediaItems', [])
            media_items.extend(items)
            next_page_token = results.get('nextPageToken')

            if not next_page_token:
                break

        return media_items

    # def list_album_media_ids(self, service):
    #     album_media_ids = set()
    #     next_page_token = None

    #     while True:
    #         albums = service.albums().list(pageSize=50, pageToken=next_page_token).execute()
    #         for album in albums.get('albums', []):
    #             album_id = album['id']
    #             media_page_token = None
    #             while True:
    #                 album_items = service.mediaItems().search(body={
    #                     'albumId': album_id,
    #                     'pageSize': 100,
    #                     'pageToken': media_page_token
    #                 }).execute()
    #                 for item in album_items.get('mediaItems', []):
    #                     album_media_ids.add(item['id'])
    #                 media_page_token = album_items.get('nextPageToken')
    #                 if not media_page_token:
    #                     break

    #         next_page_token = albums.get('nextPageToken')

    #         if not next_page_token:
    #             break

    #     return album_media_ids

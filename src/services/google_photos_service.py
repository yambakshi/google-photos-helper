import os
import logging
from utils.google_photos import init_photos_library


class GooglePhotosService:
    def __init__(
        self,
        cache_service
    ):
        self.logger = logging.getLogger('google_photos_helper')
        self.init_photos_library = init_photos_library()
        self.cache_service = cache_service

    def scan(
        self,
        is_shared: bool,
        is_in_album: bool,
        is_load_cache: bool,
    ):
        if is_load_cache and os.path.isfile(f'caches/google-photos.cache'):
            self.logger.debug('Loading photos from cache')
        else:
            self.logger.debug('Scanning photos')
            photos = []
            self.cache_service.save(photos)

    # def list_all_media(self, service):
    #     media_items = []
    #     next_page_token = None

    #     while True:
    #         results = service.mediaItems().list(pageSize=100, pageToken=next_page_token).execute()
    #         items = results.get('mediaItems', [])
    #         media_items.extend(items)
    #         next_page_token = results.get('nextPageToken')
    #         if not next_page_token:
    #             break

    #     return media_items

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

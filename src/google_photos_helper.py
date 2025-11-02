from utils.logger import init_logger
from services.cache_service import CacheService
from services.google_photos_service import GooglePhotosService

class GooglePhotosHelper:
    def __init__(self):
        self.logger = init_logger()

        self.is_load_cache = False
        self.cache_service = CacheService()
        self.google_photos_service = GooglePhotosService()

    def delete_media_items(
        self,
        is_shared=False,
        is_in_album=False,
    ):
        try:
            self.logger.debug('Deleting media items')
            media_items_to_delete = []

            if self.is_load_cache:
                self.logger.debug('Loading media items from cache')
                media_items_to_delete = self.cache_service.read('caches/media-items.cache')
            else:
                media_items_to_delete = self.google_photos_service.scan(
                    is_shared=is_shared,
                    is_in_album=is_in_album,
                )

                self.cache_service.save(media_items_to_delete)

        except Exception as error:
            self.logger.exception(error)

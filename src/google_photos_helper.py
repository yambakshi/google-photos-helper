from utils.logger import init_logger
from services.cache_service import CacheService
from services.google_photos_service import GooglePhotosService

class GooglePhotosHelper:
    def __init__(self):
        self.logger = init_logger()

        self.is_load_cache = False
        self.cache_service = CacheService()
        self.google_photos_service = GooglePhotosService(
            cache_service=self.cache_service
        )

    def delete_photos(
        self,
        is_shared=False,
        is_in_album=False,
    ):
        try:
            self.logger.debug('Deleting photos')
            photos_to_delete = self.google_photos_service.scan(
                is_shared=is_shared,
                is_in_album=is_in_album,
                is_load_cache=self.is_load_cache
            )

            if not self.is_load_cache:
                self.cache_service.save(photos_to_delete)

        except Exception as error:
            self.logger.exception(error)

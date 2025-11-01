import logging
from services.file_io_service import FileIOService


class CacheService(FileIOService):
    def __init__(
        self,
    ):
        self.logger = logging.getLogger('google_photos_helper')
        super().__init__('cache')

    def read(
        self,
        cache_file: str
    ):
        return super().read(cache_file)

    def save(
        self,
        files_paths: {} # TODO: Fix type
    ):
        self.logger.debug('Saving caches')
        super().save(files_paths)

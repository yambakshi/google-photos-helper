import logging
from utils.google_photos import init_drive

# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# import os

# Scopes define access level; this one allows read-only access to your photos library
# SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

class GooglePhotosService:
    def __init__(self, cache_service):
        self.logger = logging.getLogger('google_photos_helper')
        # self.drive = init_drive()
        self.cache_service = cache_service

    def scan(
        self,
        is_shared: bool,
        is_in_album: bool,
        is_load_cache: bool,
    ):
        pass

    # def get_service(self):
    #     creds = None
    #     if os.path.exists('token.pickle'):
    #         with open('token.pickle', 'rb') as token:
    #             creds = pickle.load(token)

    #     if not creds:
    #         flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #         with open('token.pickle', 'wb') as token:
    #             pickle.dump(creds, token)

    #     service = build('photoslibrary', 'v1', credentials=creds)

    #     return service

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

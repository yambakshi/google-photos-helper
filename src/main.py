from google_photos_helper import GooglePhotosHelper

def main():
    # service = get_service()

    # print("Fetching all media items...")
    # all_items = list_all_media(service)
    # print(f"Found {len(all_items)} total photos/videos")

    # print("Fetching album items...")
    # album_media_ids = list_album_media_ids(service)
    # print(f"Found {len(album_media_ids)} items that belong to albums")

    # unalbumed = [i for i in all_items if i['id'] not in album_media_ids]
    # print(f"Found {len(unalbumed)} photos not in any album:\n")

    # for i in unalbumed:
    #     print(i['filename'], "-", i['productUrl'])

    google_photos_helper = GooglePhotosHelper()
    google_photos_helper.delete_photos()

if __name__ == '__main__':
    main()

import requests

def create_request(collection_id='2612', image_id='AS086950071500201'):
    url = 'https://earthexplorer.usgs.gov/download/{}/{}/STANDARD/EE'.format(collection_id, image_id)

    return url
def create_request(collection_id='2612', image_id='AS086950071500201'):
    base_url = 'https://earthexplorer.usgs.gov/download/'
    ids = '{}/{}/STANDARD/EE'.format(collection_id, image_id)
    query = base_url + ids
    
    return query
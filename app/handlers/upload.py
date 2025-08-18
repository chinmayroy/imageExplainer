import cgi
import os
import json

UPLOADS_DIR = 'uploads'

def handle_uplaod_request(handler):
    try: 
        form = cgi.FieldStorage(
            fp=handler.rfile,
            headers=handler.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': handler.headers['Content-Type']
            }
        )
    except Exception as e:
        return 500, {'error': 'Failed to parse form data', 'details': str(e)}

    if 'file' not in form:
        return 400, {'eror': 'No "file" field found in the request'}
    
    file_item = form['file']

    if not file_item:
        return 400, {'error': 'File is empty or has no filename'}
    
    filename = os.path.basename(file_item.filename)
    filepath = os.path.join(UPLOADS_DIR, filename)

    try:
        with open(filepath, 'wb') as f:
            f.write(file_item.file.read())
    except IOError as e:
        return 500, {'error': 'Failed to save file on server', 'details': str(e)}
from flask import Blueprint, request, send_file
from .utils import remove_background

main = Blueprint('main', __name__)

@main.route('/remove-bg', methods=['POST'])
def remove_bg():
    print("\n\ncall from frontend\n\n")
    if 'image' not in request.files:
        return {'error': 'No file uploaded'}, 400

    image_file = request.files['image']
    output_bytes = remove_background(image_file.read())
    
    print("\n\nreturning to frontend\n\n")
    return send_file(
        output_bytes,
        mimetype='image/png',
        as_attachment=False,
        download_name='no_bg.png'
    )

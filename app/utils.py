from rembg import remove
import io
import os

def remove_background(input_bytes):
    # Get path to local model file
    model_dir = os.path.join(os.path.dirname(__file__), 'u2net')
    os.environ['U2NET_HOME'] = model_dir  # prevent rembg from downloading
    
    # Remove background using the locally stored u2net.onnx
    result = remove(input_bytes, model_name='u2net')
    return io.BytesIO(result)

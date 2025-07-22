from rembg import remove
import io
import os

def remove_background(input_bytes):
    os.environ["REMBG_SESSION_CACHE_HOME"] = "/opt/render/project/.cache"
    
    # Remove background using the locally stored u2net.onnx
    result =  remove(input_bytes)
    return io.BytesIO(result)

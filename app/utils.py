from rembg import remove
import io
import os

def remove_background(input_bytes):
    
    print("\n\nin utils removebg\n\n")
    os.environ["REMBG_SESSION_CACHE_HOME"] = "/opt/render/project/.cache" 
    
    print("\n\nafter env and calling remove fn\n\n")
    # Remove background using the locally stored u2net.onnx
    result =  remove(input_bytes)
    return io.BytesIO(result)

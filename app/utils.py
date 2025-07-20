from rembg import remove
import io

def remove_background(input_bytes):
    result = remove(input_bytes)
    return io.BytesIO(result)

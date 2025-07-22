import os
import io

# Set rembg cache directory
os.environ["REMBG_SESSION_CACHE_HOME"] = "/opt/render/project/.cache"

from rembg import remove

def remove_background(input_bytes):
    print("\n\n[INFO] In utils.remove_background()\n")

    # Print cache path
    cache_dir = os.environ["REMBG_SESSION_CACHE_HOME"]
    model_path = os.path.join(cache_dir, "u2net", "u2net.onnx")

    print(f"[INFO] Using REMBG_SESSION_CACHE_HOME: {cache_dir}")
    print(f"[INFO] Checking if model exists at: {model_path}")
    
    if os.path.exists(model_path):
        print("[SUCCESS] u2net.onnx FOUND ✅")
    else:
        print("[WARNING] u2net.onnx NOT FOUND ❌ — rembg will download it")

    print("[INFO] Calling rembg.remove()...\n")

    result = remove(input_bytes)

    print("[INFO] Background removal complete.\n")
    return io.BytesIO(result)

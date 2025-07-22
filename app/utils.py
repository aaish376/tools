import os
import io
from rembg import new_session, remove

# Set this before anything else, even before imports ideally (but fine here)
os.environ["REMBG_SESSION_CACHE_HOME"] = "/opt/render/project/.cache"

# Create a session that uses your custom model directory
session = new_session("u2net")  # Will respect the env var

def remove_background(input_bytes):
    print("\n\n[INFO] In utils.remove_background()\n")

    cache_dir = os.environ["REMBG_SESSION_CACHE_HOME"]
    model_path = os.path.join(cache_dir, "u2net", "u2net.onnx")

    print(f"[INFO] Using REMBG_SESSION_CACHE_HOME: {cache_dir}")
    print(f"[INFO] Checking if model exists at: {model_path}")

    if os.path.exists(model_path):
        print("[SUCCESS] u2net.onnx FOUND ✅")
    else:
        print("[WARNING] u2net.onnx NOT FOUND ❌ — rembg may download it")

    print("[INFO] Calling rembg.remove() with session...\n")

    result = remove(input_bytes, session=session)

    print("[INFO] Background removal complete.\n")
    return io.BytesIO(result)

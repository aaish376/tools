import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',  # Allow external access (e.g., by Render)
        port=int(os.environ.get('PORT', 5000))  # Use PORT from environment, default to 5000
    )

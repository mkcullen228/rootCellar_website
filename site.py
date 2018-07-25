import sys
import os
print("site.py")
print('\n'.join(sys.path))
from app import app
from app import db
# from flask import requests
# from app.mode import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run()


# if __name__ == '__main__':
#     app.debug = True
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)

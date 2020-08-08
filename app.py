from flask import Flask
from flask_cors import CORS

from routes.user import user_router

app = Flask(__name__)

CORS(app=app)

app.register_blueprint(user_router, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)

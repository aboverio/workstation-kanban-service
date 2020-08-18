import os
from flask import Flask
from mongoengine import connect
from flask_cors import CORS
from dotenv import load_dotenv

from routes.user import user_router
from errors import error_handlers

load_dotenv()

app = Flask(__name__)

CORS(app=app)

app.register_blueprint(user_router, url_prefix='/users')
app.register_blueprint(error_handlers)

if __name__ == '__main__':
    flask_env = os.environ.get('FLASK_ENV')
    connect(host=os.environ.get('MONGODB_HOST'))
    if flask_env is None or flask_env != 'production':
        app.run(debug=True)
    else:
        app.run(debug=False)
